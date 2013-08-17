from unittest import TestCase
from treebank import Treebanklike


class TestTreebank(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tokenizer = Treebanklike()

    def compare(self, sentence, expectation):
        res = self.tokenizer(sentence)
        res = list(res)
        self.assertEqual(expectation, res)

    def test_basic_punctuation(self):
        """It should return words and punctuation as discrete tokens.

        """
        sentence = '''Good muffins cost $3.88\nin New York.  Please buy me... two of them.\n\nThanks.'''
        expectation = ['Good', 'muffins', 'cost', '$', '3', '.', '88', 'in', 'New', 'York', '.', 'Please', 'buy', 'me', '...', 'two', 'of', 'them', '.', 'Thanks', '.']

        self.compare(sentence, expectation)

    def test_quotation_disambiguation(self):
        """It should distinguish between beginning (``) and ending ('') quotes.

        """
        sentence = '''"Good muffins" cost $3.88\nin New York.  Please buy me... two of them.\n\nThanks.'''
        expectation = ["``", 'Good', 'muffins', "''", 'cost', '$', '3', '.', '88', 'in', 'New', 'York', '.', 'Please', 'buy', 'me', '...', 'two', 'of', 'them', '.', 'Thanks', '.']

        self.compare(sentence, expectation)

    def test_possesives_and_contractions(self):
        """It should return discrete/dumb tokens rather than guessing at the meaning.

        """
        sentence = '''Good muffin's cost $3.88\nin New York.  Please'nt buy me... two of them.\n\nThanks.'''
        expectation = ['Good', "muffin", "'", "s", 'cost', '$', '3', '.', '88', 'in', 'New', 'York', '.', 'Please', "'", "nt", 'buy', 'me', '...', 'two', 'of', 'them', '.', 'Thanks', '.']

        self.compare(sentence, expectation)


if __name__ == '__main__':
    from unittest import main

    main()
