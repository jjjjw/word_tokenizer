"""
Penn Treebank Tokenizer

The Treebank tokenizer uses regular expressions to tokenize text as in Penn Treebank.
This implementation is a port of the tokenizer sed script written by Robert McIntyre
and available at http://www.cis.upenn.edu/~treebank/tokenizer.sed.

In due course, this python module then is a total rip off of the NLTK module available at
https://github.com/nltk/nltk/blob/master/nltk/tokenize/treebank.py

Reformulated using the tokenizer recipe here:
http://docs.python.org/3.2/library/re.html#writing-a-tokenizer

Very silly indeed.

"""
from re import compile as re_compile
from re import escape as re_escape
from string import punctuation


class Treebank():
    @property
    def token_spec(self):
        """The definitions used for English tokens.

        """
        if not hasattr(self, '_spec'):
            punct = punctuation.replace('"', "")
            punct = punctuation.replace("'", "")

            self._spec = (
                ('PUNCTUATION', r'[{}]'.format(re_escape(punct))),
                ('QUOTATION', re_escape(r'"')),
                ('APOSTROPHE', re_escape(r"'")),
            )

        return self._spec

    @property
    def token_pairs(self):
        for name, pattern in self.token_spec:
            yield '(?P<{}>{})'.format(name, pattern)

    @property
    def tokens_re(self):
        if not hasattr(self, '_tokens_re'):
            tokens_re = '|'.join(self.token_pairs)
            self._tokens_re = re_compile(tokens_re)

        return self._tokens_re

    def tokenize(self, text: str):
        return self.tokens_re.match(text)
