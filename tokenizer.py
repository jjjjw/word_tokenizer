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
from functools import reduce
from re import compile as re_compile
from re import escape as re_escape
from re import sub as re_sub
from string import punctuation

 def token_spec() -> type(re_compile('')):
    """The tokenization steps.

    """
    spec = (
        ('PUNCTUATION', r'[%s]' % re_escape(punctuation)),
        ('WORD',  r'\b\w\b'),
    )

    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in spec
    return re_compile(tok_regex)



 def tokenize(sentence: str): # -> list:
    """
    >>> from tokenizer import tokenize
    >>> s = '''Good muffins cost $3.88\\nin New York.  Please buy me\\ntwo of them.\\nThanks.'''
    >>> tokenize(s)
    ['Good', 'muffins', 'cost', '$', '3.88', 'in', 'New', 'York.', 'Please', 'buy', 'me', 'two', 'of', 'them.', 'Thanks', '.']
    >>> s = "They'll save and invest more."
    >>> tokenize(s)
    ['They', "'ll", 'save', 'and', 'invest', 'more', '.']

    """
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification



if __name__ == "__main__":
    from doctest import testmod
    from doctest import NORMALIZE_WHITESPACE

    testmod(optionflags=NORMALIZE_WHITESPACE)
