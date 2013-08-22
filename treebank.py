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


def lazy_initialization(func):
    """Decorates object properties to be lazily instantiated.

    """
    def dec(*args):
        self = args[0]  # Hazard!
        prop = "_" + func.__name__

        if not hasattr(self, prop):
            val = func(*args)
            setattr(self, prop, val)

        return getattr(self, prop)

    return dec


class Treebanklike():

    @property
    @lazy_initialization
    def token_spec(self):
        """The definitions used for English tokens.

        """
        punct = re_escape(punctuation)
        punct = r'[{}]'.format(punct)

        # Order matters for this spec, for example, punctuation contains a period but we want to capture ellipses.
        spec = (
            ('WORD', r'\w+'),
            ('ELLIPSES', re_escape(r'...')),
            ('QUOTATION', re_escape(r'"')),
            ('PUNCTUATION', punct),
        )

        return spec

    @property
    def token_patterns(self):
        """Yields the pattern groups.

        """
        for type_, pattern in self.token_spec:
            yield '(?P<{}>{})'.format(type_, pattern)

    @property
    @lazy_initialization
    def tokens_re(self):
        """Compiles the token regex for use.

        """
        tokens_re = '|'.join(self.token_patterns)
        tokens_re = re_compile(tokens_re)

        return tokens_re

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
