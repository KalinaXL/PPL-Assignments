import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        print(string_of_int(120));
                   EndBody."""
        expect = "120"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_int_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],([],[
    			CallStmt(Id("print"),[
                    CallExpr(Id("string_of_int"),[IntLiteral(120)])])]))])
    	expect = "120"
    	self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_case_03(self):
    	input = """
        Function: main
        Body:
            Var: str = "123";
            print(str);
        EndBody.
        """
    	expect = "123"
    	self.assertTrue(TestCodeGen.test(input,expect,502))
    def test_case_04(self):
    	input = """
        Function: main
        Body:
            Var: str[2][3] = {{True, False, True}, {False, True, False}};
            If str[0][2] Then
                print(string_of_bool(str[0][0]));
            EndIf.
        EndBody.
        """
    	expect = "true"
    	self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_case_05(self):
    	input = """
        Function: main
        Body:
            Var: x = 2;
            x = 2 * x + foo(3);
            print(string_of_int(x));
        EndBody.
        Function: foo
        Parameter: x
        Body:
            Return x;
        EndBody.
        """
    	expect = "7"
    	self.assertTrue(TestCodeGen.test(input,expect,504))
    def test_case_06(self):
    	input = """
        Function: main
        Body:
            Var: x = 2;
            If x == foo(3) Then
                print("A");
            ElseIf x > 2 Then
                print("B");
                x = foo(int_of_string("-423"));
            Else
                x = foo(int_of_string("-234"));
                print(string_of_float(float_to_int(x)));
            EndIf.
        EndBody.
        Function: foo
        Parameter: x
        Body:
            Return x;
        EndBody.
        """
    	expect = "-234.0"
    	self.assertTrue(TestCodeGen.test(input,expect,505))
    def test_case_07(self):
    	input = """
        Var: x[2] = {1, 2};
        Function: main
        Body:
            print(string_of_int(foo()));
        EndBody.
        Function: foo
        Body:
            x[0] = 100;
            Return x[0];
        EndBody.
        """
    	expect = "100"
    	self.assertTrue(TestCodeGen.test(input,expect,506))
    def test_case_08(self):
    	input = """
        Var: x[2] = {1, 2};
        Function: foo
        Body:
            Return x;
        EndBody.
        Function: main
        Body:
            foo()[1] = 222;
            print(string_of_int(foo()[1]));
            print(string_of_int(x[1]));
            print(string_of_int(x[0]));
        EndBody.
        """
    	expect = "2222221"
    	self.assertTrue(TestCodeGen.test(input,expect,507))
    def test_case_09(self):
    	input = """
        Var: x[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        Function: main
        Body:
            Var: a[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
            Var: b = 1, c = 3;
            a[9] = b * c;
            a = foo();
            foo()[b] = int_of_float(0.);
            For (b = 0, b < 10, 1) Do
                print(string_of_int(a[b]));
            EndFor.
        EndBody.
        Function: foo
        Body:
            Return x;
        EndBody.
        """
    	expect = "0023456789"
    	self.assertTrue(TestCodeGen.test(input,expect,508))
    def test_case_10(self):
    	input = """
        Var: x[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        Function: main
        Body:
            Var: a[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
            Var: b = 1, c = 3;
            a[9] = b * c;
            Do
                print(string_of_int(a[b]));
                b = b + 1;
            While check(b, 10) EndDo.
            a = foo();
            b = 0 * 8;
            foo()[b] = int_of_float(20.5);
            While b < 10 Do
                print(string_of_int(foo()[b]));
                b = b + 1;
            EndWhile.
        EndBody.
        Function: foo
        Body:
            Return x;
        EndBody.
        Function: check
        Parameter: a, b
        Body:
            Return a < b;
        EndBody.
        """
    	expect = "00000000320123456789"
    	self.assertTrue(TestCodeGen.test(input,expect,509))
    def test_case_11(self):
    	input = """
        Var: x[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        Function: main
        Body:
            Var: idx = 0;
            foo();
            While idx < 10 Do
                print(string_of_int(x[idx]));
                idx = idx + 1;
            EndWhile.
        EndBody.
        Function: foo
        Body:
            Var: i = 3;
            For (i = 3, cond(i), up()) Do
                x[i] = 22;
            EndFor.
        EndBody.
        Function: cond
        Parameter: x
        Body:
            Var: upper_bound = 6;
            Return x < upper_bound;
        EndBody.
        Function: up
        Body:
            Return 5 \ 2;
        EndBody.
        """
    	expect = "012224226789"
    	self.assertTrue(TestCodeGen.test(input,expect,510))
    def test_case_12(self):
    	input = """
        Var: x[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        Function: main
        Body:
            Var: idx = 0;
            foo(x);
            While idx < 10 Do
                print(string_of_int(x[idx]));
                idx = idx + 1;
            EndWhile.
        EndBody.
        Function: foo
        Parameter: x[10]
        Body:
            Var: i = 3;
            For (i = 3, cond(i), up()) Do
                x[i] = 77;
            EndFor.
        EndBody.
        Function: cond
        Parameter: x
        Body:
            Var: upper_bound = 6;
            Return x < upper_bound;
        EndBody.
        Function: up
        Body:
            Return 5 \ 2;
        EndBody.
        """
    	expect = "012774776789"
    	self.assertTrue(TestCodeGen.test(input,expect,511))
    def test_case_13(self):
    	input = """
        Var: x[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        Function: main
        Body:
            swap(x[0], x[1]);
            print(string_of_int(x[0]));
            print(string_of_int(x[1]));
        EndBody.
        Function: swap
        Parameter: x, y
        Body:
            Var: i = 3;
            i = x;
            x = y;
            y = i;
        EndBody.
        
        """
    	expect = "01"
    	self.assertTrue(TestCodeGen.test(input,expect,512))
    def test_case_14(self):
    	input = """
        Var: x[4] = {True, False, False, True};
        Function: main
        Body:
            Var: i = 0;
            If x[0] && x[1] Then
                print("A");
            EndIf.
            Do
                print(string_of_bool(x[i]));
                i = i + 1;
            While i < 4 EndDo.
        EndBody.
        """
    	expect = "truefalsefalsetrue"
    	self.assertTrue(TestCodeGen.test(input,expect,513))
    def test_case_15(self):
    	input = """
        Var: x[5] = {0.1, 1.2, 2.4, 3.5, 4.3};
        Function: main
        Body:
            swap(x[0], x[1]);
            print(string_of_float(x[0]));
            print(string_of_float(x[1]));
        EndBody.
        Function: swap
        Parameter: x, y
        Body:
            Var: i = 3.2;
            i = x;
            x = y;
            y = i;
        EndBody.
        """
    	expect = "0.11.2"
    	self.assertTrue(TestCodeGen.test(input,expect,514))
    def test_case_16(self):
    	input = """
        Var: x[5] = {"A", "B", "C", "D", "E"};
        Function: main
        Body:
            Var: k = 4;
            While k >= 0 Do
                print(x[k]);
                k = k - foo();
            EndWhile.
        EndBody.
        Function: foo
        Body:
            Return 1;
        EndBody.
        """
    	expect = "EDCBA"
    	self.assertTrue(TestCodeGen.test(input,expect,515))
    def test_case_17(self):
    	input = """
        Var: x[2][1][2] = {{{"AM", "CK"}}, {{"BF", "DE"}}};
        Function: main
        Body:
            Var: i = 0;
            For (i = 0, i < 2, foo()) Do
                Var: k = 0;
                While k < 1 Do
                    Var: h = 0;
                    Do
                        print(x[i][foo() - 1][h]);
                        h = h + 1;
                    While h < 2 EndDo.
                    k = k + 1;
                EndWhile.
            EndFor.
        EndBody.
        Function: foo
        Body:
            Return 1;
        EndBody.
        """
    	expect = "AMCKBFDE"
    	self.assertTrue(TestCodeGen.test(input,expect,516))
    def test_case_18(self):
    	input = """
        Var: x[2][1][2] = {{{True, False}}, {{False, True}}};
        Function: main
        Body:
            Var: i = 0;
            For (i = 0, i < 2, foo()) Do
                Var: k = 0;
                While k < 1 Do
                    Var: h = 0;
                    Do
                        print(string_of_bool(x[i][foo() - 1][h]));
                        h = h + 1;
                    While h < 2 EndDo.
                    k = k + 1;
                EndWhile.
            EndFor.
            If x[foo()][foo() - 1][foo()] Then
                Var: str = "string";
                If x[0][0][0] Then
                    Var: str = 2203.2203;
                    printStrLn(string_of_float(str));
                EndIf.
                printStrLn(str);
            EndIf.
        EndBody.
        Function: foo
        Body:
            Return 1;
        EndBody.
        """
    	expect = "truefalsefalsetrue2203.2202\nstring\n"
    	self.assertTrue(TestCodeGen.test(input,expect,517))
    def test_case_19(self):
    	input = """
        Var: x[2][1][2] = {{{2.2, 4.3}}, {{1.2, 3.4}}};
        Function: main
        Body:
            Var: i = 0;
            For (i = 0, i < 2, foo()) Do
                Var: k = 0;
                While k < 1 Do
                    Var: h = 0;
                    Do
                        print(string_of_float(x[i][foo() - 1][h]));
                        h = h + 1;
                    While h < 2 EndDo.
                    k = k + 1;
                EndWhile.
            EndFor.
        EndBody.
        Function: foo
        Body:
            Return 1;
        EndBody.
        """
    	expect = "2.24.31.23.4"
    	self.assertTrue(TestCodeGen.test(input,expect,518))
    def test_case_19(self):
    	input = """
        Var: x[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        Function: main
        Body:
            print(string_of_int(foo(x, 10)));
        EndBody.
        Function: foo
        Parameter: x[10], length
        Body:
            If length == 0 Then
                Return 0;
            ElseIf length == 1 Then
                Return x[0];
            Else
                Return x[length - 1] + foo(x, length -  1);
            EndIf.
        EndBody.
        """
    	expect = "55"
    	self.assertTrue(TestCodeGen.test(input,expect,518))
    def test_case_20(self):
    	input = """
        Var: x[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        Function: main
        Body:
            Var: length = 10;
            Var: idx = 0;
            sort(x, length);
            While idx < length Do
                print(string_of_int(x[idx]));
                print(" ");
                idx = idx + 1;
            EndWhile.
        EndBody.
        Function: sort
        Parameter: arr[10], length
        Body:
            Var: i = 0;
            While i < length - 1 Do
                Var: j = 0;
                j = i + 1;
                Do
                    If arr[i] < arr[j] Then
                        swap(arr, i, j);
                    EndIf.
                    j = j + 1;
                While j < length EndDo.
                i = i + 1;
            EndWhile.
        EndBody.
        Function: swap
        Parameter: arr[10], i, j
        Body:
            Var: temp = 0;
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        EndBody.
        """
    	expect = "10 9 8 7 6 5 4 3 2 1 "
    	self.assertTrue(TestCodeGen.test(input,expect,519))
    def test_case_21(self):
    	input = """
        Var: x[1][1][1][3][2] = {{{{{1, 2}, {4, 32}, {10, 22}}}}};
        Function: main
        Body:
            x[0][0][0][0][1] = 1;
            x[0][0][0][0][0] = x[0][0][0][1][1];
            print(string_of_int(x[0][0][0][0][0]));
            print(string_of_int(x[0][0][0][x[0][0][0][0][1]][0]));
            print(string_of_int(x[0][0][0][x[0][0][0][1][1] - 20 - 2 - 9][x[0][0][0][0][1]]));
        EndBody.
        """
    	expect = "32432"
    	self.assertTrue(TestCodeGen.test(input,expect,520))
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
    def test_case_23(self):
    	input = """
        Function: main
        Body:
            Var: x = 10;
            Var: u = 1, y = 3, z = 3;
            test();
        EndBody.
        Function: test
        Body:
            If True Then
                Var: x[5] = {1, 2, 3, 4, 5};
                Var: i = 0;
                While i < 5 Do
                    Var: y[5] = {1.2, 3.4, 4.2, 4.9, 2.4};
                    If x[i] == int_of_float(y[i]) Then
                        printStrLn(string_of_float(y[i]));
                    Else
                        Var: y = "hello";
                        print(y);
                        print(" ");
                        printStrLn(string_of_int(x[i]));
                    EndIf.
                    i = i + 1;
                EndWhile.
            EndIf.
        EndBody.
        """
    	expect = "1.2\nhello 2\nhello 3\n4.9\nhello 5\n"
    	self.assertTrue(TestCodeGen.test(input,expect,522))
    def test_case_24(self):
    	input = """
        Function: main
        Body:
            Var: x = 10;
            Var: u = 1, y = 3, z = 3;
            test();
        EndBody.
        Function: test
        Body:
            Var: i = 0;
            For (i = 0, i < 10, 1) Do
                Var: s[9] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
                print(string_of_int(i));
                print(string_of_int(int_of_float(sum(s))));
                print(" ");
                i = i + 2;
            EndFor.
        EndBody.
        Function: sum
        Parameter: x[9]
        Body:
            Var: sum = 0.0;
            Var: i = 0;
            Do
                sum = sum +. float_to_int(x[i]);
                i = i + 1;
            While i < 9 EndDo.
            Return sum;
        EndBody.
        """
    	expect = "045 345 645 945 "
    	self.assertTrue(TestCodeGen.test(input,expect,523))
    def test_case_25(self):
    	input = """
        Var: arr[4] = {1, 2, 3, 4}, i = 2;
        Function: foo
        Parameter: flag
        Body:
            Var: k[4] = {11, 22, 33, 44};
            i = -2;
            While flag > 0 Do
                Return arr;            
            EndWhile.
            Return k;
        EndBody.
        Function: main
        Body:
            Var: j = 3;
            foo(0)[foo(1)[1]] = i;
            printStrLn(string_of_int(i));
            While j > -1 Do
                print(string_of_int(arr[j]));
                print(string_of_int(foo(0)[foo(1)[1]]));
                j = j - 1;
            EndWhile.
        EndBody.
        """
    	expect = "-2\n433333233133"
    	self.assertTrue(TestCodeGen.test(input,expect,524))
    def test_case_26(self):
    	input = """
        Var: arr[4] = {1, 2, 3, 4}, i = 2;
        
        Function: main
        Body:
            Var: k = 5.0;
            Var: m = 2.0;
            print(string_of_float(k \. m));
        EndBody.
        """
    	expect = "2.5"
    	self.assertTrue(TestCodeGen.test(input,expect,525))
    def test_case_27(self):
    	input = """
        Var: arr[10] = {1,2,3,4,5,6,7,8,9,10};
        Function: main
        Body:
            Var: min = 1;
            Var: max = 1;
            Var: i = 1;
            min = arr[0];
            max = arr[0];
            While i < 10 Do
                If min > arr[i] Then
                    min = arr[i];
                EndIf.
                If max < arr[i] Then
                    If i == 9 Then
                        If max > min Then
                            print("aaassd");
                        EndIf.
                    EndIf.
                    max = arr[i];
                EndIf.
                i = i + 1;
            EndWhile.
            print(string_of_int(min));
            print(string_of_int(max));
        EndBody.
        """
    	expect = "aaassd110"
    	self.assertTrue(TestCodeGen.test(input,expect,526))
    def test_case_28(self):
    	input = """
        Var: arr[10] = {1,2,3,4,5,6,7,8,9,10};
        Function: main
        Body:
            Var: i = 1;
            For(i = 1, i < 20, 1) Do
                If pnum(i) Then
                    print(string_of_int(i));
                    print(" ");
                EndIf.
            EndFor.
        EndBody.
        Function: pnum
        Parameter: x
        Body:
            Var: i = 1;
            Var: sum = 0;
            For(i = 1, i <= x - 1, 1) Do
                Var: k = 0;
                If is_divide(x, i) Then
                    k = i;
                EndIf.
                sum = sum + k;
            EndFor.
            Return sum == x;
        EndBody.
        Function: is_divide
        Parameter: a, b
        Body:
            If a % b == 0 Then
                Return True;
            Else
                Return False;
            EndIf.
        EndBody.
        """
    	expect = "6 "
    	self.assertTrue(TestCodeGen.test(input,expect,527))
    def test_case_29(self):
    	input = """
        Function: main
        Body:
            Var: i = 0;
            Do
                Var: flag = False;
                Var: j = 0;
                While j < i \ 2 + 1 Do
                    flag = flag || foo(j, i);
                    If flag Then
                        Break;
                    EndIf.
                    j = j + 1;
                EndWhile.
                If flag Then
                    print(string_of_int(i));
                EndIf.
                i = i + 1;
            While i < 20 EndDo.
        EndBody.
        Function: foo
        Parameter: number, n
        Body:
            Var: iter = 0;
            Var: upper = 0, sum = 0e1;
            upper = 2 * number - 1;
            For (iter = 1, iter <= int_of_float(float_to_int(upper)), int_of_float(1.24)) Do 
                sum = sum +. float_to_int(iter);
                iter = iter + 1;
            EndFor.
            Return  !(sum =/= float_to_int(n));
        EndBody.
        """
    	expect = "04916"
    	self.assertTrue(TestCodeGen.test(input,expect,528))
    def test_case_30(self):
    	input = """
        Function: main
        Body:
            printStrLn(string_of_bool(-. 1.0 =/= 1.0));
            printStrLn(string_of_bool(1.0 =/= 1.0));
            printStrLn(string_of_bool(-. 2.0 <=. -. 2.0));
            printStrLn(string_of_bool(2.0 <=. 1.0));
            printStrLn(string_of_bool(1.0 >=. -. 1.0));
            printStrLn(string_of_bool(1.0 >=. 1.0));
            printStrLn(string_of_bool(-. 1.0 >. 1.0));
            printStrLn(string_of_bool(1.0 >. 1.0));
            printStrLn(string_of_bool(1.0 <. 1.0));
            printStrLn(string_of_bool(1.0 <. -. 1.0));
            printStrLn(string_of_bool(1.0 <. 2.0));
            printStrLn(string_of_bool(1.0 >=. 2.0));
        EndBody.
        """
    	expect = "true\nfalse\ntrue\nfalse\ntrue\ntrue\nfalse\nfalse\nfalse\nfalse\ntrue\nfalse\n"
    	self.assertTrue(TestCodeGen.test(input,expect,529))
    def test_case_31(self):
    	input = """
        Function: partition
        Parameter: arr[7], low, high
        Body:
            Var: i = 0, pivot = 0;
            Var: j = 0, temp = 0;
            i = low - 1;
            pivot = arr[high];
            For (j = low, j < high, 1) Do
                If arr[j] < pivot Then
                    Var: temp = 0;
                    i = i + 1;
                    temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                EndIf.
            EndFor.
            temp = arr[i + 1];
            arr[i + 1] = pivot;
            arr[high] = temp;
            Return i + 1;
        EndBody.
        Function: quick_sort
        Parameter: x[7], low, high
        Body:
            Var: idx = 0;
            If low >= high Then
                Return;
            EndIf.
            idx = partition(x, low, high);
            print(string_of_int(low));
            print(" ");
            print(string_of_int(high));
            print(" ");
            printStrLn(string_of_int(idx));
            quick_sort(x, low, idx - 1);
            quick_sort(x, idx + 1, high);
        EndBody.
        Function: main
        Body:
          Var: x[7] = {10, 80, 30, 90, 40, 50, 70};
          quick_sort(x, 0, 6);
        EndBody.
        """
    	expect = "0 6 4\n0 3 3\n0 2 2\n0 1 1\n5 6 5\n"
    	self.assertTrue(TestCodeGen.test(input,expect,530))
    def test_case_32(self):
    	input = """
        Function: partition
        Parameter: arr[7], low, high
        Body:
            Var: i = 0, pivot = 0;
            Var: j = 0, temp = 0;
            i = low;
            pivot = arr[high];
            For (j = low, j < high, 1) Do
                If arr[j] < pivot Then
                   If arr[i] != arr[j] Then
                        Var: temp = 0;
                        temp = arr[j];
                        arr[j] = arr[i];
                        arr[i] = temp;
                    EndIf.
                    i = i + 1;
                EndIf.
            EndFor.
            temp = arr[i];
            arr[i] = arr[high];
            arr[high] = temp;
            Return i;
        EndBody.
        Function: quick_sort
        Parameter: x[7], low, high
        Body:
            Var: idx = 0;
            If low >= high Then
                Return;
            EndIf.
            idx = partition(x, low, high);
            quick_sort(x, low, idx - 1);
            quick_sort(x, idx + 1, high);

        EndBody.
        Function: main
        Body:
          Var: x[7] = {10, 80, 30, 90, 40, 50, 70};
          Var: i = 0;
          quick_sort(x, 0, 6);
          While i < 7 Do
            print(string_of_int(x[i]));
            i = i + 1;
          EndWhile.
        EndBody.
        """
    	expect = "10304050708090"
    	self.assertTrue(TestCodeGen.test(input,expect,531))
    def test_case_33(self):
    	input = """
        Function: foo
        Parameter: arr[7], x, y
        Body:
            arr[x] = arr[y] + 1;
            x = y;
        EndBody.
        Function: main
        Body:
          Var: x[7] = {10, 80, 30, 90, 40, 50, 70};
          Var: a = 0, b = 4;
          foo(x, a, b);
          print(string_of_int(a));
          print(string_of_int(x[a]));
        EndBody.
        """
    	expect = "041"
    	self.assertTrue(TestCodeGen.test(input,expect,532))
    def test_case_34(self):
    	input = """
        Function: main
        Body:
          Var: x[7] = {10, 80, 30, 90, 40, 50, 70};
          Var: a = 8, b = 4;
          If (a < 7) && (x[a] == 10) Then
          EndIf.
        EndBody.
        """
    	expect = ""
    	self.assertTrue(TestCodeGen.test(input,expect,533))
    def test_case_35(self):
    	input = """
        Function: main
        Body:
          Var: x[7] = {10, 80, 30, 90, 40, 50, 70};
          Var: a = 8, b = 4;
          If (a == 8) || (x[a] == 10) Then
          EndIf.
        EndBody.
        """
    	expect = ""
    	self.assertTrue(TestCodeGen.test(input,expect,534))
    def test_case_36(self):
    	input = """
        Function: max
        Parameter: x, y
        Body:
            If x < y Then
                Return y;
            EndIf.
            Return x;
        EndBody.
        Function: main
        Body:
            print(string_of_int(max(20, 72)));
        EndBody.
        """
    	expect = "72"
    	self.assertTrue(TestCodeGen.test(input,expect,535))
    def test_case_37(self):
    	input = """
        Function: max
        Parameter: x
        Body:
            print(x);
        EndBody.
        Function: main
        Body:
            max("Hello BKIT");
        EndBody.
        """
    	expect = "Hello BKIT"
    	self.assertTrue(TestCodeGen.test(input,expect,536))
    def test_case_38(self):
    	input = """
        Var: arr[8] = {1, 2, 3, 4, 5, 6, 7, 8};
        Function: identity
        Parameter: x
        Body:
            Return x + 1;
        EndBody.
        Function: main
        Body:
            print(string_of_int(arr[arr[arr[arr[identity(arr[identity(0)])]]]]));
        EndBody.
        """
    	expect = "7"
    	self.assertTrue(TestCodeGen.test(input,expect,537))
    def test_case_39(self):
    	input = """
        Function: fibonaci
        Parameter: n
        Body:
            If (n == 0) || (n == 1) Then
                Return n;
            EndIf.
            Return fibonaci(n - 1) + fibonaci(n - 2);
        EndBody.
        Function: main
        Body:
            print(string_of_int(fibonaci(22)));
        EndBody.
        """
    	expect = "17711"
    	self.assertTrue(TestCodeGen.test(input,expect,538))
    def test_case_40(self):
        input = """
        Function: fibonaci
        Parameter: n
        Body:
            Var: x[21] = {0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
            Var: i = 2;
            While i <= n Do
                x[i] = x[i - 1] + x[i - 2];
                i = i + 1;
            EndWhile.
            print(string_of_int(x[n]));
        EndBody.
        Function: main
        Body:
            fibonaci(20);
        EndBody.
        """
        expect = "6765"
        self.assertTrue(TestCodeGen.test(input,expect,539))
    def test_case_41(self):
    	input = """
        Function: fibonaci
        Parameter: n
        Body:
            Var: i = 2;
            Var: f = 0, g = 1;
            For (i = 2, i < n + 1, 1) Do
                g = f + g;
                f = g - f;
            EndFor.
            print(string_of_int(g));
        EndBody.
        Function: main
        Body:
            fibonaci(30);
        EndBody.
        """
    	expect = "832040"
    	self.assertTrue(TestCodeGen.test(input,expect,540))
    def test_case_42(self):
    	input = """
        Function: divisors
        Parameter: n
        Body:
            Var: i = 244;
            For (i = 1, i < n + 1, 1) Do
                If n % i == 0 Then
                    print(string_of_float(float_to_int(i)));
                EndIf.
            EndFor.
        EndBody.
        Function: main
        Body:
            divisors(30);
        EndBody.
        """
    	expect = "1.02.03.05.06.010.015.030.0"
    	self.assertTrue(TestCodeGen.test(input,expect,541))
    def test_case_43(self):
        input = """Function: main
                   Body: 
                        print(string_of_int(120));
                        print(string_of_float(-.12.527e-2));
                        print(string_of_bool(True));
                        print(string_of_bool(False));
                   EndBody."""
        expect = "120-0.12527truefalse"
        self.assertTrue(TestCodeGen.test(input,expect,542))
    def test_case_44(self):
    	input = """
        Function: main
        Body:
            Var: str = 210.32e2;
            str = -.str;
            print(string_of_float(str));
        EndBody.
        """
    	expect = "-21032.0"
    	self.assertTrue(TestCodeGen.test(input,expect,543))
    def test_case_45(self):
    	input = """
        Function: main
        Body:
            Var: str[2][3] = {{True, False, True}, {False, True, False}};
            Var: flag = True;
            Var: i = 0, j = 0;
            For(i = 0, i < 2, 1) Do
                For (j = 0, j < 3, 1) Do
                    flag = flag && str[i][j];
                EndFor.
            EndFor.
            If flag Then
                print(string_of_int(i));
                print(string_of_int(j));
            Else
                print(string_of_int(j));
                print(string_of_int(i));
            EndIf.
        EndBody.
        """
    	expect = "32"
    	self.assertTrue(TestCodeGen.test(input,expect,544))
    def test_case_46(self):
    	input = """
        Function: main
        Body:
            Var: x = 2;
            Var: y = 0.0;
            y = -.2.0 *. float_to_int(x) +. foo(float_to_int(3));
            print(string_of_float(y));
        EndBody.
        Function: foo
        Parameter: x
        Body:
            Return x;
        EndBody.
        """
    	expect = "-1.0"
    	self.assertTrue(TestCodeGen.test(input,expect,545))
    def test_case_47(self):
    	input = """
        Function: main
        Body:
            Var: x = 3;
            If x == foo(3) Then
                print("A");
            ElseIf x > 2 Then
                print("B");
                x = foo(int_of_string("-423"));
            Else
                x = foo(int_of_string("-234"));
                print(string_of_float(float_to_int(x)));
            EndIf.
        EndBody.
        Function: foo
        Parameter: x
        Body:
            Return x;
        EndBody.
        """
    	expect = "A"
    	self.assertTrue(TestCodeGen.test(input,expect,546))
    def test_case_48(self):
    	input = """
        Function: main
        Body:
            Var: x = 4;
            If x == foo(3) Then
                print("A");
            ElseIf x > 2 Then
                print("B");
                x = foo(int_of_string("-423"));
            Else
                x = foo(int_of_string("-234"));
                print(string_of_float(float_to_int(x)));
            EndIf.
        EndBody.
        Function: foo
        Parameter: x
        Body:
            Return x;
        EndBody.
        """
    	expect = "B"
    	self.assertTrue(TestCodeGen.test(input,expect,547))
    def test_case_49(self):
    	input = """
        Function: main
        Body:
            Var: x = 6;
            If x < 2 Then
                print("A");
            ElseIf x < 4 Then
                print("B");
            ElseIf x < 6 Then
                print("C");
            EndIf.
            print("XL");
        EndBody.
        """
    	expect = "XL"
    	self.assertTrue(TestCodeGen.test(input,expect,548))
    def test_case_50(self):
    	input = """
        Function: main
        Body:
            Var: x = 5;
            If x < 2 Then
                print("A");
            ElseIf x < 4 Then
                print("B");
            ElseIf x < 6 Then
                print("C");
            EndIf.
            print("XL");
        EndBody.
        """
    	expect = "CXL"
    	self.assertTrue(TestCodeGen.test(input,expect,549))
    def test_case_51(self):
    	input = """
        Function: main
        Body:
            Var: x = 7;
            If x < 2 Then
                print("A");
            ElseIf x < 4 Then
                print("B");
            ElseIf x < 6 Then
                print("C");
            ElseIf x < 8 Then
                print("D");
            EndIf.
            print("XL");
        EndBody.
        """
    	expect = "DXL"
    	self.assertTrue(TestCodeGen.test(input,expect,550))
    def test_case_52(self):
    	input = """
        Var: x[2] = {1.2, 2.0};
        Function: main
        Body:
            print(string_of_float(foo()));
        EndBody.
        Function: foo
        Body:
            x[0] = -.100.222;
            Return x[0];
        EndBody.
        """
    	expect = "-100.222"
    	self.assertTrue(TestCodeGen.test(input,expect,551))
    def test_case_53(self):
    	input = """
        Var: x[2] = {1.1, 2.2};
        Function: foo
        Body:
            Return x;
        EndBody.
        Function: main
        Body:
            foo()[0] = 202.22;
            print(string_of_float(foo()[0]));
            print(string_of_float(x[1]));
            print(string_of_float(x[0]));
        EndBody.
        """
    	expect = "202.222.2202.22"
    	self.assertTrue(TestCodeGen.test(input,expect,552))
    def test_case_54(self):
    	input = """
        Function: main
        Body:
            Var: a[10] = {0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0};
            Var: b = 1.1, c = 3.3, i = 0;
            a[9] = b *. c;
            a = foo(a);
            foo(a)[int_of_float(b)] = float_to_int(10);
            For (i = 0, i < 10, 1) Do
                print(string_of_float(a[i]));
            EndFor.
        EndBody.
        Function: foo
        Parameter: a[10]
        Body:
            Return a;
        EndBody.
        """
    	expect = "0.110.00.30.40.50.60.70.80.93.63"
    	self.assertTrue(TestCodeGen.test(input,expect,553))
    def test_case_55(self):
    	input = """
        Var: x[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        Function: main
        Body:
            Var: b = 1, c = 3;
            x[9] = b * c;
            Do
                print(string_of_int(x[b]));
                b = b + 1;
            While check(b, 10) EndDo.
            x = foo();
            b = 0 * 8;
            foo()[b] = int_of_float(20.5);
            While b < 10 Do
                print(string_of_int(foo()[b]));
                b = b + 1;
            EndWhile.
        EndBody.
        Function: foo
        Body:
            Return x;
        EndBody.
        Function: check
        Parameter: a, b
        Body:
            Return a < b;
        EndBody.
        """
    	expect = "12345678320123456783"
    	self.assertTrue(TestCodeGen.test(input,expect,554))
    def test_case_56(self):
    	input = """
        Var: x[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        Function: main
        Body:
            Var: idx = 0;
            foo();
            While idx < 10 Do
                print(string_of_int(x[idx]));
                idx = idx + 1;
            EndWhile.
        EndBody.
        Function: foo
        Body:
            Var: i = 3;
            For (i = 3, i < 10, 1) Do
                x[i] = i * 10 + i;
            EndFor.
        EndBody.
        """
    	expect = "01233445566778899"
    	self.assertTrue(TestCodeGen.test(input,expect,555))
    def test_case_57(self):
    	input = """
        Var: x[10] = {"This", "is", "a", "simple", "testcase", "and", "it", "passes", "doesn\\'t", "it?"};
        Function: main
        Body:
            Var: i = 0;
            Do
                print(x[i]);
                If i < 9 Then
                    print(" ");
                EndIf.
                i = i + 1;
            While i < 10 EndDo.
        EndBody.
        """
    	expect = "This is a simple testcase and it passes doesn't it?"
    	self.assertTrue(TestCodeGen.test(input,expect,556))
    def test_case_58(self):
    	input = """
        Var: x[4] = {True, True, False, True};
        Function: main
        Body:
            Var: i = 0;
            If x[0] && x[1] Then
                print("A");
            EndIf.
        EndBody.
        """
    	expect = "A"
    	self.assertTrue(TestCodeGen.test(input,expect,557))
    def test_case_59(self):
    	input = """
        Var: x[5] = {"A", "B", "C", "D", "E"};
        Function: main
        Body:
            Var: k = 4;
            While k >= 0 Do
                k = k - foo();
                If k < 0 Then
                    print("OutOutOut");
                    Break;
                EndIf.
                print(x[k]);
            EndWhile.
        EndBody.
        Function: foo
        Body:
            Return 1;
        EndBody.
        """
    	expect = "DCBAOutOutOut"
    	self.assertTrue(TestCodeGen.test(input,expect,558))
    def test_case_60(self):
    	input = """
        Function: main
        Body:
            Var: i = 0;
            Var: n = 20;
            While i < n Do
                If i % 2 == 0 Then
                    i = i + 1;
                    Continue;
                EndIf.
                print(string_of_int(i));
                i = i + 1;
            EndWhile.
        EndBody.
        """
    	expect = "135791113151719"
    	self.assertTrue(TestCodeGen.test(input,expect,559))
    def test_case_61(self):
    	input = """
        Function: main
        Body:
            Var: i = 0;
            Var: n = 20;
            While i < n Do
                While i < 10 Do
                    print(string_of_int(i));
                    Break;
                EndWhile.
                i = i + 1;
            EndWhile.
        EndBody.
        """
    	expect = "0123456789"
    	self.assertTrue(TestCodeGen.test(input,expect,560))
    def test_case_62(self):
    	input = """
        Function: main
        Body:
            Var: i = 0;
            Var: n = 20;
            While i < n Do
                While i < 10 Do
                    print(string_of_int(i));
                    If i < 5 Then
                        Break;
                    EndIf.
                    i = i + 1;
                    Continue;
                EndWhile.
                i = i + 1;
            EndWhile.
        EndBody.
        """
    	expect = "0123456789"
    	self.assertTrue(TestCodeGen.test(input,expect,561))
    def test_case_63(self):
    	input = """
        Function: main
        Body:
            Var: i = 0;
            Var: n = 20;
            While i < n Do
                If i == 5 Then
                    While True Do
                        print("a");
                        Break;
                    EndWhile.
                    Break;
                EndIf.
                i = i + 1;
            EndWhile.
            print(string_of_int(i));
        EndBody.
        """
    	expect = "a5"
    	self.assertTrue(TestCodeGen.test(input,expect,562))
    def test_case_64(self):
    	input = """
        Function: main
        Body:
            Var: i = 0;
            Var: n = 20;
            While i < n Do
                If True Then
                    i = i + 1;
                    Continue;
                EndIf.
                print("A");
            EndWhile.
            print(string_of_int(i));
        EndBody.
        """
    	expect = "20"
    	self.assertTrue(TestCodeGen.test(input,expect,563))
    def test_case_65(self):
    	input = """
        Var: x[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        Function: main
        Body:
            print(string_of_int(foo(x, 10)));
        EndBody.
        Function: foo
        Parameter: x[10], length
        Body:
            If length == 0 Then
                Return 0;
            ElseIf length == 1 Then
                Return x[0];
            Else
                Return x[length - 1] + foo(x, length -  2);
            EndIf.
        EndBody.
        """
    	expect = "30"
    	self.assertTrue(TestCodeGen.test(input,expect,564))
    def test_case_66(self):
    	input = """
        Var: x[10] = {100, 90, 80, 70, 60, 50, 40, 30, 20, 10};
        Function: main
        Body:
            Var: length = 10;
            Var: idx = 0;
            sort(x, length);
            While idx < length Do
                print(string_of_int(x[idx]));
                print(" ");
                idx = idx + 1;
            EndWhile.
        EndBody.
        Function: sort
        Parameter: arr[10], length
        Body:
            Var: i = 0;
            While i < length - 1 Do
                Var: j = 0;
                j = i + 1;
                Do
                    If arr[i] > arr[j] Then
                        swap(arr, i, j);
                    EndIf.
                    j = j + 1;
                While j < length EndDo.
                i = i + 1;
            EndWhile.
        EndBody.
        Function: swap
        Parameter: arr[10], i, j
        Body:
            Var: temp = 0;
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        EndBody.
        """
    	expect = "10 20 30 40 50 60 70 80 90 100 "
    	self.assertTrue(TestCodeGen.test(input,expect,565))
    def test_case_67(self):
    	input = """
        Function: main
        Body:
            Var: x = 10;
            Var: u = 1, y = 3, z = 3;
            test();
        EndBody.
        Function: test
        Body:
            Var: i = 0;
            For (i = 0, i < 10, 1) Do
                Var: s[9] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
                print(string_of_int(i));
                i = i + 2;
                If i > 5 Then
                    Break;
                Else
                    Continue;
                EndIf.
            EndFor.
        EndBody.
        """
    	expect = "036"
    	self.assertTrue(TestCodeGen.test(input,expect,566))
    def test_case_68(self):
    	input = """      
        Function: main
        Body:
            Var: k = 5.0;
            Var: m = 2.0;
            print(string_of_int(int_of_float(k \. m)));
        EndBody.
        """
    	expect = "2"
    	self.assertTrue(TestCodeGen.test(input,expect,567))
    def test_case_69(self):
    	input = """
        Var: arr[10] = {1,2,3,4,5,6,7,8,9,10};
        Function: main
        Body:
            Var: min = 1;
            Var: max = 1;
            Var: i = 1;
            min = arr[0];
            max = arr[0];
            While i < 10 Do
                If min > arr[i] Then
                    min = arr[i];
                EndIf.
                If max < arr[i] Then
                    If i == 9 Then
                        If max > min Then
                            print("aaassd");
                            Break;
                        EndIf.
                    EndIf.
                    max = arr[i];
                EndIf.
                i = i + 1;
            EndWhile.
            print(string_of_int(min));
            print(string_of_int(max));
        EndBody.
        """
    	expect = "aaassd19"
    	self.assertTrue(TestCodeGen.test(input,expect,568))
    def test_case_70(self):
    	input = """
        Function: main
        Body:
            printStrLn(string_of_bool(True || False));
            printStrLn(string_of_bool(True || True));
            printStrLn(string_of_bool(False || True));
            printStrLn(string_of_bool(False || False));
            printStrLn(string_of_bool(True && True));
            printStrLn(string_of_bool(True && False));
            printStrLn(string_of_bool(False && False));
            printStrLn(string_of_bool(False && True));
        EndBody.
        """
    	expect = "true\ntrue\ntrue\nfalse\ntrue\nfalse\nfalse\nfalse\n"
    	self.assertTrue(TestCodeGen.test(input,expect,569))
    def test_case_71(self):
    	input = """
        Function: foo
        Parameter: arr[7], x, y
        Body:
            arr[x] = arr[y] + 1;
            x = y;
        EndBody.
        Function: main
        Body:
          Var: x[7] = {10, 80, 30, 90, 40, 50, 70};
          Var: a = 0, b = 4;
          foo(x, a, b);
          print(string_of_int(b));
          print(string_of_int(x[b]));
        EndBody.
        """
    	expect = "440"
    	self.assertTrue(TestCodeGen.test(input,expect,570))
    def test_case_72(self):
    	input = """
        Function: max
        Parameter: x
        Body:
            printStrLn(x);
        EndBody.
        Function: main
        Body:
            max("Hello 2021");
        EndBody.
        """
    	expect = "Hello 2021\n"
    	self.assertTrue(TestCodeGen.test(input,expect,571))
    def test_case_73(self):
    	input = """
        Var: arr[8] = {1, 2, 3, 4, 5, 6, 7, 8};
        Function: identity
        Parameter: x
        Body:
            Return int_of_float(float_of_string(x));
        EndBody.
        Function: main
        Body:
            print(string_of_int(arr[arr[arr[arr[identity("2.424")]]]]));
        EndBody.
        """
    	expect = "6"
    	self.assertTrue(TestCodeGen.test(input,expect,572))
    # def test_case_39(self):
    # 	input = """
    #     Function: fibonaci
    #     Parameter: n
    #     Body:
    #         If (n == 0) || (n == 1) Then
    #             Return n;
    #         EndIf.
    #         Return fibonaci(n - 1) + fibonaci(n - 2);
    #     EndBody.
    #     Function: main
    #     Body:
    #         print(string_of_int(fibonaci(22)));
    #     EndBody.
    #     """
    # 	expect = "17711"
    # 	self.assertTrue(TestCodeGen.test(input,expect,538))
    # def test_case_40(self):
    #     input = """
    #     Function: fibonaci
    #     Parameter: n
    #     Body:
    #         Var: x[21] = {0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
    #         Var: i = 2;
    #         While i <= n Do
    #             x[i] = x[i - 1] + x[i - 2];
    #             i = i + 1;
    #         EndWhile.
    #         print(string_of_int(x[n]));
    #     EndBody.
    #     Function: main
    #     Body:
    #         fibonaci(20);
    #     EndBody.
    #     """
    #     expect = "6765"
    #     self.assertTrue(TestCodeGen.test(input,expect,539))
    # def test_case_41(self):
    # 	input = """
    #     Function: fibonaci
    #     Parameter: n
    #     Body:
    #         Var: i = 2;
    #         Var: f = 0, g = 1;
    #         For (i = 2, i < n + 1, 1) Do
    #             g = f + g;
    #             f = g - f;
    #         EndFor.
    #         print(string_of_int(g));
    #     EndBody.
    #     Function: main
    #     Body:
    #         fibonaci(30);
    #     EndBody.
    #     """
    # 	expect = "832040"
    # 	self.assertTrue(TestCodeGen.test(input,expect,540))