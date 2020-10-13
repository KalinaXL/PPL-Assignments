import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """Var: x;
    #     Function: main
    #     Body:
    #     Return 0;
    #     EndBody."""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,200))
    
    # def test_wrong_miss_close(self):
    #     """Miss variable"""
    #     input = """
    #         Var: m, n[10]; 
    #         Function: main 
           
    #             Parameter: n 
    #             Body: 
    #             x = {{{1,2}, {3,4}}, {5,6}};
    #             If n == 0 Then 
    #                 Return 1; 
    #             Else
    #                 Return n * face({1,2});
    #             EndIf.
    #             EndBody. 
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,201))
    # def test_case_3(self):
    #     input = """
    #     Var: x;
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 3 col 8: <EOF>", 202))
    # def test_case_4(self):
    #     input = """
    #     Var: x = {1,2,{2};
    #     Function: main
    #     Body:
    #     Return;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 2 col 25: ;",203))
    # def test_case_5(self):
    #     input = """
    #     Function: main
    #     Body:
    #         Var
    #         Return;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 12: Return",204))
    # def test_case_6(self):
    #     input = """
    #     Function: main
    #     Body:
    #         printLn();
    #         Var: x;
    #         Return;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 12: Var",205))
    # def test_case_6(self):
    #     input = """
    #     Function: main
    #     Body:
    #         If x == 1 Then
    #         Else
    #         Else EndIf.
    #         Return;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 6 col 12: Else",206))
    # def test_case_7(self):
    #     input = """
    #     Var: x;
    #     Function: main
    #     Body:
    #         Var: r = 10., v, i;
    #         v = (4. \. 3.) *. 3.14 *. r *. r *. r;
    #         For (i = 0, i < 10, 2) Do
    #             writeln(i);
    #         EndFor.
    #         Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "successful",206))
    # def test_case_8(self):
    #     input = """
    #     Var: x;
    #     Function: main
    #     Body:
    #        Var: m;
    #        x = m = 10;
    #        Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 6 col 17: =",207))
    # def test_case_9(self):
    #     input = """
    #     Var: x;
    #     Function: main
    #     Body:
    #        Var: m;
    #        x = m = 10;
    #        Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 6 col 17: =",207))    
    # def test_case_9(self):
    #     input = """
    #     Var: x;
    #     Function: main
    #     Body:
    #        Var: a[10];
    #        a[3 + foo(2)] = a[b[2][3]] + 3;
    #        Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "successful",208))       
    # def test_case_10(self):
    #     input = """
    #     Var: x;
    #     Function: main
    #     Body:
    #        Var: a[10];
    #        a[3 + foo(2)] = a[b[2][3]] + 3;
    #        Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "successful",209))
    # def test_case_11(self):
    #     input = """
    #     Function: main
    #     Parameter:
    #     Body:
    #         Var: i = 0;
    #         While (i < 5) Do
    #             a[0] = b +. 1.0;
    #             i = i + 1;
    #         EndWhile.
    #         Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 8: Body", 210))  
    # def test_case_12(self):
    #     input = """
    #     Var: x[3][3 * (4 + f(2) - 4)];
    #     Function: main
    #     Parameter: k
    #     Body:
    #         Var: i = 0;
    #         While (i < 5) Do
    #             a[0] = b +. 1.0;
    #             i = i + 1;
    #         EndWhile.
    #         Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 2 col 20: *", 211))  
    # def test_case_13(self):
    #     input = """
    #     Function: main
    #     Parameter: k
    #     Body:
    #         Var: i = 10, k[10][2] = {{}, {}};
    #         Do
    #             Break;
    #         While i <= 10 EndDo.
    #         Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "successful", 212)) 
    # def test_case_14(self):
    #     input = """
    #     Function: main
    #     Body:
    #         Var: s = 0;
    #         For (i = 0, i < 10, f(2)) Do
    #             s += i *. 2;
    #         EndFor.
    #         Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 6 col 18: +", 213)) 
    # def test_case_15(self):
    #     input = """
    #     Var: a, b, c = 10 + 2 * 4;
    #     Function: main
    #     Body:
    #         Var: i = 0, arr[10];
    #         c = arr[0];
    #         For (i = 1, i < 10, 1) Do
    #             If (c < arr[i]) Then
    #                 c = arr[i];
    #             EndIf.
    #         EndFor.  
    #         Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 2 col 26: +", 214))
    # def test_case_16(self):
    #     input = """
    #     Var: a, b, c = 10;
    #     Function: func
    #     Body:
    #         Return "Hello World";
    #     EndBody.
    #     Function: main
    #     Body:
    #         print(func());
    #         Return;  
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "successful", 215))
    # def test_case_17(self):
    #     input = """
    #     Var: a, b, c = 2;
    #     Function: func
    #     Body:
    #         Return "Hello World" 1967;
    #     EndBody.
    #     Function: main
    #     Body:
    #         print(func());
    #         Return;  
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 33: 1967", 216))
    # def test_case_18(self):
    #     input = """
    #     Function: main
    #     Body:
    #         Var: i;
    #         For(i = 0, i < 10, 1) Do
    #             Continue i;
    #         EndFor.  
    #         Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 6 col 25: i", 217))
    # def test_case_19(self):
    #     input = """
    #     Function: main
    #     Body:
    #         For(i = 0, i < 10, 1) Do
    #             Continue;
    #         EndFor.
    #         Var: i;  
    #         Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 7 col 12: Var", 218))
    # def test_case_20(self):
    #     input = """
    #     Function: main
    #     Parameter: n = 10
    #     Body:
    #         Var: i;
    #         For(i = 0, i < 10, 1) Do
    #             Continue;
    #         EndFor.
    #         Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 3 col 21: =", 219))
    # def test_case_21(self):
    #     input = """
    #     Function: main
    #     Parameter: n m i k u
    #     Body:
    #         Var: i;
    #         For(i = 0, i < 10, 1) Do
    #             Continue;
    #         EndFor.
    #         Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 3 col 21: m", 220))
    # def test_case_22(self):
    #     input = """
    #     Function: main
    #     Body:
    #         Var: x = {2 + 1, foo(2), fact(4)};
    #         Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 24: +", 221))
    # def test_case_23(self):
    #     input = """
    #     Function: main
    #     Body:
    #         Var: i;
    #         If i == 10 Then
    #         Else
    #             print(i);
    #         ElseIf i == 2 Then
    #             Break;
    #         EndIf.
    #         Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 8 col 12: ElseIf", 222))
    # def test_case_24(self):
    #     input = """
    #     Function: main
    #     Body:
    #         Var: i;
    #         If i == 10 Then
    #         Else
    #             print(i);
    #         ElseIf i == 2 Then
    #             Break;
    #         EndIf.
    #         Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 8 col 12: ElseIf", 223))
    # def test_case_25(self):
    #     input = """
    #     Function: main
    #     Body:
    #         Var: x = 0., y = 2.;
    #         While (x =/= y) Do
    #             x = x +. 1;
    #             y = y -. 1;
    #         EndWhile.
    #         Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "successful", 224))
    # def test_case_26(self):
    #     input = """
    #     Function: main
    #     Body:
    #         Var: i = 0;
    #         For (i, i < 10, 2) Do
    #             writeln(i);
    #         EndFor.
    #         Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 18: ,", 225))
    # def test_case_27(self):
    #     input = """
    #     Function: main
    #     Body:
    #         Var: i[10] = {0};
    #         For (i[0] = 12, i < 10, 2) Do
    #             writeln(i);
    #         EndFor.
    #         Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 18: [", 226))
    # def test_case_28(self):
    #     input = """
    #     Function: main
    #     Body:
    #         Var: i[10] = {0};
    #         Var: j;
    #         For(j = 0, j < 10, 2) Do
    #             Break j;
    #         EndFor.
    #         Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 7 col 22: j", 227))
    # def test_case_29(self):
    #     input = """
    #     Function: find_max
    #     Parameter: a[10]
    #     Body:
    #         Return a[random(0, 10, False)];   
    #     EndBody.
    #     Function: main
    #     Body:
    #         print(find_max({1,2,3,4,5,6,7,8,9,10}));
    #         Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "successful", 228))
    # def test_case_30(self):
    #     input = """
    #     Function: main
    #     Body:
    #         Var: x[10];
    #         x[0] = fact(f(0))[0][4][123];
    #         Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "successful", 229))
    # def test_case_31(self):
    #     input = """
    #     Function: main
    #     Body:
    #         Var: x[10];
    #         x[0, 1] = fact(f(0))[0][4][123];
    #         Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 15: ,", 230))
    # def test_case_32(self):
    #     input = """
    #     Function: main
    #     Body:
    #         Var: x[10, 15];
    #         Var: count = 0;
    #         While True Do
    #             count = count + 1;
    #             print(count);
    #         EndWhile.
    #         Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 21: ,", 231))
    # def test_case_33(self):
    #     input = """
    #     Function: main
    #     Body:
    #         Var: x[[10]][10]];
    #         goo(2. +. 4., 2 *. 10);
    #         Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 19: [", 232))
    # def test_case_34(self):
    #     input = """
    #     Function: main
    #     Body:
    #         Var: x[[10]][10]];
    #         goo(2. +. 4., 2 *. 10);
    #         Return 0;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 19: [", 233))
    # def test_case_35(self):
    #     input = """
    #     Function: main
    #     Body:
    #         Var: x = 10;
    #         goo(2. +. 4., 2 *. 10)
    #         x = 1;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 6 col 12: x", 234))
    # def test_case_36(self):
    #     input = """
    #     Function: main
    #     Body:
    #         Var: x = 10;
    #         goo(2. +. 4., 2 *. 10);
    #         x = 1;
    #     EndBody.
    #     Var: x;
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 8 col 8: Var", 235))
    # def test_case_37(self):
    #     input = ""
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 1 col 0: <EOF>", 236))
    # def test_case_38(self):
    #     input = """
    #     Function: main
    #     Body:
    #         x = 5[10] + 4;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 17: [", 237))
    # def test_case_38(self):
    #     input = """
    #     Function: main
    #     Body:
    #         x = 5[10] + 4;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 17: [", 237))
    # def test_case_39(self):
    #     input = """
    #     Function: main
    #     Body:
    #         x = (5 + f() * 3 + a[10])[2] * 5 \\ 8;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 37: [", 238))
    # def test_case_40(self):
    #     input = """
    #     Function: main
    #     Body:
    #         x = (x)[2] * 5 \\ 8;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "successful", 239))
    # def test_case_41(self):
    #     input = """
    #     Function: main
    #     Body:
    #         x = 9 == 20 == 6;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 24: ==", 240))
    # def test_case_42(self):
    #     input = """
    #     Function: main
    #     Body:
    #         x = 9 == 20 == 6;
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 24: ==", 241))
    # def test_case_43(self):
    #     input = """
    #     Function: main
    #     Body:
    #         x = "1" + "1";
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 20: +", 242))
    # def test_case_44(self):
    #     input = """
    #     Function: main
    #     Body:
    #        x =  f("1", "194") + a[0][3] * "blu bla";
    #     EndBody.
    #     """
    #     self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 42: blu bla", 243))
    def test_case_45(self):
        input = """
        Function: main
        Body:
           x =  f("", "194") + a[0][3] * "blu bla";
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 41: blu bla", 244))



    
    