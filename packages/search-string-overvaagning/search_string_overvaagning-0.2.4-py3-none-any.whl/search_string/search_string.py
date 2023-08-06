from __future__ import annotations

import re
from typing import Generic, Iterable, TypeVar, Union

Data = TypeVar('Data')

MAX_SENTENCE_CHARS = 1000
SENTENCE_BREAK = '(...)'
GLOBAL = '!global'
REGEX_SPECIAL_CHARS = r'\.|()[]{}^$*+?-'

_REGEX_SPECIAL_CHARS = REGEX_SPECIAL_CHARS + ';~'
_REGEX_SPECIAL_CHARS_RE = re.compile('|'.join('\\' + c for c in _REGEX_SPECIAL_CHARS))

WORD_BOUNDARY, WORD_BOUNDARY_CHAR = r'\b', '~'
PURE_WORD_BOUNDARY_RE = re.compile(r'^[\s~]*$')

# Some random characters that are highly unlikely to be in a word
UNCOMMON_CHARS = 'ДЖЖЖДЖЖЖД'


class SearchString(Generic[Data]):
    """
    A SearchString class. It is used for searching a text. For something to be
    deemed a match, the text must match the `first_str` and if the `second_str`
    is not empty, the text must also match the `second_str`. If the `not_str`
    is not empty, the text must *not* match the `not_str`. A logical AND is
    used between the three conditions. The three strings can each be a
    collection of strings separated by semicolons wherein a match is deemed by
    logical OR. You can use '~' to make a word boundary. Finally, you can use
    `!global` at the end of a string to signal that that part should check
    globally.

    Example:
    >>> ss = SearchString('example;hello', 'text', 'elephant', data=None)
    >>> ss.match('This is an example text')
    True
    >>> ss.match('This text says hello')
    True
    >>> ss.match('This is just an example')
    False
    >>> ss.match('This is an example text with an elephant')
    False
    >>> SearchString('', '', '', data=None).match('https://example.com')
    True
    >>> arla_ss1 = SearchString('arla', '', '', data=None)
    >>> arla_ss2 = SearchString('~arla~', '', '', data=None)
    >>> arla_ss1.match('A text about Arla')
    True
    >>> arla_ss2.match('A text about Arla')
    True
    >>> arla_ss1.match('The European Parlament')
    True
    >>> arla_ss2.match('The European Parlament')
    False
    >>> arla_ss2.highlight('A text about Arla')
    'A text about <b>Arla</b>'
    """
    __slots__ = (
        'data',
        'first_str',
        'first_str_global',
        'second_str',
        'second_str_global',
        'show_third_in_repr',
        'third_str',
        'third_str_global',
        'not_str',
        'not_str_global',
        'matched_sentences',
        '_any_global',
    )

    def __init__(
        self,
        first_str: str,
        second_str: str,
        not_str: str,
        *,
        data: Data,
        third_str: str | None = None
    ) -> None:
        self.data = data

        search_str, first_str_global = self._preprocess_string(first_str)
        self.first_str = search_str
        self.first_str_global = first_str_global

        search_str, second_str_global = self._preprocess_string(second_str)
        self.second_str = search_str
        self.second_str_global = second_str_global

        self.show_third_in_repr = third_str is not None
        search_str, third_str_global = self._preprocess_string(third_str or '')
        self.third_str = search_str
        self.third_str_global = third_str_global

        search_str, not_str_global = self._preprocess_string(not_str)
        self.not_str = search_str
        self.not_str_global = not_str_global

        self.matched_sentences: list[str] = []
        self._any_global = any([
            first_str_global,
            second_str_global,
            third_str_global,
            not_str_global,
        ])

    def _escape_pattern(self, raw_pattern: str) -> str | None:
        """
        Takes a raw pattern and escapes all regex special characters. Finally,
        substitutes '~' to '\b' to make it a word boundary. Returns a compiled
        regex pattern or None if the pattern is empty.

        NB: The `re.escape` function also exists, but it escapes all special
        chars, not just special chars in the regex.
        """
        if not raw_pattern:
            return None

        pattern = raw_pattern
        for bad_char in REGEX_SPECIAL_CHARS:
            pattern = pattern.replace(bad_char, f'\\{bad_char}')

        if PURE_WORD_BOUNDARY_RE.match(pattern):
            return None

        pattern = pattern.replace(WORD_BOUNDARY_CHAR, WORD_BOUNDARY)
        return pattern

    def _pop_sentence_break_if_needed(self) -> None:
        """
        Removes the last sentence break from the matched sentences list, if
        there is one
        """
        ms = self.matched_sentences
        if ms and ms[-1] == SENTENCE_BREAK:
            ms.pop()

    def _reset_matched_sentences(self) -> None:
        """Reset the matched sentences list to an empty list"""
        self.matched_sentences = []

    def _preprocess_string(self, string: str) -> tuple[None | re.Pattern | str, bool]:
        """
        Preprocesses a single string into a list of patterns.

        >>> ss = SearchString('', '', '', None)
        >>> ss._preprocess_string('A;sample;searchString~;')
        re.compile('a|sample|searchstring\\b'), False
        >>> ss._preprocess_string('')
        (None, False)
        >>> ss._preprocess_string(';;;;')
        (None, False)
        >>> ss._preprocess_string('   ~   ')
        (None, False)
        >>> ss._preprocess_string('ritzau!global')
        (re.compile('ritzau'), True)
        """
        if not isinstance(string, str):
            raise TypeError(
                f'Search strings must be strings, but received value {string} '
                + f'of type {type(string)} for SS.data={self.data}'
            )

        is_global = False
        cleaned = string.strip(';').lower()
        if cleaned.endswith(GLOBAL):
            cleaned = cleaned[:-len(GLOBAL)]
            is_global = True

        final_str = cleaned.rstrip(';')
        if not final_str:
            return None, is_global

        parts = final_str.split(';')
        full_pattern = '|'.join(filter(None, map(self._escape_pattern, parts)))
        if not full_pattern:
            return None, is_global

        # if not any(char in final_str for char in _REGEX_SPECIAL_CHARS):
        if not _REGEX_SPECIAL_CHARS_RE.search(final_str):
            return final_str, is_global

        return re.compile(full_pattern, flags=re.IGNORECASE), is_global

    def _any_match(
        self,
        text: str,
        re_pattern: None | re.Pattern | str,
        empty_ret: bool = True,
    ) -> bool:
        """
        Returns a bool indicating whether the pattern matches the text.
        In case the pattern is empty, the empty_ret value is returned.
        """
        if not re_pattern:
            return empty_ret

        return (
            re_pattern in text.lower()
            if isinstance(re_pattern, str)
            else bool(re_pattern.search(text))
        )

    def _match_sentence(self, sentence: str) -> bool:
        """
        Returns a bool indicating whether the text from a single sentence
        matches the search string. If you need to check multiple sentences,
        use `match_sentences` which takes global search strings into account.

        Example:
        >>> ss = SearchString('example;hello', 'text', 'elephant', None)
        >>> ss._match_sentence('This is an example text')
        True
        >>> ss._match_sentence('This text says hello')
        True
        >>> ss._match_sentence('This is just an example')
        False
        >>> ss._match_sentence('This is an example text with an elephant')
        False
        """
        is_match = (
            self._any_match(sentence, self.first_str)
            and self._any_match(sentence, self.second_str)
            and self._any_match(sentence, self.third_str)
            and not self._any_match(sentence, self.not_str, empty_ret=False)
        )
        if is_match:
            self.matched_sentences = [sentence[:MAX_SENTENCE_CHARS]]

        return is_match

    def _match_sentences(self, sentences: list[str]) -> bool:
        """
        Returns a bool indicating whether the text from multiple sentences
        matches the search string. Takes global search strings into account.
        Mutates the instance variable `matched_sentences` list inplace.

        Example:
        >>> ss = SearchString('bornholm;samsø', '', 'ritzau!global', None)
        >>> ss._match_sentences(['Bornholm is a nice island', 'ritzau'])
        False
        >>> ss._match_sentences(['Bornholm is a nice island', 'Sentence 2'])
        True
        >>> ss._match_sentences(['Samsø is a nice island - ritzau', ''])
        False
        """
        self._reset_matched_sentences()

        # Check, if needed, if there are any global matches
        fst_global, snd_global, third_global, not_global \
            = False, False, False, False

        if self._any_global:
            full_text = '\n\n'.join(sentences)
            if self.first_str_global:
                fst_global = self._any_match(full_text, self.first_str)
            if self.second_str_global:
                snd_global = self._any_match(full_text, self.second_str)
            if self.third_str_global:
                third_global = self._any_match(full_text, self.third_str)
            if self.not_str_global:
                not_global = self._any_match(full_text, self.not_str,
                                             empty_ret=False)
                if not_global:  # If there is a global not match, we can stop
                    return False

        # Check if there is a match in any of the sentences
        found_match, found_last_iter = False, False
        for sentence in sentences:
            is_match = (
                (fst_global or self._any_match(sentence, self.first_str))
                and (snd_global or self._any_match(sentence, self.second_str))
                and (third_global or self._any_match(sentence, self.third_str))
                and not (self._any_match(sentence, self.not_str,
                                         empty_ret=False))
            )
            if is_match:
                self.matched_sentences.append(sentence[:MAX_SENTENCE_CHARS])
                found_match = True
                found_last_iter = True
            elif found_last_iter:
                self.matched_sentences.append(SENTENCE_BREAK)
                found_last_iter = False

        self._pop_sentence_break_if_needed()
        return found_match

    def match(self, text: str | list[str]) -> bool:
        """
        Returns a bool indicating whether the text matches the search string.
        The text can either be a single sentence or a list of sentences. If a
        list of sentences is given, global search strings are taken into
        account.
        After a match has been found, the `matched_sentences` property is set
        as well and possible to get by accessing the property `matched_text`.

        Example:
        >>> ss = SearchString('example;hello', 'text', 'elephant', None)
        >>> ss.match('This is an example text')
        True
        >>> ss.match('This text says hello')
        True
        >>> ss.match('This is just an example')
        False
        >>> ss.match('This is an example text with an elephant')
        False
        >>> ss.match(['This is an example text', 'This is just an example'])
        True
        >>> sentences = ['This is an example text', 'This is just an example',
        ...              'This is an example text with an elephant']
        >>> ss.match(sentences)
        True
        >>> ss2 = SearchString('example;hello', 'text', 'elephant/global', None)
        >>> ss2.match(sentences)
        False
        """
        return (self._match_sentence(text)
                if isinstance(text, str) else
                self._match_sentences(text))

    def highlight(self, text: str) -> str:
        """
        Returns a string with the text matching the search string highlighted.
        The highlights are wrapped in <b>[MATCHED TEXT]</b> tags.
        """
        try:
            subbed = text
            for re_pattern in [self.first_str, self.second_str, self.third_str]:
                if re_pattern is None:
                    continue
                elif isinstance(re_pattern, str):
                    subbed = re.sub(re_pattern, r'<b>\g<0></b>', subbed, flags=re.IGNORECASE)
                else:
                    subbed = re_pattern.sub(r'<b>\g<0></b>', subbed)

            return subbed
        except Exception:
            return text

    def _pattern_to_str(
        self,
        re_pattern: None | re.Pattern | str,
        is_global: bool,
    ) -> str:
        """
        Returns a string representation of the list of patterns for one of the
        search string parts
        """
        if re_pattern is None:
            return '-'

        if isinstance(re_pattern, str):
            return re_pattern

        replaced = re_pattern.pattern\
            .replace('|', ';')\
            .replace(WORD_BOUNDARY, WORD_BOUNDARY_CHAR)\
            .replace('\\\\', UNCOMMON_CHARS)\
            .replace('\\', '')\
            .replace(UNCOMMON_CHARS, '\\')
        return replaced + (GLOBAL if is_global else '')

    def _get_inner(self) -> str:
        """
        Returns the inner part of the string representation without
        parentheses surrounding the search string parts

        Example
        >>> ss = SearchString('an;example~', '', 'not-str!global', data=1)
        >>> ss._get_inner()
        'an;example~, -, not-str!global'
        """
        first_str = self._pattern_to_str(self.first_str, self.first_str_global)
        second_str = self._pattern_to_str(self.second_str, self.second_str_global)
        to_join = [first_str, second_str]
        if self.show_third_in_repr:
            third_str = self._pattern_to_str(self.third_str, self.third_str_global)
            to_join.append(third_str)
        not_str = self._pattern_to_str(self.not_str, self.not_str_global)
        to_join.append(not_str)
        return ', '.join(to_join)

    def __str__(self) -> str:
        """
        Returns a string representation of the search string

        Example
        >>> ss = SearchString('an;example~', '', 'not-str!global', data=1)
        >>> str(ss)
        (an;example~, -, not-str!global)
        """
        return f'({self._get_inner()})'

    def __repr__(self) -> str:
        """
        Returns a string representation of the search string

        Example
        >>> SearchString('an;example~', '', 'not-str!global', data=1)
        SearchString(an;example~, -, not-str!global, data=1)
        """
        inner = self._get_inner()
        if self.data is not None:
            inner += f', data={self.data}'

        return f'SearchString({inner})'

    @property
    def long_str(self) -> str:
        """Long multiline string representation of the SearchString"""
        fst_str = self._pattern_to_str(self.first_str, self.first_str_global)
        snd_str = self._pattern_to_str(self.second_str, self.second_str_global)
        third_str = self._pattern_to_str(self.third_str, self.third_str_global)
        not_str = self._pattern_to_str(self.not_str, self.not_str_global)
        return '\n\n'.join([
            f'{self.data}-søgeord',
            f'Første søgestreng: {fst_str}',
            f'Anden søgestreng: {snd_str}',
            *([f'Tredje søgestreng: {third_str}'] if self.show_third_in_repr else []),
            f'NOT-søgestreng: {not_str}',
        ])

    @property
    def simple_string(self) -> str:
        """
        If the search string only contains the `first_str`, this property
        returns only that part. Otherwise, it returns the full string
        representation of the search string.
        """
        if self.second_str is None and self.not_str is None:
            return self._pattern_to_str(self.first_str, self.first_str_global)
        return str(self)

    @property
    def matched_text(self) -> str | None:
        """
        Returns the matched text as a string, joined around '(...)'. If no
        text was matched, None is returned.
        """
        if not self.matched_sentences:
            return None

        return ' '.join(self.matched_sentences)

    @property
    def matched_text_highlighted(self) -> str | None:
        """
        Returns the matched text highlighted with <b> tags as a string,
        joined around '(...)'. If no text was matched, None is returned.
        """
        if self.matched_sentences is None:
            return None

        return ' '.join([self.highlight(sentence)
                         for sentence in self.matched_sentences])

    @staticmethod
    def find_one(
        text: str | list[str],
        search_strings: Iterable[SearchString],
    ) -> SearchString | None:
        """
        Finds the first match of the search strings for the text or list of
        text fragments and returns the given search string. If no match is
        found, None is returned. Should be used when there logically only can
        be one match.

        Example:
        >>> ss = [SearchString('test', str(i), '', data=i) for i in range(500)]
        >>> result = SearchString.find_one('test 123', ss)
        >>> result.data if result else None
        1
        >>> result.matched_text if result else None
        'test 123'
        """
        for search_string in search_strings:
            if search_string.match(text):
                return search_string
        return None

    @staticmethod
    def find_all(
        text: Union[str, list[str]],
        search_strings: Iterable[SearchString],
    ) -> list[SearchString]:
        """
        Finds all matches of the search strings for the text or list of text
        fragments. Returns a list of the matched searchstrings. If none is found,
        the list is empty. Should be used when there can be multiple matches.

        Example:
        >>> ss = [SearchString('test', str(i), '', data=i) for i in range(500)]
        >>> results = SearchString.find_all(['test 12', 'test 9'], ss)
        >>> [(r.data, r.matched_text) for r in results]
        [(1, 'test 12'), (2, 'test 12'), (9, 'test 9'), (12, 'test 12')]
        """
        return [ss for ss in search_strings if ss.match(text)]

    @staticmethod
    def find_all_sliding_window(
        text: str,
        search_strings: Iterable[SearchString],
        *,
        window_size: int = 300,
        step_size: int = 20,
    ) -> list[SearchString]:
        """
        Find matches based on a sliding window method. Can be used if
        underlying text is unsuitable for section- or sentence-tokenization
        but it should still be enforced that matched text parts are not too
        far apart.
        Returns a list of all the search strings that matched some window
        of the supplied text.
        You can tune the sliding window using the `window_size` and
        `step_size` parameters.

        Example:
        >>> ss = [SearchString('part1', 'part2', 'bad', data=None)]
        >>> text = (' ' * 200).join(['part1', 'part2', 'bad.'])
        >>> SearchString.find_all_sliding_window(text, ss, window_size=100)
        []
        >>> SearchString.find_all_sliding_window(text, ss, window_size=250)
        [SearchString(part1, part2, bad)]
        >>> SearchString.find_all_sliding_window(text, ss, window_size=500)
        []
        """
        matched_ss_data = set()
        ret_val = []
        for start_idx in range(0, len(text), step_size):
            window = text[start_idx:start_idx+window_size]
            for ss in search_strings:
                if ss.data not in matched_ss_data and ss.match(window):
                    matched_ss_data.add(ss.data)
                    ret_val.append(ss)
        return ret_val
