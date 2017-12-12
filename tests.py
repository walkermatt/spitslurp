import unittest
import tempfile
from spitslurp import spit, slurp


class TestSpit(unittest.TestCase):

    def test_default(self):
        with tempfile.NamedTemporaryFile() as temp_file:
            txt = u'Hello\nWorld\n'
            self.assertEqual(spit(temp_file.name, txt), txt)
            self.assertEqual(slurp(temp_file.name), txt)


class TestSlurp(unittest.TestCase):

    def test_default(self):
        with tempfile.NamedTemporaryFile() as temp_file:
            txt = u'Hello\nWorld\n'
            spit(temp_file.name, txt)
            self.assertEqual(slurp(temp_file.name), txt)

if __name__ == '__main__':
    unittest.main()
