"""
Penn Treebank Tokenizer

The Treebank tokenizer uses regular expressions to tokenize text as in Penn Treebank.
This implementation is a port of the tokenizer sed script written by Robert McIntyre
and available at http://www.cis.upenn.edu/~treebank/tokenizer.sed.

In due course, this python module then is a total rip off of the NLTK module available at
https://github.com/nltk/nltk/blob/master/nltk/tokenize/treebank.py

Very silly indeed.

"""
from functools import reduce
from re import sub as re_sub


def _steps() -> tuple:
    """The tokenization steps.

    """
    #starting quotes
    def step1(text: str) -> str:
        return re_sub(r'^\"', r'``', text)

    def step2(text: str) -> str:
        return re_sub(r'(``)', r' \1 ', text)

    def step3(text: str) -> str:
        return re_sub(r'([ (\[{<])"', r'\1 `` ', text)

    #punctuation
    def step4(text: str) -> str:
        return re_sub(r'([:,])([^\d])', r' \1 \2', text)
    def step5(text: str) -> str:
        return re_sub(r'\.\.\.', r' ... ', text)
    def step6(text: str) -> str:
        return re_sub(r'[;@#$%&]', r' \g<0> ', text)
    def step7(text: str) -> str:
        return re_sub(r'([^\.])(\.)([\]\)}>"\']*)\s*$', r'\1 \2\3 ', text)
    def step8(text: str) -> str:
        return re_sub(r'[?!]', r' \g<0> ', text)

    # ???
    def step9(text: str) -> str:
        return re_sub(r"([^'])' ", r"\1 ' ", text)

    #parens, brackets, etc.
    def step10(text: str) -> str:
        return re_sub(r'[\]\[\(\)\{\}\<\>]', r' \g<0> ', text)
    def step11(text: str) -> str:
        return re_sub(r'--', r' -- ', text)

    #add extra space to make things easier
    def step12(text: str) -> str:
        return " " + text + " "

    #ending quotes
    def step13(text: str) -> str:
        return re_sub(r'"', " '' ", text)
    def step14(text: str) -> str:
        return re_sub(r'(\S)(\'\')', r'\1 \2 ', text)

    def step15(text: str) -> str:
        return re_sub(r"([^' ])('[sS]|'[mM]|'[dD]|') ", r"\1 \2 ", text)
    def step16(text: str) -> str:
        return re_sub(r"([^' ])('ll|'LL|'re|'RE|'ve|'VE|n't|N'T) ", r"\1 \2 ",
                  text)

    # Order matters...
    return tuple(locals().values())


STEPS = _steps()


def word_tokenize(sentence: str) -> list:
    """
    No regressions so far!

    >>> from treebank import word_tokenize
    >>> s = '''Good muffins cost $3.88\\nin New York.  Please buy me\\ntwo of them.\\nThanks.'''
    >>> word_tokenize(s)
    ['Good', 'muffins', 'cost', '$', '3.88', 'in', 'New', 'York.', 'Please', 'buy', 'me', 'two', 'of', 'them.', 'Thanks', '.']
    >>> s = "They'll save and invest more."
    >>> word_tokenize(s)
    ['They', "'ll", 'save', 'and', 'invest', 'more', '.']

    """
    return reduce(lambda x, y: y(x), STEPS, sentence).split()


if __name__ == "__main__":
    from doctest import testmod
    from doctest import NORMALIZE_WHITESPACE

    testmod(optionflags=NORMALIZE_WHITESPACE)
