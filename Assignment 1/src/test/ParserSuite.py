import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;
        Function: main
        Body:
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """
            Var: x = 1;
            Function: main
                Parameter: a[5], b
                Body:

                    writeln(i);

                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))