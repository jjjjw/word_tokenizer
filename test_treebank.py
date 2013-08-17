from unittest import TestCase
from treebank import Treebanklike


class TestTreebank(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tokenizer = Treebanklike()
        cls.sentence = '''Good muffins cost $3.88\nin New York.  Please buy me... two of them.\n\nThanks.'''
        cls.expectation = ['Good', 'muffins', 'cost', '$', '3', '.', '88', 'in', 'New', 'York', '.', 'Please', 'buy', 'me', '...', 'two', 'of', 'them', '.', 'Thanks', '.']

    def test_tokenizer(self):
        res = self.tokenizer(self.sentence)
        res = list(res)
        self.assertEqual(res, self.expectation)


if __name__ == '__main__':
    from unittest import main

    main()
