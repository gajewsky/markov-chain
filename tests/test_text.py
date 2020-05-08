import unittest

from markov_chain.text import Text

class TestText(unittest.TestCase):
    def test_text(self):
        """
        Test that it correctly calculates successors words probability
        """
        input_text = "foo bar foo adin dwa foo bar"
        expected_result = { 
            "foo":  {"adin": 1/3, "bar": 2/3},
            "bar":  {"foo": 1},
            "adin": {"dwa": 1},
            "dwa":  {"foo": 1},
        }

        analized_text = Text(input_text).analyze()
        self.assertEqual(analized_text, expected_result)

if __name__ == '__main__':
    unittest.main()
