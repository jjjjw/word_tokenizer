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
    def token_spec():
        """The definitions used for English tokens.

        """
        punct = punctuation.replace('"', None)
        punct = punctuation.replace("'", None)

        spec = (
            ('PUNCTUATION', r'[%s]' % re_escape(punct)),
            ('QUOTATION', r'"'),
            ('APOSTROPHE', r"'"),
        )

        return spec

    @property
    def tokens_re():
        if not hasattr(self, '_tokens_re'):
            tokens_re = '|'.join('(?P<%s>%s)' % pair for pair in self.token_spec
            self._tokens_re = re_compile(tokens_re)

        return self._tokens_re
