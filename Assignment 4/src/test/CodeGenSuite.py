import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_int(self):
    #     """Simple program: int main() {} """
    #     input = """Function: main
    #                Body: 
    #                     print(string_of_int(120));
    #                EndBody."""
    #     expect = "120"
    #     self.assertTrue(TestCodeGen.test(input,expect,500))
    # def test_int_ast(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],([],[
    # 			CallStmt(Id("print"),[
    #                 CallExpr(Id("string_of_int"),[IntLiteral(120)])])]))])
    # 	expect = "120"
    # 	self.assertTrue(TestCodeGen.test(input,expect,501))
    # def test_case_03(self):
    # 	input = """
    #     Function: main
    #     Body:
    #         Var: str = "123";
    #         print(str);
    #     EndBody.
    #     """
    # 	expect = "123"
    # 	self.assertTrue(TestCodeGen.test(input,expect,502))
    # def test_case_04(self):
    # 	input = """
    #     Function: main
    #     Body:
    #         Var: str[2][3] = {{True, False, True}, {False, True, False}};
    #         If str[0][2] Then
    #             print(string_of_bool(str[0][0]));
    #         EndIf.
    #     EndBody.
    #     """
    # 	expect = "true"
    # 	self.assertTrue(TestCodeGen.test(input,expect,503))
    # def test_case_05(self):
    # 	input = """
    #     Function: main
    #     Body:
    #         Var: x = 2;
    #         x = 2 * x + foo(3);
    #         print(string_of_int(x));
    #     EndBody.
    #     Function: foo
    #     Parameter: x
    #     Body:
    #         Return x;
    #     EndBody.
    #     """
    # 	expect = "7"
    # 	self.assertTrue(TestCodeGen.test(input,expect,504))
    # def test_case_06(self):
    # 	input = """
    #     Function: main
    #     Body:
    #         Var: x = 2;
    #         If x == foo(3) Then
    #             print("A");
    #         ElseIf x > 2 Then
    #             print("B");
    #             x = foo(int_of_string("-423"));
    #         Else
    #             x = foo(int_of_string("-234"));
    #             print(string_of_float(float_to_int(x)));
    #         EndIf.
    #     EndBody.
    #     Function: foo
    #     Parameter: x
    #     Body:
    #         Return x;
    #     EndBody.
    #     """
    # 	expect = "-234.0"
    # 	self.assertTrue(TestCodeGen.test(input,expect,505))
    # def test_case_07(self):
    # 	input = """
    #     Var: x[2] = {1, 2};
    #     Function: main
    #     Body:
    #         print(string_of_int(foo()));
    #     EndBody.
    #     Function: foo
    #     Body:
    #         x[0] = 100;
    #         Return x[0];
    #     EndBody.
    #     """
    # 	expect = "100"
    # 	self.assertTrue(TestCodeGen.test(input,expect,506))
    # def test_case_08(self):
    # 	input = """
    #     Var: x[2] = {1, 2};
    #     Function: foo
    #     Body:
    #         Return x;
    #     EndBody.
    #     Function: main
    #     Body:
    #         foo()[1] = 222;
    #         print(string_of_int(foo()[1]));
    #         print(string_of_int(x[1]));
    #         print(string_of_int(x[0]));
    #     EndBody.
    #     """
    # 	expect = "2222221"
    # 	self.assertTrue(TestCodeGen.test(input,expect,507))
    # def test_case_09(self):
    # 	input = """
    #     Var: x[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    #     Function: main
    #     Body:
    #         Var: a[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    #         Var: b = 1, c = 3;
    #         a[9] = b * c;
    #         a = foo();
    #         foo()[b] = int_of_float(0.);
    #         For (b = 0, b < 10, 1) Do
    #             print(string_of_int(a[b]));
    #         EndFor.
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Return x;
    #     EndBody.
    #     """
    # 	expect = "0023456789"
    # 	self.assertTrue(TestCodeGen.test(input,expect,508))
    # def test_case_10(self):
    # 	input = """
    #     Var: x[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    #     Function: main
    #     Body:
    #         Var: a[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    #         Var: b = 1, c = 3;
    #         a[9] = b * c;
    #         Do
    #             print(string_of_int(a[b]));
    #             b = b + 1;
    #         While check(b, 10) EndDo.
    #         a = foo();
    #         b = 0 * 8;
    #         foo()[b] = int_of_float(20.5);
    #         While b < 10 Do
    #             print(string_of_int(foo()[b]));
    #             b = b + 1;
    #         EndWhile.
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Return x;
    #     EndBody.
    #     Function: check
    #     Parameter: a, b
    #     Body:
    #         Return a < b;
    #     EndBody.
    #     """
    # 	expect = "00000000320123456789"
    # 	self.assertTrue(TestCodeGen.test(input,expect,509))
    # def test_case_11(self):
    # 	input = """
    #     Var: x[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    #     Function: main
    #     Body:
    #         Var: idx = 0;
    #         foo();
    #         While idx < 10 Do
    #             print(string_of_int(x[idx]));
    #             idx = idx + 1;
    #         EndWhile.
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Var: i = 3;
    #         For (i = 3, cond(i), up()) Do
    #             x[i] = 22;
    #         EndFor.
    #     EndBody.
    #     Function: cond
    #     Parameter: x
    #     Body:
    #         Var: upper_bound = 6;
    #         Return x < upper_bound;
    #     EndBody.
    #     Function: up
    #     Body:
    #         Return 5 \ 2;
    #     EndBody.
    #     """
    # 	expect = "012224226789"
    # 	self.assertTrue(TestCodeGen.test(input,expect,510))
    # def test_case_12(self):
    # 	input = """
    #     Var: x[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    #     Function: main
    #     Body:
    #         Var: idx = 0;
    #         foo(x);
    #         While idx < 10 Do
    #             print(string_of_int(x[idx]));
    #             idx = idx + 1;
    #         EndWhile.
    #     EndBody.
    #     Function: foo
    #     Parameter: x[10]
    #     Body:
    #         Var: i = 3;
    #         For (i = 3, cond(i), up()) Do
    #             x[i] = 77;
    #         EndFor.
    #     EndBody.
    #     Function: cond
    #     Parameter: x
    #     Body:
    #         Var: upper_bound = 6;
    #         Return x < upper_bound;
    #     EndBody.
    #     Function: up
    #     Body:
    #         Return 5 \ 2;
    #     EndBody.
    #     """
    # 	expect = "012774776789"
    # 	self.assertTrue(TestCodeGen.test(input,expect,511))
    # def test_case_13(self):
    # 	input = """
    #     Var: x[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    #     Function: main
    #     Body:
    #         swap(x[0], x[1]);
    #         print(string_of_int(x[0]));
    #         print(string_of_int(x[1]));
    #     EndBody.
    #     Function: swap
    #     Parameter: x, y
    #     Body:
    #         Var: i = 3;
    #         i = x;
    #         x = y;
    #         y = i;
    #     EndBody.
        
    #     """
    # 	expect = "01"
    # 	self.assertTrue(TestCodeGen.test(input,expect,512))
    # def test_case_14(self):
    # 	input = """
    #     Var: x[4] = {True, False, False, True};
    #     Function: main
    #     Body:
    #         Var: i = 0;
    #         If x[0] && x[1] Then
    #             print("A");
    #         EndIf.
    #         Do
    #             print(string_of_bool(x[i]));
    #             i = i + 1;
    #         While i < 4 EndDo.
    #     EndBody.
    #     """
    # 	expect = "truefalsefalsetrue"
    # 	self.assertTrue(TestCodeGen.test(input,expect,513))
    # def test_case_15(self):
    # 	input = """
    #     Var: x[5] = {0.1, 1.2, 2.4, 3.5, 4.3};
    #     Function: main
    #     Body:
    #         swap(x[0], x[1]);
    #         print(string_of_float(x[0]));
    #         print(string_of_float(x[1]));
    #     EndBody.
    #     Function: swap
    #     Parameter: x, y
    #     Body:
    #         Var: i = 3.2;
    #         i = x;
    #         x = y;
    #         y = i;
    #     EndBody.
    #     """
    # 	expect = "0.11.2"
    # 	self.assertTrue(TestCodeGen.test(input,expect,514))
    # def test_case_16(self):
    # 	input = """
    #     Var: x[5] = {"A", "B", "C", "D", "E"};
    #     Function: main
    #     Body:
    #         Var: k = 4;
    #         While k >= 0 Do
    #             print(x[k]);
    #             k = k - foo();
    #         EndWhile.
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Return 1;
    #     EndBody.
    #     """
    # 	expect = "EDCBA"
    # 	self.assertTrue(TestCodeGen.test(input,expect,515))
    # def test_case_17(self):
    # 	input = """
    #     Var: x[2][1][2] = {{{"AM", "CK"}}, {{"BF", "DE"}}};
    #     Function: main
    #     Body:
    #         Var: i = 0;
    #         For (i = 0, i < 2, foo()) Do
    #             Var: k = 0;
    #             While k < 1 Do
    #                 Var: h = 0;
    #                 Do
    #                     print(x[i][foo() - 1][h]);
    #                     h = h + 1;
    #                 While h < 2 EndDo.
    #                 k = k + 1;
    #             EndWhile.
    #         EndFor.
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Return 1;
    #     EndBody.
    #     """
    # 	expect = "AMCKBFDE"
    # 	self.assertTrue(TestCodeGen.test(input,expect,516))
    # def test_case_18(self):
    # 	input = """
    #     Var: x[2][1][2] = {{{True, False}}, {{False, True}}};
    #     Function: main
    #     Body:
    #         Var: i = 0;
    #         For (i = 0, i < 2, foo()) Do
    #             Var: k = 0;
    #             While k < 1 Do
    #                 Var: h = 0;
    #                 Do
    #                     print(string_of_bool(x[i][foo() - 1][h]));
    #                     h = h + 1;
    #                 While h < 2 EndDo.
    #                 k = k + 1;
    #             EndWhile.
    #         EndFor.
    #         If x[foo()][foo() - 1][foo()] Then
    #             Var: str = "string";
    #             If x[0][0][0] Then
    #                 Var: str = 2203.2203;
    #                 printStrLn(string_of_float(str));
    #             EndIf.
    #             printStrLn(str);
    #         EndIf.
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Return 1;
    #     EndBody.
    #     """
    # 	expect = "truefalsefalsetrue2203.2202\nstring\n"
    # 	self.assertTrue(TestCodeGen.test(input,expect,517))
    # def test_case_19(self):
    # 	input = """
    #     Var: x[2][1][2] = {{{2.2, 4.3}}, {{1.2, 3.4}}};
    #     Function: main
    #     Body:
    #         Var: i = 0;
    #         For (i = 0, i < 2, foo()) Do
    #             Var: k = 0;
    #             While k < 1 Do
    #                 Var: h = 0;
    #                 Do
    #                     print(string_of_float(x[i][foo() - 1][h]));
    #                     h = h + 1;
    #                 While h < 2 EndDo.
    #                 k = k + 1;
    #             EndWhile.
    #         EndFor.
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Return 1;
    #     EndBody.
    #     """
    # 	expect = "2.24.31.23.4"
    # 	self.assertTrue(TestCodeGen.test(input,expect,518))
    # def test_case_19(self):
    # 	input = """
    #     Var: x[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    #     Function: main
    #     Body:
    #         print(string_of_int(foo(x, 10)));
    #     EndBody.
    #     Function: foo
    #     Parameter: x[10], length
    #     Body:
    #         If length == 0 Then
    #             Return 0;
    #         ElseIf length == 1 Then
    #             Return x[0];
    #         Else
    #             Return x[length - 1] + foo(x, length -  1);
    #         EndIf.
    #     EndBody.
    #     """
    # 	expect = "55"
    # 	self.assertTrue(TestCodeGen.test(input,expect,518))
    # def test_case_20(self):
    # 	input = """
    #     Var: x[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    #     Function: main
    #     Body:
    #         Var: length = 10;
    #         Var: idx = 0;
    #         sort(x, length);
    #         While idx < length Do
    #             print(string_of_int(x[idx]));
    #             print(" ");
    #             idx = idx + 1;
    #         EndWhile.
    #     EndBody.
    #     Function: sort
    #     Parameter: arr[10], length
    #     Body:
    #         Var: i = 0;
    #         While i < length - 1 Do
    #             Var: j = 0;
    #             j = i + 1;
    #             Do
    #                 If arr[i] < arr[j] Then
    #                     swap(arr, i, j);
    #                 EndIf.
    #                 j = j + 1;
    #             While j < length EndDo.
    #             i = i + 1;
    #         EndWhile.
    #     EndBody.
    #     Function: swap
    #     Parameter: arr[10], i, j
    #     Body:
    #         Var: temp = 0;
    #         temp = arr[i];
    #         arr[i] = arr[j];
    #         arr[j] = temp;
    #     EndBody.
    #     """
    # 	expect = "10 9 8 7 6 5 4 3 2 1 "
    # 	self.assertTrue(TestCodeGen.test(input,expect,519))
    # def test_case_21(self):
    # 	input = """
    #     Var: x[1][1][1][3][2] = {{{{{1, 2}, {4, 32}, {10, 22}}}}};
    #     Function: main
    #     Body:
    #         x[0][0][0][0][1] = 1;
    #         x[0][0][0][0][0] = x[0][0][0][1][1];
    #         print(string_of_int(x[0][0][0][0][0]));
    #         print(string_of_int(x[0][0][0][x[0][0][0][0][1]][0]));
    #         print(string_of_int(x[0][0][0][x[0][0][0][1][1] - 20 - 2 - 9][x[0][0][0][0][1]]));
    #     EndBody.
    #     """
    # 	expect = "32432"
    # 	self.assertTrue(TestCodeGen.test(input,expect,520))
    def test_case_22(self):
    	input = """
        Function: main
        Parameter: x, y
        Body:
            Var: n = 100;
            Var: num = 0;
            While num < n + 1 Do
                If isPrime(num) Then
                    print(string_of_int(num));
                    print(" ");
                EndIf.
                num = num + 1;
            EndWhile.
        EndBody.
        Function: isPrime
        Parameter: x
        Body:
            Var: i = 2;
            If x < 2 Then
                Return False;
            EndIf.
            For (i = 2, i < x, 1) Do
                If x % i == 0 Then
                    Return False;
                EndIf.
            EndFor.
            Return True;
        EndBody.
        """
    	expect = "2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 "
    	self.assertTrue(TestCodeGen.test(input,expect,521))