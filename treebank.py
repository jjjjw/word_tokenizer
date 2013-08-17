"""
Penn Treebanklike Tokenizer

The Treebanklike tokenizer uses regular expressions to tokenize text as in Penn Treebank.
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


class Treebanklike():
    @property
    def token_spec(self):
        """The definitions used for English tokens.

        """
        if not hasattr(self, '_spec'):
            punct = re_escape(punctuation)
            punct = r'[{}]'.format(punct)

            # Order matters for this spec, for example, punctuation contains a period but we want to capture ellipses.
            self._spec = (
                ('WORD', r'\w+'),
                ('ELLIPSES', re_escape(r'...')),
                ('QUOTATION', re_escape(r'"')),
                ('PUNCTUATION', punct),
            )

        return self._spec

    @property
    def token_patterns(self):
        """Yields the pattern groups.

        """
        for type_, pattern in self.token_spec:
            yield '(?P<{}>{})'.format(type_, pattern)

    @property
    def tokens_re(self) -> type(re_compile(r'')):
        """Compiles the token regex for use.

        """
        if not hasattr(self, '_tokens_re'):
            tokens_re = '|'.join(self.token_patterns)
            self._tokens_re = re_compile(tokens_re)

        return self._tokens_re

    def __call__(self, text: str):
        """Yields tokens.

        """
        in_quote = False

        for mo in self.tokens_re.finditer(text):
            type_ = mo.lastgroup
            token = mo.group()

            if type_ == "QUOTATION":
                if in_quote:
                    in_quote = False
                    token = "''"
                else:
                    in_quote = True
                    token = "``"

            yield token
