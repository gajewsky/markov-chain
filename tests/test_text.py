import unittest

from markov_chain.text import Text

class TestText(unittest.TestCase):
    def test_text(self):
        """
        Test that it correctly counds successors words
        """
        input_text = "foo bar foo adin dwa foo bar"
        expected_result = { 
            "foo":  {"bar": 2, "adin": 1},
            "bar":  {"foo": 1},
            "adin": {"dwa": 1},
            "dwa":  {"foo": 1},
        }

        word_stats = Text(input_text).word_stats()
        self.assertEqual(word_stats, expected_result)

if __name__ == '__main__':
    unittest.main()
