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
    # def test_case_22(self):
    #     input = """
    #     "fklasjghs'"assgf'\""""
    #     self.assertTrue(TestLexer.checkLexeme(input, """Unclosed String: fklasjghs'"assgf'\"""",22))
    # def test_case_23(self):
    #     input = "Var x:$;"
    #     self.assertTrue(TestLexer.checkLexeme(input, "Var,x,:,Error Token $", 23))
    # def test_case_24(self):
    #     input = "0_dAaf"
    #     self.assertTrue(TestLexer.checkLexeme(input, "0,Error Token _", 24))
    # def test_case_25(self):
    #     input = """
    #     Var: a = 1, b[10], s = "ajkg'", dA;"""
    #     self.assertTrue(TestLexer.checkLexeme(input, """Var,:,a,=,1,,,b,[,10,],,,s,=,Unclosed String: ajkg'", dA;""", 25))
    # def test_case_26(self):
    #     input = """
    #     Function: fact
    #     Parameter: n
    #     Body:
    #         If n == 0 Then
    #             Return 1;
    #         Else
    #             Return n * fact (n - 1);
    #         EndIf.
    #     EndBody."""
    #     self.assertTrue(TestLexer.checkLexeme(input, "Function,:,fact,Parameter,:,n,Body,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,EndBody,.,<EOF>", 26))
    # def test_case_27(self):
    #     input = """
    #     Function: foo
    #     Parameter: a[5], b
    #     Body:
    #         Var: i = 0;
    #         While (i < 5)
    #             a[i] = b +. 1.0;
    #             i += 1;
    #         EndWhile.
    #     EndBody."""
    #     self.assertTrue(TestLexer.checkLexeme(input, "Function,:,foo,Parameter,:,a,[,5,],,,b,Body,:,Var,:,i,=,0,;,While,(,i,<,5,),a,[,i,],=,b,+.,1.0,;,i,+,=,1,;,EndWhile,.,EndBody,.,<EOF>", 27))
    # def test_case_28(self):
    #     input = "Var: b[2][3]={{1,2,3},{4,5,6}};"
    #     self.assertTrue(TestLexer.checkLexeme(input, "Var,:,b,[,2,],[,3,],=,{,{,1,,,2,,,3,},,,{,4,,,5,,,6,},},;,<EOF>", 28))
    # def test_case_29(self):
    #     input = "*lkaf**"
    #     self.assertTrue(TestLexer.checkLexeme(input, "*,lkaf,Unterminated Comment", 29))
    # def test_case_30(self):
    #     input = "foo (2 + x, 4. \. y);"
    #     self.assertTrue(TestLexer.checkLexeme(input, "foo,(,2,+,x,,,4.,\.,y,),;,<EOF>", 30))
    # def test_case_31(self):
    #     input = """
    #         If (True)
    #             s = 0o248542;
    #         EndIf."""
    #     self.assertTrue(TestLexer.checkLexeme(input, "If,(,True,),s,=,0o24,8542,;,EndIf,.,<EOF>", 31))
    # def test_case_32(self):
    #     input = """
    #     If (True || False)
    #         print("aff\g\d");
    #     EndIf.
    #     """
    #     self.assertTrue(TestLexer.checkLexeme(input, "If,(,True,||,False,),print,(,Illegal Escape In String: aff\g", 32))
    # def test_case_33(self):
    #     input = "Var# x = 12;"
    #     self.assertTrue(TestLexer.checkLexeme(input, "Var,Error Token #", 33))
    # def test_case_34(self):
    #     input = "Var: x; x =/= 10;"
    #     self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,;,x,=/=,10,;,<EOF>", 34))
    # def test_case_35(self):
    #     input = """
    #     Var: x = "124\\f\\b98";
    #     Var: y = "1234"""
    #     self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,=,124\\f\\b98,;,Var,:,y,=,Unclosed String: 1234", 35))
    # def test_case_36(self):
    #     input = """
    #     Var: a = "kagfus\\a\\k\\o";"""
    #     self.assertTrue(TestLexer.checkLexeme(input, "Var,:,a,=,Illegal Escape In String: kagfus\\a", 36))
    # def test_case_37(self):
    #     input ="""**kjgsjgh*jhs\\f"""
    #     self.assertTrue(TestLexer.checkLexeme(input, """Unterminated Comment""", 37))
    # def test_case_38(self):
    #     input ="""
    #     "asd\\uf"**comm\\n\\kent**"""
    #     self.assertTrue(TestLexer.checkLexeme(input, """Illegal Escape In String: asd\\u""", 38))
    # def test_case_39(self):
    #     input ="""
    #     **comm\\n\\kent**"""
    #     self.assertTrue(TestLexer.checkLexeme(input, "<EOF>", 39))
    # def test_case_40(self):
    #     input = "0xFF0o0843"
    #     self.assertTrue(TestLexer.checkLexeme(input, "0xFF0,o0843,<EOF>", 40))
    # def test_case_41(self):
    #     input = """
    #     Var: x = 10;
    #     ** define
    #     * variable
    #     *
    #     """
    #     self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,=,10,;,Unterminated Comment", 41))
    # def test_case_42(self):
    #     input = """
    #     Var: x = 10.e2;
    #     """
    #     self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,=,10.e2,;,<EOF>", 42))
    # def test_case_43(self):
    #     input = """
    #     Var: flag = False;
    #     flag = !flag;
    #     """
    #     self.assertTrue(TestLexer.checkLexeme(input, "Var,:,flag,=,False,;,flag,=,!,flag,;,<EOF>", 43))
    # def test_case_44(self):
    #     input = """
    #     Var: x = 10.e2;
    #     """
    #     self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,=,10.e2,;,<EOF>", 44))
    # def test_case_45(self):
    #     input = """
    #     Var: x = 'asdaf';
    #     """
    #     self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,=,Error Token '", 45))
    # def test_case_46(self):
    #     input = """
    #     "\\bkkg\\fh\\tdsf\\n'"fsd'"f\\r\\\gdshg\\'"
    #     """
    #     self.assertTrue(TestLexer.checkLexeme(input, """\\bkkg\\fh\\tdsf\\n'"fsd'"f\\r\\\gdshg\\',<EOF>""", 46))
    # def test_case_47(self):
    #     input = """
    #     Var: f = -10e+;
    #     """
    #     self.assertTrue(TestLexer.checkLexeme(input, "Var,:,f,=,-,10,e,+,;,<EOF>", 47))
    # def test_case_48(self):
    #     input = """
    #     x_kaf124kah_ = (1 < 2) && (2. < 3.);
    #     """
    #     self.assertTrue(TestLexer.checkLexeme(input, "x_kaf124kah_,=,(,1,<,2,),&&,(,2.,<,3.,),;,<EOF>", 48))
    # def test_case_49(self):
    #     input = """Var: variable-@list;"""
    #     self.assertTrue(TestLexer.checkLexeme(input, "Var,:,variable,-,Error Token @", 49))
    def test_case_50(self):
        input = """
        s = "dajfsg';"""
        self.assertTrue(TestLexer.checkLexeme(input, "s,=,Unclosed String: dajfsg';", 50))
    # def test_case_42(self):
    #     input = """
    #     Var: x = 10.e2;
    #     """
    #     self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,=,10.e2,;,<EOF>", 42))
    # def test_case_42(self):
    #     input = """
    #     Var: x = 10.e2;
    #     """
    #     self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,=,10.e2,;,<EOF>", 42))
