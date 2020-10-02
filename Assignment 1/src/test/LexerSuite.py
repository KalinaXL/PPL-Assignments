import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    # def test_lower_identifier(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>", 1))

    # def test_lower_upper_id(self):
    #     self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>", 2))

    # def test_wrong_token(self):
    #     self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?", 3))

    # def test_integer(self):
    #     """test integers"""
    #     self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>", 4))

    # def test_illegal_escape(self):
    #     """test illegal escape"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""", 5))

    # def test_unterminated_string(self):
    #     """test unclosed string"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """, 6))

    # def test_normal_string_with_escape(self):
    #     """test normal string with escape"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""", 7))
    # def test_unterminated_comment(self):
    #     input ="""
    #     ** This is a
    #     * multi-line
    #     * comment
    #     **"""
    #     self.assertTrue(TestLexer.checkLexeme(input, "<EOF>", 8))
    # def test_case_9(self):
    #     input = """
    #     "this is a string'"\k"
    #     """
    #     self.assertTrue(TestLexer.checkLexeme(input, """Illegal Escape In String: this is a string'"\k""", 9))
    # def test_case_10(self):
    #     input = "0o0423"
    #     self.assertTrue(TestLexer.checkLexeme(input, "0o0,423,<EOF>", 10))
    # def test_case_11(self):
    #     input = "Ask"
    #     self.assertTrue(TestLexer.checkLexeme(input, "Error Token A", 11))
    # def test_case_12(self):
    #     input = "Var: x = 12e-5;";
    #     self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,=,12e-5,;,<EOF>", 12))
    # def test_case_13(self):
    #     input = "Var: a = {1,2,43;";
    #     self.assertTrue(TestLexer.checkLexeme(input, "Var,:,a,=,{,1,,,2,,,43,;,<EOF>", 13))
    # def test_case_14(self):
    #     input = "a[3 + foo(2)] = a[b[2][3]] + 4;"
    #     self.assertTrue(TestLexer.checkLexeme(input, "a,[,3,+,foo,(,2,),],=,a,[,b,[,2,],[,3,],],+,4,;,<EOF>", 14))
    # def test_case_15(self):
    #     input = "**this a commen(*$^*%&#^&**"
    #     self.assertTrue(TestLexer.checkLexeme(input, "<EOF>", 15))
    # def test_case_16(self):
    #     input = "**this is a comment*&^52465"
    #     self.assertTrue(TestLexer.checkLexeme(input, "Unterminated Comment", 16))
    # def test_case_17(self):
    #     input = "**just a comment*(&^%&*"
    #     self.assertTrue(TestLexer.checkLexeme(input, "Unterminated Comment", 17))
    # def test_case_18(self):
    #     input = """
    #     Function: main
    #     Body:
    #         x = 10;
    #         fact(x);
    #     EndBody.
    #     """
    #     self.assertTrue(TestLexer.checkLexeme(input, "Function,:,main,Body,:,x,=,10,;,fact,(,x,),;,EndBody,.,<EOF>", 18))
    # def test_case_19(self):
    #     input = """ "string \\\ string\\' hjg" """
    #     self.assertTrue(TestLexer.checkLexeme(input, "string \\\ string\\' hjg,<EOF>", 19))
    # def test_case_20(self):
    #     input = "v = (4. \. 3.) *. 3.14 *. r *. r *. r;"
    #     self.assertTrue(TestLexer.checkLexeme(input, "v,=,(,4.,\.,3.,),*.,3.14,*.,r,*.,r,*.,r,;,<EOF>", 20))
    # def test_case_21(self):
    #     input = """
    #     "hjagfysugd'"afsdg'"agd"
    #     """
    #     self.assertTrue(TestLexer.checkLexeme(input, """hjagfysugd'"afsdg'"agd,<EOF>""", 21))
    def test_case_22(self):
        input = """
        "fklasjghs'"assgf'\""""
        self.assertTrue(TestLexer.checkLexeme(input, """Unclosed String: fklasjghs'"assgf'\"""",22))
    # def test_case_10(self):
    #     input = ""
    #     self.assertTrue(TestLexer.checkLexeme(input, "", 110))
    # def test_case_10(self):
    #     input = ""
    #     self.assertTrue(TestLexer.checkLexeme(input, "", 110))
    # def test_case_10(self):
    #     input = ""
    #     self.assertTrue(TestLexer.checkLexeme(input, "", 110))
    # def test_case_10(self):
    #     input = ""
    #     self.assertTrue(TestLexer.checkLexeme(input, "", 110))
    # def test_case_10(self):
    #     input = ""
    #     self.assertTrue(TestLexer.checkLexeme(input, "", 110))
    # def test_case_10(self):
    #     input = ""
    #     self.assertTrue(TestLexer.checkLexeme(input, "", 110))
    # def test_case_10(self):
    #     input = ""
    #     self.assertTrue(TestLexer.checkLexeme(input, "", 110))
    # def test_case_10(self):
    #     input = ""
    #     self.assertTrue(TestLexer.checkLexeme(input, "", 110))
    # def test_case_10(self):
    #     input = ""
    #     self.assertTrue(TestLexer.checkLexeme(input, "", 110))
    # def test_case_10(self):
    #     input = ""
    #     self.assertTrue(TestLexer.checkLexeme(input, "", 110))
    # def test_case_10(self):
    #     input = ""
    #     self.assertTrue(TestLexer.checkLexeme(input, "", 110))
    # def test_case_10(self):
    #     input = ""
    #     self.assertTrue(TestLexer.checkLexeme(input, "", 110))
    # def test_case_10(self):
    #     input = ""
    #     self.assertTrue(TestLexer.checkLexeme(input, "", 110))
    # def test_case_10(self):
    #     input = ""
    #     self.assertTrue(TestLexer.checkLexeme(input, "", 110))
    # def test_case_10(self):
    #     input = ""
    #     self.assertTrue(TestLexer.checkLexeme(input, "", 110))