import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_0(self):
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))


    def test_1(self):
        input = """Var:x,y,z;"""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_2(self):
        input = """Var:x, y = 2, z[1][2][3]=True;"""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],IntLiteral(2)),VarDecl(Id("z"),[1,2,3],BooleanLiteral(True))])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_3(self):
        input = """Var:x, y = 2, z[1][2][3]=True;
                Var: a[69], b = "DSM", c = 0;"""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],IntLiteral(2)),VarDecl(Id("z"),[1,2,3],BooleanLiteral(True)),VarDecl(Id("a"),[69],None),VarDecl(Id("b"),[],StringLiteral("DSM")),VarDecl(Id("c"),[],IntLiteral(0))])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_4(self):
        input = """Function: main
                    Body:
                        If x == 1 Then
                            print1(1);
                        ElseIf x == 2 Then
                            print2(2);
                        Else
                            print3(3);
                        EndIf.
                    EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[If([(BinaryOp('==',Id('x'),IntLiteral(1)),[],[CallStmt(Id('print1'),[IntLiteral(1)])]),(BinaryOp('==',Id('x'),IntLiteral(2)),[],[CallStmt(Id('print2'),[IntLiteral(2)])])],([],[CallStmt(Id('print3'),[IntLiteral(3)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_5(self):
        input = """
        Var: epsilon = 1e-6;
        Function: isInteger
        Parameter: d
        Body:
            Return d - round(d) <. epsilon;
        EndBody.
        Function: main
        Parameter: argc, argv
        Body:
            If (argc != 2) Then
                Return -1;
            Else
                If isInteger(atof(argv[2])) Then
                    print("True");
                Else
                    print("False");
                EndIf.
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id('epsilon'),[],FloatLiteral(1e-06)),FuncDecl(Id('isInteger'),[VarDecl(Id('d'),[],None)],([],[Return(BinaryOp('<.',BinaryOp('-',Id('d'),CallExpr(Id('round'),[Id('d')])),Id('epsilon')))])),FuncDecl(Id('main'),[VarDecl(Id('argc'),[],None),VarDecl(Id('argv'),[],None)],([],[If([(BinaryOp('!=',Id('argc'),IntLiteral(2)),[],[Return(UnaryOp('-',IntLiteral(1)))])],([],[If([(CallExpr(Id('isInteger'),[CallExpr(Id('atof'),[ArrayCell(Id('argv'),[IntLiteral(2)])])]),[],[CallStmt(Id('print'),[StringLiteral('''True''')])])],([],[CallStmt(Id('print'),[StringLiteral('''False''')])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_6(self):
        input = """
        Function: abc
        Parameter: x, y, z[4][5]
        Body:
            Var: sum, n;
            For (i = 0, i < n, i + 1) Do
                sum = sum + i;
            EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[4,5],None)],([VarDecl(Id('sum'),[],None),VarDecl(Id('n'),[],None)],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),Id('n')),BinaryOp('+',Id('i'),IntLiteral(1)),([],[Assign(Id('sum'),BinaryOp('+',Id('sum'),Id('i')))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_7(self):
        input = """
        Var: x;
        Function: main
        Body:
            Var: r = 10., v, i;
            v = (4.5 \. 3.1) *. 3.143 *. r *. r *. r;
            For (i = 0, i <. 10., 2.) Do
                writeln(i);
            EndFor.
            Return 0;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('main'),[],([VarDecl(Id('r'),[],FloatLiteral(10.0)),VarDecl(Id('v'),[],None),VarDecl(Id('i'),[],None)],[Assign(Id('v'),BinaryOp('*.',BinaryOp('*.',BinaryOp('*.',BinaryOp('*.',BinaryOp('\.',FloatLiteral(4.5),FloatLiteral(3.1)),FloatLiteral(3.143)),Id('r')),Id('r')),Id('r'))),For(Id('i'),IntLiteral(0),BinaryOp('<.',Id('i'),FloatLiteral(10.0)),FloatLiteral(2.0),([],[CallStmt(Id('writeln'),[Id('i')])])),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_8(self):
        input = """
        Var: x;
        Function: main
        Body:
            Var: a[50];
            a[4 + foo(3)] = a[b[13][5]] + 6;
            Return 0;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('main'),[],([VarDecl(Id('a'),[50],None)],[Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(4),CallExpr(Id('foo'),[IntLiteral(3)]))]),BinaryOp('+',ArrayCell(Id('a'),[ArrayCell(Id('b'),[IntLiteral(13),IntLiteral(5)])]),IntLiteral(6))),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_9(self):
        input = """
        Var: x;
        Function: main
        Body:
            Var: a[10];
            a[3 + foo(True)] = a[b[2][3]] + 3;
            Return 0;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('main'),[],([VarDecl(Id('a'),[10],None)],[Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('foo'),[BooleanLiteral(True)]))]),BinaryOp('+',ArrayCell(Id('a'),[ArrayCell(Id('b'),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(3))),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_10(self):
        input = """
        Function: main
        Body:
            Var: a[10] = {0};
            Var: b;
            For(b = 0, b < 10, 2) Do
                print(b);
            EndFor.
            Return 0;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([VarDecl(Id('a'),[10],ArrayLiteral([IntLiteral(0)])),VarDecl(Id('b'),[],None)],[For(Id('b'),IntLiteral(0),BinaryOp('<',Id('b'),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id('print'),[Id('b')])])),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_11(self):
        input = """
        Function: foo
        Parameter: a[5]
        Body:
            Return a[rand(12)];
        EndBody.
        Function: main
        Body:
            print(foo({1,2,3,4,5}));
            Return 0;
        EndBody.
        """
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[5],None)],([],[Return(ArrayCell(Id('a'),[CallExpr(Id('rand'),[IntLiteral(12)])]))])),FuncDecl(Id('main'),[],([],[CallStmt(Id('print'),[CallExpr(Id('foo'),[ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])])]),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_12(self):
        input = """
        Var: x = {{1,2}, {3,4}};       
        """
        expect = Program([VarDecl(Id('x'),[],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(3),IntLiteral(4)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_13(self):
        input = """
        Var: x = {1, 3.5, True, {6, 9, 6, 9}, "some"};
        """
        expect = Program([VarDecl(Id('x'),[],ArrayLiteral([IntLiteral(1),FloatLiteral(3.5),BooleanLiteral(True),ArrayLiteral([IntLiteral(6),IntLiteral(9),IntLiteral(6),IntLiteral(9)]),StringLiteral('''some''')]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_14(self):
        input = """
        Var: x = {{1, 5.5}, 4e4, {"False"}, {1, 9 ,{4}}};
        """
        expect = Program([VarDecl(Id('x'),[],ArrayLiteral([ArrayLiteral([IntLiteral(1),FloatLiteral(5.5)]),FloatLiteral(40000.0),ArrayLiteral([StringLiteral('''False''')]),ArrayLiteral([IntLiteral(1),IntLiteral(9),ArrayLiteral([IntLiteral(4)])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_15(self):
        input = """
        Var: x = { {1,2}, 
                    {3,4},
                    {5,6},
                    {7,8},
                    ** comment **
                    {9, 0}
                };
        """
        expect = Program([VarDecl(Id('x'),[],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(5),IntLiteral(6)]),ArrayLiteral([IntLiteral(7),IntLiteral(8)]),ArrayLiteral([IntLiteral(9),IntLiteral(0)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_16(self):
        input = """
        Function: main
        Parameter: a, b, c
        Body:
            Var: a = 5, b = 2, c = 3;
            Var: y = 1, x = 3, z;
            x = a;
            y = b + c;
            z = b * c;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([VarDecl(Id('a'),[],IntLiteral(5)),VarDecl(Id('b'),[],IntLiteral(2)),VarDecl(Id('c'),[],IntLiteral(3)),VarDecl(Id('y'),[],IntLiteral(1)),VarDecl(Id('x'),[],IntLiteral(3)),VarDecl(Id('z'),[],None)],[Assign(Id('x'),Id('a')),Assign(Id('y'),BinaryOp('+',Id('b'),Id('c'))),Assign(Id('z'),BinaryOp('*',Id('b'),Id('c')))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_17(self):
        input = """
        Var: x = {{}, {{{{},{{{}}},{}},{},{}}}, {{}, {}}};
        """
        expect = Program([VarDecl(Id('x'),[],ArrayLiteral([ArrayLiteral([]),ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([]),ArrayLiteral([ArrayLiteral([ArrayLiteral([])])]),ArrayLiteral([])]),ArrayLiteral([]),ArrayLiteral([])])]),ArrayLiteral([ArrayLiteral([]),ArrayLiteral([])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
    
    def test_18(self):
        input = """
        Function: main
        Parameter: a, b, c[0o123]
        Body:
            Var: x[0x123];
            a = 4 + !1 && 9;
            b = True && False || True;
            c = 4 - 3 * (5 +. 2);
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[83],None)],([VarDecl(Id('x'),[291],None)],[Assign(Id('a'),BinaryOp('&&',BinaryOp('+',IntLiteral(4),UnaryOp('!',IntLiteral(1))),IntLiteral(9))),Assign(Id('b'),BinaryOp('||',BinaryOp('&&',BooleanLiteral(True),BooleanLiteral(False)),BooleanLiteral(True))),Assign(Id('c'),BinaryOp('-',IntLiteral(4),BinaryOp('*',IntLiteral(3),BinaryOp('+.',IntLiteral(5),IntLiteral(2)))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_19(self):
        input = """
        Function: abc
        Parameter: x, y, z[4][5]
        Body:
            If 1 + 2 == 3 Then
                x = 6;
                t = 7;
            ElseIf x == 2 Then
                y = 8;
                z = 9;
            ElseIf vlxx() > xnxx() Then
                y = 10;
                z = 11;
            ElseIf x[1] + y[z] == 7 Then
                y = 12;
                z = 13;
            Else z = 14;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[4,5],None)],([],[If([(BinaryOp('==',BinaryOp('+',IntLiteral(1),IntLiteral(2)),IntLiteral(3)),[],[Assign(Id('x'),IntLiteral(6)),Assign(Id('t'),IntLiteral(7))]),(BinaryOp('==',Id('x'),IntLiteral(2)),[],[Assign(Id('y'),IntLiteral(8)),Assign(Id('z'),IntLiteral(9))]),(BinaryOp('>',CallExpr(Id('vlxx'),[]),CallExpr(Id('xnxx'),[])),[],[Assign(Id('y'),IntLiteral(10)),Assign(Id('z'),IntLiteral(11))]),(BinaryOp('==',BinaryOp('+',ArrayCell(Id('x'),[IntLiteral(1)]),ArrayCell(Id('y'),[Id('z')])),IntLiteral(7)),[],[Assign(Id('y'),IntLiteral(12)),Assign(Id('z'),IntLiteral(13))])],([],[Assign(Id('z'),IntLiteral(14))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_20(self):
        input = """
        Function: abc
        Parameter: x, y, z[4][5]
        Body:
            If 2 * 3 == 6 Then
                Var: x, t;
                x = 2 * 3;
                t = 7;
            ElseIf x + y == z Then
                If 3 + 5 == 6 Then
                EndIf.
            ElseIf rand() > 10 Then
                Var: a, b;
                a = 9.0000009e12;
                b = 10;
            Else z = 69;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[4,5],None)],([],[If([(BinaryOp('==',BinaryOp('*',IntLiteral(2),IntLiteral(3)),IntLiteral(6)),[VarDecl(Id('x'),[],None),VarDecl(Id('t'),[],None)],[Assign(Id('x'),BinaryOp('*',IntLiteral(2),IntLiteral(3))),Assign(Id('t'),IntLiteral(7))]),(BinaryOp('==',BinaryOp('+',Id('x'),Id('y')),Id('z')),[],[If([(BinaryOp('==',BinaryOp('+',IntLiteral(3),IntLiteral(5)),IntLiteral(6)),[],[])],None)]),(BinaryOp('>',CallExpr(Id('rand'),[]),IntLiteral(10)),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],[Assign(Id('a'),FloatLiteral(9000000900000.0)),Assign(Id('b'),IntLiteral(10))])],([],[Assign(Id('z'),IntLiteral(69))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_21(self):
        input = """
        Function: abc
        Parameter: x, y, z[1][2]
        Body:
            z = {{1, 2}, {3, 4}};
            For (a = 3, a == 10, 1) Do
                If a == 5 Then Break;
                EndIf.
            EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[1,2],None)],([],[Assign(Id('z'),ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(3),IntLiteral(4)])])),For(Id('a'),IntLiteral(3),BinaryOp('==',Id('a'),IntLiteral(10)),IntLiteral(1),([],[If([(BinaryOp('==',Id('a'),IntLiteral(5)),[],[Break()])],None)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    
    def test_22(self):
        input = """
        Function: main
        Parameter: x, y, z[1][2]
        Body:
            While a % b =/= 0 Do
                a = b;
                b = b - a;
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[1,2],None)],([],[While(BinaryOp('=/=',BinaryOp('%',Id('a'),Id('b')),IntLiteral(0)),([],[Assign(Id('a'),Id('b')),Assign(Id('b'),BinaryOp('-',Id('b'),Id('a')))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    
    def test_23(self):
        input = """
        Function: abc
        Parameter: x, y, z
        Body:
            While True Do
                Break;
                Continue;
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[],None)],([],[While(BooleanLiteral(True),([],[Break(),Continue()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    
    def test_24(self):
        input = """
        Var: x;
        Function: fact
        Parameter: n
        Body:
            If n == 0 Then
                Return 1;
            Else
                Return n * fact(n-1);
            EndIf.
        EndBody.
        Function: main
        Body:
            x = 10;
            print(fact(x));
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None)],([],[If([(BinaryOp('==',Id('n'),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[Return(BinaryOp('*',Id('n'),CallExpr(Id('fact'),[BinaryOp('-',Id('n'),IntLiteral(1))])))]))])),FuncDecl(Id('main'),[],([],[Assign(Id('x'),IntLiteral(10)),CallStmt(Id('print'),[CallExpr(Id('fact'),[Id('x')])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_25(self):
        input = """
        Function: reverse
        Parameter: str
        Body:
            If str[0] == terminated_char Then
                Return "";
            Else
                Return reverse(str + 1) + str[0];
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('reverse'),[VarDecl(Id('str'),[],None)],([],[If([(BinaryOp('==',ArrayCell(Id('str'),[IntLiteral(0)]),Id('terminated_char')),[],[Return(StringLiteral(''''''))])],([],[Return(BinaryOp('+',CallExpr(Id('reverse'),[BinaryOp('+',Id('str'),IntLiteral(1))]),ArrayCell(Id('str'),[IntLiteral(0)])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    
    def test_26(self):
        input = """
        Function: foo
        Parameter: a[5], b
        Body:
            Var: x = True;
            Do
                a[1] = b *. 3;
                i = i + 1;
                x = a[0xFFFF] || a[0O7777];
            While (x <=. b)
            EndDo.
        EndBody.
        """
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[5],None),VarDecl(Id('b'),[],None)],([VarDecl(Id('x'),[],BooleanLiteral(True))],[Dowhile(([],[Assign(ArrayCell(Id('a'),[IntLiteral(1)]),BinaryOp('*.',Id('b'),IntLiteral(3))),Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Assign(Id('x'),BinaryOp('||',ArrayCell(Id('a'),[IntLiteral(65535)]),ArrayCell(Id('a'),[IntLiteral(4095)])))]),BinaryOp('<=.',Id('x'),Id('b')))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    
    def test_27(self):
        input = """
        Var: terminated_char = "\\\\0";
        Function: strlen
        Parameter: str
        Body:
            Var: len = 0;
            While str[len] =/= terminated_char Do
                len = len + 1;
            EndWhile.
            Return len;
        EndBody.
        """
        expect = Program([VarDecl(Id('terminated_char'),[],StringLiteral('''\\\\0''')),FuncDecl(Id('strlen'),[VarDecl(Id('str'),[],None)],([VarDecl(Id('len'),[],IntLiteral(0))],[While(BinaryOp('=/=',ArrayCell(Id('str'),[Id('len')]),Id('terminated_char')),([],[Assign(Id('len'),BinaryOp('+',Id('len'),IntLiteral(1)))])),Return(Id('len'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    
    def test_28(self):
        input = """
        Function: max2
        Parameter: a, b
        Body:
            If a > b Then
                Return a;
            Else
                Return b;
            EndIf.
        EndBody.
        Function: max3
        Parameter: a, b, c
        Body:
            Return max2(max2(a, b), c);
        EndBody.
        """
        expect = Program([FuncDecl(Id('max2'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([],[If([(BinaryOp('>',Id('a'),Id('b')),[],[Return(Id('a'))])],([],[Return(Id('b'))]))])),FuncDecl(Id('max3'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Return(CallExpr(Id('max2'),[CallExpr(Id('max2'),[Id('a'),Id('b')]),Id('c')]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    
    
    def test_29(self):
        input = """
        Function: swap
        Parameter: a,b
        Body:
            Var: temp;
            temp = a;
            a = b;
            b = temp;
        EndBody.
        """
        expect = Program([FuncDecl(Id('swap'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([VarDecl(Id('temp'),[],None)],[Assign(Id('temp'),Id('a')),Assign(Id('a'),Id('b')),Assign(Id('b'),Id('temp'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
    
    def test_30(self):
        input = """
        Function: sumOfDigit
        Parameter: n
        Body:
            If (n == 0) Then
                Return 0;
            Else
                Return n % 10 + sumOfDigit(n \\ 10);
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('sumOfDigit'),[VarDecl(Id('n'),[],None)],([],[If([(BinaryOp('==',Id('n'),IntLiteral(0)),[],[Return(IntLiteral(0))])],([],[Return(BinaryOp('+',BinaryOp('%',Id('n'),IntLiteral(10)),CallExpr(Id('sumOfDigit'),[BinaryOp('\\',Id('n'),IntLiteral(10))])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    
    def test_31(self):
        input = """
        Function: trimLeft
        Parameter: str
        Body:
            While (contain("\\t ", str)) Do
                str = str + 1;
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id('trimLeft'),[VarDecl(Id('str'),[],None)],([],[While(CallExpr(Id('contain'),[StringLiteral('''\\t '''),Id('str')]),([],[Assign(Id('str'),BinaryOp('+',Id('str'),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    
    def test_32(self):
        input = """
        Function: printReverse
        Parameter: n
        Body:
            If n == 0 Then
                print(0);
            Else
                print(n \\ 10);
                print(n % 10);
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('printReverse'),[VarDecl(Id('n'),[],None)],([],[If([(BinaryOp('==',Id('n'),IntLiteral(0)),[],[CallStmt(Id('print'),[IntLiteral(0)])])],([],[CallStmt(Id('print'),[BinaryOp('\\',Id('n'),IntLiteral(10))]),CallStmt(Id('print'),[BinaryOp('%',Id('n'),IntLiteral(10))])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
    
    def test_33(self):
        input = """
        Function: findMax
        Parameter: arr
        Body:
            Var: max;
            max = arr[0];
            For (i = 0, i < len(arr), 1) Do
                If arr[i] > max Then
                    max = arr[i];
                EndIf.
            EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id('findMax'),[VarDecl(Id('arr'),[],None)],([VarDecl(Id('max'),[],None)],[Assign(Id('max'),ArrayCell(Id('arr'),[IntLiteral(0)])),For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),CallExpr(Id('len'),[Id('arr')])),IntLiteral(1),([],[If([(BinaryOp('>',ArrayCell(Id('arr'),[Id('i')]),Id('max')),[],[Assign(Id('max'),ArrayCell(Id('arr'),[Id('i')]))])],None)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    
    def test_34(self):
        input = """
        Function: main
        Parameter: complicated
        Body:
            inp = 1 + 2. + 3e4 + True + False + "String" || !"Char" && {5, 6, {7, 8}} > 9;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('complicated'),[],None)],([],[Assign(Id('inp'),BinaryOp('>',BinaryOp('&&',BinaryOp('||',BinaryOp('+',BinaryOp('+',BinaryOp('+',BinaryOp('+',BinaryOp('+',IntLiteral(1),FloatLiteral(2.0)),FloatLiteral(30000.0)),BooleanLiteral(True)),BooleanLiteral(False)),StringLiteral('''String''')),UnaryOp('!',StringLiteral('''Char'''))),ArrayLiteral([IntLiteral(5),IntLiteral(6),ArrayLiteral([IntLiteral(7),IntLiteral(8)])])),IntLiteral(9)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    
    def test_35(self):
        input = """
        Function: main
        Body:
            Return foo({})[2][3] * 2. \\. 3.0 + 6 || !!zzz;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(BinaryOp('||',BinaryOp('+',BinaryOp('\\.',BinaryOp('*',ArrayCell(CallExpr(Id('foo'),[ArrayLiteral([])]),[IntLiteral(2),IntLiteral(3)]),FloatLiteral(2.0)),FloatLiteral(3.0)),IntLiteral(6)),UnaryOp('!',UnaryOp('!',Id('zzz')))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    
    def test_36(self):
        input = """
        Function: main
        Body:
            If (a > b) Then
                If (a > c) Then
                    Return a;
                Else Break;
                EndIf.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[If([(BinaryOp('>',Id('a'),Id('b')),[],[If([(BinaryOp('>',Id('a'),Id('c')),[],[Return(Id('a'))])],([],[Break()]))])],None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    
    def test_37(self):
        input = """
        Var: x;
        Function: main
        Body:
            Var: r = 10., v, i;
            v = (4. \. 3.) *. 3.14 *. r *. r *. r;
            For (i = 0, i < 10, 2) Do
                writeln(i);
            EndFor.
            Return 0;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('main'),[],([VarDecl(Id('r'),[],FloatLiteral(10.0)),VarDecl(Id('v'),[],None),VarDecl(Id('i'),[],None)],[Assign(Id('v'),BinaryOp('*.',BinaryOp('*.',BinaryOp('*.',BinaryOp('*.',BinaryOp(r'\.',FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id('r')),Id('r')),Id('r'))),For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id('writeln'),[Id('i')])])),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    
    def test_38(self):
        input = """
        Var: x;
        Function: main
        Body:
           Var: a[10];
           a[3 + foo(2)] = a[b[2][3]] + 3;
           Return 0;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('main'),[],([VarDecl(Id('a'),[10],None)],[Assign(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),CallExpr(Id('foo'),[IntLiteral(2)]))]),BinaryOp('+',ArrayCell(Id('a'),[ArrayCell(Id('b'),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(3))),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
    
    def test_39(self):
        input = """
        Function: main
        Parameter: k[0][0x1][0o1][0X1][0O1][1]
        Body:
            Var: i = 10, k[10][2] = {{}, {}};
            Do
                Break;
            While i <= 10 EndDo.
            Return 0;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('k'),[0,1,1,1,1,1],None)],([VarDecl(Id('i'),[],IntLiteral(10)),VarDecl(Id('k'),[10,2],ArrayLiteral([ArrayLiteral([]),ArrayLiteral([])]))],[Dowhile(([],[Break()]),BinaryOp('<=',Id('i'),IntLiteral(10))),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
    
    def test_40(self):
        input = """
        Function: main
        Body:
            Var: x[10];
            x[0] = fact(f(0))[0][4][123];
            Return 0;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([VarDecl(Id('x'),[10],None)],[Assign(ArrayCell(Id('x'),[IntLiteral(0)]),ArrayCell(CallExpr(Id('fact'),[CallExpr(Id('f'),[IntLiteral(0)])]),[IntLiteral(0),IntLiteral(4),IntLiteral(123)])),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    
    def test_41(self):
        input = """
        Var: a, b, c = 10;
        Function: func
        Body:
            Return "Hello World";
        EndBody.
        Function: main
        Body:
            print(func());
            Return;
        EndBody.
        """
        expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],IntLiteral(10)),FuncDecl(Id('func'),[],([],[Return(StringLiteral('''Hello World'''))])),FuncDecl(Id('main'),[],([],[CallStmt(Id('print'),[CallExpr(Id('func'),[])]),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    
    def test_42(self):
        input = """
        Function: abc
        Body:
            x = 5 + 6 + 7;
            y = 5 +. 4 +. 1;
            z = True && False || True;
            w = 4 - 3 - 3;
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[],([],[Assign(Id('x'),BinaryOp('+',BinaryOp('+',IntLiteral(5),IntLiteral(6)),IntLiteral(7))),Assign(Id('y'),BinaryOp('+.',BinaryOp('+.',IntLiteral(5),IntLiteral(4)),IntLiteral(1))),Assign(Id('z'),BinaryOp('||',BinaryOp('&&',BooleanLiteral(True),BooleanLiteral(False)),BooleanLiteral(True))),Assign(Id('w'),BinaryOp('-',BinaryOp('-',IntLiteral(4),IntLiteral(3)),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    
    def test_43(self):
        input = """
        Function: abc
        Body:
            x[3 + 2 + foo() + y[1 + 4 + 6]] = y[2 + 3];
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[],([],[Assign(ArrayCell(Id('x'),[BinaryOp('+',BinaryOp('+',BinaryOp('+',IntLiteral(3),IntLiteral(2)),CallExpr(Id('foo'),[])),ArrayCell(Id('y'),[BinaryOp('+',BinaryOp('+',IntLiteral(1),IntLiteral(4)),IntLiteral(6))]))]),ArrayCell(Id('y'),[BinaryOp('+',IntLiteral(2),IntLiteral(3))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
    
    def test_44(self):
        input = """
        Function: abc
        Body:
            x = True && !False || !!a && !!!bsdklf;
            y = 5.5 -. -.3.3456 -. -.1.2345 +. -.12.e3 +. -.12.;
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[],([],[Assign(Id('x'),BinaryOp('&&',BinaryOp('||',BinaryOp('&&',BooleanLiteral(True),UnaryOp('!',BooleanLiteral(False))),UnaryOp('!',UnaryOp('!',Id('a')))),UnaryOp('!',UnaryOp('!',UnaryOp('!',Id('bsdklf')))))),Assign(Id('y'),BinaryOp('+.',BinaryOp('+.',BinaryOp('-.',BinaryOp('-.',FloatLiteral(5.5),UnaryOp('-.',FloatLiteral(3.3456))),UnaryOp('-.',FloatLiteral(1.2345))),UnaryOp('-.',FloatLiteral(12000.0))),UnaryOp('-.',FloatLiteral(12.0))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
    
    def test_45(self):
        input = """
        Function: abc
        Body:
            x = hoo(foo() + goo(too()) - too(goo() + foo() + qoo()));
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[],([],[Assign(Id('x'),CallExpr(Id('hoo'),[BinaryOp('-',BinaryOp('+',CallExpr(Id('foo'),[]),CallExpr(Id('goo'),[CallExpr(Id('too'),[])])),CallExpr(Id('too'),[BinaryOp('+',BinaryOp('+',CallExpr(Id('goo'),[]),CallExpr(Id('foo'),[])),CallExpr(Id('qoo'),[]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    
    def test_46(self):
        input = """
        Function: foo
        Parameter: a[5], b
        Body:
            Var: i = 0;
            While (i < 5) Do
                a[i] = b +. 1.0;
                i = i + 1;
                If (i % 2 == 0) Then
                    Do
                        x = rand();
                    While (a <. b)
                    EndDo.
                ElseIf (i % 3 == 0) Then
                    doSth();
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[5],None),VarDecl(Id('b'),[],None)],([VarDecl(Id('i'),[],IntLiteral(0))],[While(BinaryOp('<',Id('i'),IntLiteral(5)),([],[Assign(ArrayCell(Id('a'),[Id('i')]),BinaryOp('+.',Id('b'),FloatLiteral(1.0))),Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),If([(BinaryOp('==',BinaryOp('%',Id('i'),IntLiteral(2)),IntLiteral(0)),[],[Dowhile(([],[Assign(Id('x'),CallExpr(Id('rand'),[]))]),BinaryOp('<.',Id('a'),Id('b')))]),(BinaryOp('==',BinaryOp('%',Id('i'),IntLiteral(3)),IntLiteral(0)),[],[CallStmt(Id('doSth'),[])])],None)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,346))
    
    def test_47(self):
        input = """
        Function: test_exp
            Body:
               a = a <= 1;
               b = b >= 1;
               c = c =/= 1;
               d = d <. 1;
               e = e >. 1;
               f = f <=. 1;
               g = g >=. 1;
               h = a[1] + b[a[1]*1-a[e[c+d]]];
            EndBody.
        """
        expect = Program([FuncDecl(Id('test_exp'),[],([],[Assign(Id('a'),BinaryOp('<=',Id('a'),IntLiteral(1))),Assign(Id('b'),BinaryOp('>=',Id('b'),IntLiteral(1))),Assign(Id('c'),BinaryOp('=/=',Id('c'),IntLiteral(1))),Assign(Id('d'),BinaryOp('<.',Id('d'),IntLiteral(1))),Assign(Id('e'),BinaryOp('>.',Id('e'),IntLiteral(1))),Assign(Id('f'),BinaryOp('<=.',Id('f'),IntLiteral(1))),Assign(Id('g'),BinaryOp('>=.',Id('g'),IntLiteral(1))),Assign(Id('h'),BinaryOp('+',ArrayCell(Id('a'),[IntLiteral(1)]),ArrayCell(Id('b'),[BinaryOp('-',BinaryOp('*',ArrayCell(Id('a'),[IntLiteral(1)]),IntLiteral(1)),ArrayCell(Id('a'),[ArrayCell(Id('e'),[BinaryOp('+',Id('c'),Id('d'))])]))])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
    
    def test_48(self):
        input = """
        Var: hex = 0x567A;
        Var: oct = 0O123;
        Function: test
        Parameter: a,b
        Body:
            Return a + b;
        EndBody.
        Function: main
        Body:
            Return test(hex, oct);
        EndBody.
        """
        expect = Program([VarDecl(Id('hex'),[],IntLiteral(22138)),VarDecl(Id('oct'),[],IntLiteral(83)),FuncDecl(Id('test'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([],[Return(BinaryOp('+',Id('a'),Id('b')))])),FuncDecl(Id('main'),[],([],[Return(CallExpr(Id('test'),[Id('hex'),Id('oct')]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
    
    def test_49(self):
        input = """
        Function: main
        Body:
            Do
                func(0x45);
                While x Do
                    Var: x;
                    If x == 1 Then
                        Var: x;
                    EndIf.
                EndWhile.
            While True EndDo.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Dowhile(([],[CallStmt(Id('func'),[IntLiteral(69)]),While(Id('x'),([VarDecl(Id('x'),[],None)],[If([(BinaryOp('==',Id('x'),IntLiteral(1)),[VarDecl(Id('x'),[],None)],[])],None)]))]),BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,349))
    
    def test_50(self):
        input = """
        Var: x = {{{1,  2  }, {  4 , "Nested",  5}  },  {{ 6  ,  7  },{ 8,9}}};
        """
        expect = Program([VarDecl(Id('x'),[],ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(4),StringLiteral('''Nested'''),IntLiteral(5)])]),ArrayLiteral([ArrayLiteral([IntLiteral(6),IntLiteral(7)]),ArrayLiteral([IntLiteral(8),IntLiteral(9)])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    
    def test_51(self):
        input = """
        Function: abc
        Parameter: x, y, z
        Body:
            Var: x = 4, y, z = 8;
            Var: y = 1, x = 3, q;
            x = 1;
            y = 7;
            z = 6;
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[],None)],([VarDecl(Id('x'),[],IntLiteral(4)),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[],IntLiteral(8)),VarDecl(Id('y'),[],IntLiteral(1)),VarDecl(Id('x'),[],IntLiteral(3)),VarDecl(Id('q'),[],None)],[Assign(Id('x'),IntLiteral(1)),Assign(Id('y'),IntLiteral(7)),Assign(Id('z'),IntLiteral(6))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
    
    def test_52(self):
        input = """
        Function: abc
        Body:
            x = 1 - 2 + 3 * 5 \\ 0x21;
            y = 0o234 +. 3 -. 6.9 *. 8.0 \\. 3.14e1;
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[],([],[Assign(Id('x'),BinaryOp('+',BinaryOp('-',IntLiteral(1),IntLiteral(2)),BinaryOp('\\',BinaryOp('*',IntLiteral(3),IntLiteral(5)),IntLiteral(33)))),Assign(Id('y'),BinaryOp('-.',BinaryOp('+.',IntLiteral(156),IntLiteral(3)),BinaryOp('\\.',BinaryOp('*.',FloatLiteral(6.9),FloatLiteral(8.0)),FloatLiteral(31.4))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    
    def test_53(self):
        input = """
        Function: abc
        Body:
            x = 1 != 2;
            y = 1 == (2 < 3);
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[],([],[Assign(Id('x'),BinaryOp('!=',IntLiteral(1),IntLiteral(2))),Assign(Id('y'),BinaryOp('==',IntLiteral(1),BinaryOp('<',IntLiteral(2),IntLiteral(3))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,353))
    
    def test_54(self):
        input = """
        Function: abc
        Body:
            getArray()[3 + 4 + (5 * 8)] = 5 + 7;
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[],([],[Assign(ArrayCell(CallExpr(Id('getArray'),[]),[BinaryOp('+',BinaryOp('+',IntLiteral(3),IntLiteral(4)),BinaryOp('*',IntLiteral(5),IntLiteral(8)))]),BinaryOp('+',IntLiteral(5),IntLiteral(7)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,354))
    
    def test_55(self):
        input = """
        Function: abc
        Parameter: x, y, z[4][5]
        Body:
            If 12 + 13 == 54 Then
                x = 6134;
                t = 7900000000000;
            ElseIf 1 + 3 == 7 Then
                y = 9.00000000001;
                z = 10;
            ElseIf f() > g() Then
                y = 9;
                z = 10;
            ElseIf 1 + 3 == 7 Then
                y = 9;
                z = 10;
            Else z = 11;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[4,5],None)],([],[If([(BinaryOp('==',BinaryOp('+',IntLiteral(12),IntLiteral(13)),IntLiteral(54)),[],[Assign(Id('x'),IntLiteral(6134)),Assign(Id('t'),IntLiteral(7900000000000))]),(BinaryOp('==',BinaryOp('+',IntLiteral(1),IntLiteral(3)),IntLiteral(7)),[],[Assign(Id('y'),FloatLiteral(9.00000000001)),Assign(Id('z'),IntLiteral(10))]),(BinaryOp('>',CallExpr(Id('f'),[]),CallExpr(Id('g'),[])),[],[Assign(Id('y'),IntLiteral(9)),Assign(Id('z'),IntLiteral(10))]),(BinaryOp('==',BinaryOp('+',IntLiteral(1),IntLiteral(3)),IntLiteral(7)),[],[Assign(Id('y'),IntLiteral(9)),Assign(Id('z'),IntLiteral(10))])],([],[Assign(Id('z'),IntLiteral(11))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,355))
    
    def test_56(self):
        input = """
        Function: abc
        Body:
            getArray()[3 + 2 + foo() + y()[1 + 4 + 6]] = y()[2 + 3];
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[],([],[Assign(ArrayCell(CallExpr(Id('getArray'),[]),[BinaryOp('+',BinaryOp('+',BinaryOp('+',IntLiteral(3),IntLiteral(2)),CallExpr(Id('foo'),[])),ArrayCell(CallExpr(Id('y'),[]),[BinaryOp('+',BinaryOp('+',IntLiteral(1),IntLiteral(4)),IntLiteral(6))]))]),ArrayCell(CallExpr(Id('y'),[]),[BinaryOp('+',IntLiteral(2),IntLiteral(3))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,356))
    
    def test_57(self):
        input = """
        Function: main
        Body:
            x = !!!!-------.-.-.2;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(Id('x'),UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-.',UnaryOp('-.',UnaryOp('-.',IntLiteral(2)))))))))))))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,357))
    
    def test_58(self):
        input = """
        Function: abc
        Body:
            x = -5 + -7 - -8 - -9 - -------10;
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[],([],[Assign(Id('x'),BinaryOp('-',BinaryOp('-',BinaryOp('-',BinaryOp('+',UnaryOp('-',IntLiteral(5)),UnaryOp('-',IntLiteral(7))),UnaryOp('-',IntLiteral(8))),UnaryOp('-',IntLiteral(9))),UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',IntLiteral(10))))))))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,358))
    
    def test_59(self):
        input = """
        Function: abc
        Body:
            x = foo(1, {1, 0x2}) [1 + foo(4, 3213 * sadf())] + asdf("sdfgfg foo()");
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[],([],[Assign(Id('x'),BinaryOp('+',ArrayCell(CallExpr(Id('foo'),[IntLiteral(1),ArrayLiteral([IntLiteral(1),IntLiteral(2)])]),[BinaryOp('+',IntLiteral(1),CallExpr(Id('foo'),[IntLiteral(4),BinaryOp('*',IntLiteral(3213),CallExpr(Id('sadf'),[]))]))]),CallExpr(Id('asdf'),[StringLiteral('''sdfgfg foo()''')])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,359))
    
    def test_60(self):
        input = """
        Function: abc
        Body:
            x = -5 == -(s[4]) + -8;
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[],([],[Assign(Id('x'),BinaryOp('==',UnaryOp('-',IntLiteral(5)),BinaryOp('+',UnaryOp('-',ArrayCell(Id('s'),[IntLiteral(4)])),UnaryOp('-',IntLiteral(8)))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
    
    def test_61(self):
        input = """
        Function: abc
        Parameter: x, y, z[4][5]
        Body:
            If a Then
                If b Then
                EndIf.
                If c Then
                    If d Then
                        a = b;
                        If e Then
                            Do
                                f();
                            While (g)
                            EndDo.
                        EndIf.
                    EndIf.
                EndIf.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[4,5],None)],([],[If([(Id('a'),[],[If([(Id('b'),[],[])],None),If([(Id('c'),[],[If([(Id('d'),[],[Assign(Id('a'),Id('b')),If([(Id('e'),[],[Dowhile(([],[CallStmt(Id('f'),[])]),Id('g'))])],None)])],None)])],None)])],None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
    
    def test_62(self):
        input = """
        Function: abc
        Parameter: x, y, z[1][2]
        Body:
            For (a = 4, a == 100, f() + g()) Do
                i = i[1] + 1;
            EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[1,2],None)],([],[For(Id('a'),IntLiteral(4),BinaryOp('==',Id('a'),IntLiteral(100)),BinaryOp('+',CallExpr(Id('f'),[]),CallExpr(Id('g'),[])),([],[Assign(Id('i'),BinaryOp('+',ArrayCell(Id('i'),[IntLiteral(1)]),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
    
    def test_63(self):
        input = """
        Function: abc
        Parameter: x, y, z[4][5]
        Body:
            For (a = 4, a == 10, 1 + 2) Do
                If a == 4 Then a = 5;
                Do sth(); While (x == - -x) EndDo.
                EndIf.
            EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[4,5],None)],([],[For(Id('a'),IntLiteral(4),BinaryOp('==',Id('a'),IntLiteral(10)),BinaryOp('+',IntLiteral(1),IntLiteral(2)),([],[If([(BinaryOp('==',Id('a'),IntLiteral(4)),[],[Assign(Id('a'),IntLiteral(5)),Dowhile(([],[CallStmt(Id('sth'),[])]),BinaryOp('==',Id('x'),UnaryOp('-',UnaryOp('-',Id('x')))))])],None)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
    
    def test_64(self):
        input = """
        Function: abc
        Parameter: x, y, z[0x23][0o213]
        Body:
            Do
                a = z[0x123];
                b = z[1][0o2];
                Break;
                Continue;
            While False + True EndDo.
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[35,139],None)],([],[Dowhile(([],[Assign(Id('a'),ArrayCell(Id('z'),[IntLiteral(291)])),Assign(Id('b'),ArrayCell(Id('z'),[IntLiteral(1),IntLiteral(2)])),Break(),Continue()]),BinaryOp('+',BooleanLiteral(False),BooleanLiteral(True)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
    
    def test_65(self):
        input = """
        Var: a = 5;
        Var: b[2][3] = {{2,{{{3}}},4},{4,{{{{{{{{{{5}}}}}}}}}},6}};
        Var: c,d=6,e,f;
        Var: m,n[10];
        """
        expect = Program([VarDecl(Id('a'),[],IntLiteral(5)),VarDecl(Id('b'),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(3)])])]),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(5)])])])])])])])])])]),IntLiteral(6)])])),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],IntLiteral(6)),VarDecl(Id('e'),[],None),VarDecl(Id('f'),[],None),VarDecl(Id('m'),[],None),VarDecl(Id('n'),[10],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,365))
    
    def test_66(self):
        input = """
        Function: test
        Body:
            If a_function_call("Ronaldo") Then
                a = printf("It it #$%");
                b = a()[1] * 2.0;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('test'),[],([],[If([(CallExpr(Id('a_function_call'),[StringLiteral('''Ronaldo''')]),[],[Assign(Id('a'),CallExpr(Id('printf'),[StringLiteral('''It it #$%''')])),Assign(Id('b'),BinaryOp('*',ArrayCell(CallExpr(Id('a'),[]),[IntLiteral(1)]),FloatLiteral(2.0)))])],None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,366))
    
    def test_67(self):
        input = """
        Function: test
        Parameter: n
        Body:
            If n > 100 Then
                Return a;
            ElseIf n < 100 Then
                Return 100;
            Else
                Return 0;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('test'),[VarDecl(Id('n'),[],None)],([],[If([(BinaryOp('>',Id('n'),IntLiteral(100)),[],[Return(Id('a'))]),(BinaryOp('<',Id('n'),IntLiteral(100)),[],[Return(IntLiteral(100))])],([],[Return(IntLiteral(0))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,367))
    
    def test_68(self):
        input = """
        Function: main
        Body:
            Var: i[100] = {0};
            For (i = 1, i < 100, 5) Do
                writeln(i);
            EndFor.
            Return 0;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([VarDecl(Id('i'),[100],ArrayLiteral([IntLiteral(0)]))],[For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),IntLiteral(100)),IntLiteral(5),([],[CallStmt(Id('writeln'),[Id('i')])])),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,368))
    
    def test_69(self):
        input = """
        Function: test
        Parameter: arr
        Body:
            Return pop_back(arr);
        EndBody.
        Function: test1
        Parameter: arr
        Body:
            Return seek(arr);
        EndBody.
        """
        expect = Program([FuncDecl(Id('test'),[VarDecl(Id('arr'),[],None)],([],[Return(CallExpr(Id('pop_back'),[Id('arr')]))])),FuncDecl(Id('test1'),[VarDecl(Id('arr'),[],None)],([],[Return(CallExpr(Id('seek'),[Id('arr')]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,369))
    
    def test_70(self):
        input = """
        Function: main
        Parameter: buffer
        Body:
            Var: str;
            str = string_to_int(input());
            printLn(str);
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('buffer'),[],None)],([VarDecl(Id('str'),[],None)],[Assign(Id('str'),CallExpr(Id('string_to_int'),[CallExpr(Id('input'),[])])),CallStmt(Id('printLn'),[Id('str')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,370))
    
    def test_71(self):
        input = """
        Function: main
        Parameter: x
        Body:
            Var: i = 10, k[3][5] = {{{}}, {{1}}};
            Do
                Break;
                Return;
            While i <= 10 EndDo.
            Continue;
            Return 0;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([VarDecl(Id('i'),[],IntLiteral(10)),VarDecl(Id('k'),[3,5],ArrayLiteral([ArrayLiteral([ArrayLiteral([])]),ArrayLiteral([ArrayLiteral([IntLiteral(1)])])]))],[Dowhile(([],[Break(),Return(None)]),BinaryOp('<=',Id('i'),IntLiteral(10))),Continue(),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,371))
    
    def test_72(self):
        input = """
        Function: fibonaci
        Parameter: a, b
        Body:
            If (a % b == 0) Then
                Return b;
            Else
                Return fibonaci(b, a % b);
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('fibonaci'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([],[If([(BinaryOp('==',BinaryOp('%',Id('a'),Id('b')),IntLiteral(0)),[],[Return(Id('b'))])],([],[Return(CallExpr(Id('fibonaci'),[Id('b'),BinaryOp('%',Id('a'),Id('b'))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,372))
    
    def test_73(self):
        input = """
        Function: trivial
        Body:
            Var: a = 0.5, b = 2.5;
            While (a =/= b) Do
                a = a +. 1;
                b = b -. 1;
            EndWhile.
            Return 0;
        EndBody.
        """
        expect = Program([FuncDecl(Id('trivial'),[],([VarDecl(Id('a'),[],FloatLiteral(0.5)),VarDecl(Id('b'),[],FloatLiteral(2.5))],[While(BinaryOp('=/=',Id('a'),Id('b')),([],[Assign(Id('a'),BinaryOp('+.',Id('a'),IntLiteral(1))),Assign(Id('b'),BinaryOp('-.',Id('b'),IntLiteral(1)))])),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,373))
    
    def test_74(self):
        input = """
        Function: main
        Body:
            Var: x;
            x = f(1 + f[2]) + {1, {}} + f()[0x1] + True || False *. 2. \\. 3. + !2 && "PPL";
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([VarDecl(Id('x'),[],None)],[Assign(Id('x'),BinaryOp('&&',BinaryOp('||',BinaryOp('+',BinaryOp('+',BinaryOp('+',CallExpr(Id('f'),[BinaryOp('+',IntLiteral(1),ArrayCell(Id('f'),[IntLiteral(2)]))]),ArrayLiteral([IntLiteral(1),ArrayLiteral([])])),ArrayCell(CallExpr(Id('f'),[]),[IntLiteral(1)])),BooleanLiteral(True)),BinaryOp('+',BinaryOp('\\.',BinaryOp('*.',BooleanLiteral(False),FloatLiteral(2.0)),FloatLiteral(3.0)),UnaryOp('!',IntLiteral(2)))),StringLiteral('''PPL''')))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,374))
    
    def test_75(self):
        input = """
        Var: x = 0x45;
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(69))])
        self.assertTrue(TestAST.checkASTGen(input,expect,375))
    
    def test_76(self):
        input = """
        Var: y = True;
        """
        expect = Program([VarDecl(Id('y'),[],BooleanLiteral(True))])
        self.assertTrue(TestAST.checkASTGen(input,expect,376))
    
    def test_77(self):
        input = """
        Function: main
        Body:
            For(i = 0., foo(i) * main[10] == 0x45, {123}) Do
                x = 321;
            EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[For(Id('i'),FloatLiteral(0.0),BinaryOp('==',BinaryOp('*',CallExpr(Id('foo'),[Id('i')]),ArrayCell(Id('main'),[IntLiteral(10)])),IntLiteral(69)),ArrayLiteral([IntLiteral(123)]),([],[Assign(Id('x'),IntLiteral(321))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,377))
    
    def test_78(self):
        input = r"""
        Var: str = "abc\t\b";
        """
        expect = Program([VarDecl(Id('str'),[],StringLiteral(r'''abc\t\b'''))])
        self.assertTrue(TestAST.checkASTGen(input,expect,378))
    
    def test_79(self):
        input = """
        Function: main
        Body:
            Return a * b - (c + (d -. e + "ffff" <=. 1.5));
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(BinaryOp('-',BinaryOp('*',Id('a'),Id('b')),BinaryOp('+',Id('c'),BinaryOp('<=.',BinaryOp('+',BinaryOp('-.',Id('d'),Id('e')),StringLiteral('''ffff''')),FloatLiteral(1.5)))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,379))
    
    def test_80(self):
        input = """
        Var: a, b, c[2][3] = 2;
        Function: func
        Body:
            Return "Principles of Programing Language" + " 201";
        EndBody.
        Function: main
        Body:
            print(func());
            Return;
        EndBody.
        """
        expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[2,3],IntLiteral(2)),FuncDecl(Id('func'),[],([],[Return(BinaryOp('+',StringLiteral('''Principles of Programing Language'''),StringLiteral(''' 201''')))])),FuncDecl(Id('main'),[],([],[CallStmt(Id('print'),[CallExpr(Id('func'),[])]),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,380))
    
    def test_81(self):
        input = """
        Function: main
        Body:
            Var: i[10] = {0, 1, 2, 3, 9};
            For (i = 1, i < 10, i + 1) Do
                print(i);
            EndFor.
            Return 0;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([VarDecl(Id('i'),[10],ArrayLiteral([IntLiteral(0),IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(9)]))],[For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('+',Id('i'),IntLiteral(1)),([],[CallStmt(Id('print'),[Id('i')])])),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,381))
    
    def test_82(self):
        input = """
    
        """
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input,expect,382))
    
    def test_83(self):
        input = """
        Function: abc
        Body:
            x = 1 + 2 + 3;
            y = x +. 4 +. 1;
            z = y && False || True || nand(x, y);
            w = 4 - 3 - 3;
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[],([],[Assign(Id('x'),BinaryOp('+',BinaryOp('+',IntLiteral(1),IntLiteral(2)),IntLiteral(3))),Assign(Id('y'),BinaryOp('+.',BinaryOp('+.',Id('x'),IntLiteral(4)),IntLiteral(1))),Assign(Id('z'),BinaryOp('||',BinaryOp('||',BinaryOp('&&',Id('y'),BooleanLiteral(False)),BooleanLiteral(True)),CallExpr(Id('nand'),[Id('x'),Id('y')]))),Assign(Id('w'),BinaryOp('-',BinaryOp('-',IntLiteral(4),IntLiteral(3)),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,383))
    
    def test_84(self):
        input = """
        Function: nand
        Parameter: a, b
        Body:
            Return !(a && b);
        EndBody.
        """
        expect = Program([FuncDecl(Id('nand'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([],[Return(UnaryOp('!',BinaryOp('&&',Id('a'),Id('b'))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,384))
    
    def test_85(self):
        input = """
        Function: nor
        Parameter: a, b
        Body:
            Return !(a || b);
        EndBody.
        """
        expect = Program([FuncDecl(Id('nor'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([],[Return(UnaryOp('!',BinaryOp('||',Id('a'),Id('b'))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,385))
    
    def test_86(self):
        input = """
        Function: xor
        Parameter: a, b
        Body:
            Return (a || b) && !(a && b);
        EndBody.
        """
        expect = Program([FuncDecl(Id('xor'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([],[Return(BinaryOp('&&',BinaryOp('||',Id('a'),Id('b')),UnaryOp('!',BinaryOp('&&',Id('a'),Id('b')))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,386))
    
    def test_87(self):
        input = """
        Function: abc
        Body:
            x[1 + 2 + foo() + x[3 + 4 + 6]] = y[6 + 7];
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[],([],[Assign(ArrayCell(Id('x'),[BinaryOp('+',BinaryOp('+',BinaryOp('+',IntLiteral(1),IntLiteral(2)),CallExpr(Id('foo'),[])),ArrayCell(Id('x'),[BinaryOp('+',BinaryOp('+',IntLiteral(3),IntLiteral(4)),IntLiteral(6))]))]),ArrayCell(Id('y'),[BinaryOp('+',IntLiteral(6),IntLiteral(7))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,387))
    
    def test_88(self):
        input = r"""
        Var: clgt = "\b\f\r\n\t :D :D :D :)))";
        """
        expect = Program([VarDecl(Id('clgt'),[],StringLiteral(r'''\b\f\r\n\t :D :D :D :)))'''))])
        self.assertTrue(TestAST.checkASTGen(input,expect,388))
    
    def test_89(self):
        input = """
        Function: abc
        Body:
            x = -5 + -7 - -.7 + -.2 **skdljf** + -(-5 + 4) + x[5] + (foo() + goo())[5];
        EndBody.
        """
        expect = Program([FuncDecl(Id('abc'),[],([],[Assign(Id('x'),BinaryOp('+',BinaryOp('+',BinaryOp('+',BinaryOp('+',BinaryOp('-',BinaryOp('+',UnaryOp('-',IntLiteral(5)),UnaryOp('-',IntLiteral(7))),UnaryOp('-.',IntLiteral(7))),UnaryOp('-.',IntLiteral(2))),UnaryOp('-',BinaryOp('+',UnaryOp('-',IntLiteral(5)),IntLiteral(4)))),ArrayCell(Id('x'),[IntLiteral(5)])),ArrayCell(BinaryOp('+',CallExpr(Id('foo'),[]),CallExpr(Id('goo'),[])),[IntLiteral(5)])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,389))
    
    def test_90(self):
        input = """
        Var: x[1][2][3][4] = 5;
            Var: y[6][7] = 8, t = 9, f[3];
            Var: q,w,e,r,t,y;
        """
        expect = Program([VarDecl(Id('x'),[1,2,3,4],IntLiteral(5)),VarDecl(Id('y'),[6,7],IntLiteral(8)),VarDecl(Id('t'),[],IntLiteral(9)),VarDecl(Id('f'),[3],None),VarDecl(Id('q'),[],None),VarDecl(Id('w'),[],None),VarDecl(Id('e'),[],None),VarDecl(Id('r'),[],None),VarDecl(Id('t'),[],None),VarDecl(Id('y'),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,390))
    
    def test_91(self):
        input = """
        Function: main
        Body:
            x = "Hello world";
            print(x);
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(Id('x'),StringLiteral('''Hello world''')),CallStmt(Id('print'),[Id('x')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,391))
    
    def test_92(self):
        input = """
        Function: main
        Body:
            x = 1 - 2 + 4.0 * 0.5 \\ 6;
            y = 1.1 +. 3e4 -. 0.2 *. 1.1 \\. 3.14;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(Id('x'),BinaryOp('+',BinaryOp('-',IntLiteral(1),IntLiteral(2)),BinaryOp('\\',BinaryOp('*',FloatLiteral(4.0),FloatLiteral(0.5)),IntLiteral(6)))),Assign(Id('y'),BinaryOp('-.',BinaryOp('+.',FloatLiteral(1.1),FloatLiteral(30000.0)),BinaryOp('\\.',BinaryOp('*.',FloatLiteral(0.2),FloatLiteral(1.1)),FloatLiteral(3.14))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,392))
    
    def test_93(self):
        input = """
        Function: main
        Body:
            x = True || False && (3 + 5) || !!(4 \\. 2e3);
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(Id('x'),BinaryOp('||',BinaryOp('&&',BinaryOp('||',BooleanLiteral(True),BooleanLiteral(False)),BinaryOp('+',IntLiteral(3),IntLiteral(5))),UnaryOp('!',UnaryOp('!',BinaryOp('\.',IntLiteral(4),FloatLiteral(2000.0))))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,393))
    
    def test_94(self):
        input = """
        Function: qua_met_moi_roi
                Parameter: x, y, z[4][5]
                Body:
                    If y % x == z % 2 Then
                        x = 1;
                        t = 2;
                    ElseIf x % y == z % 3 Then
                        y = 3;
                        z = 4;
                    Else z = 5;
                    EndIf.
                EndBody.
        """
        expect = Program([FuncDecl(Id('qua_met_moi_roi'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[4,5],None)],([],[If([(BinaryOp('==',BinaryOp('%',Id('y'),Id('x')),BinaryOp('%',Id('z'),IntLiteral(2))),[],[Assign(Id('x'),IntLiteral(1)),Assign(Id('t'),IntLiteral(2))]),(BinaryOp('==',BinaryOp('%',Id('x'),Id('y')),BinaryOp('%',Id('z'),IntLiteral(3))),[],[Assign(Id('y'),IntLiteral(3)),Assign(Id('z'),IntLiteral(4))])],([],[Assign(Id('z'),IntLiteral(5))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,394))
    
    def test_95(self):
        input = """
        Function: toi_doi_bung
        Parameter: x, y, z[4][5]
        Body:
            Var: x;
            x = 5;
            x[1] = 6;
            x[2][3] = {2, 3};
        EndBody.
        """
        expect = Program([FuncDecl(Id('toi_doi_bung'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[4,5],None)],([VarDecl(Id('x'),[],None)],[Assign(Id('x'),IntLiteral(5)),Assign(ArrayCell(Id('x'),[IntLiteral(1)]),IntLiteral(6)),Assign(ArrayCell(Id('x'),[IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(2),IntLiteral(3)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,395))
    
    def test_96(self):
        input = """
        Function: main
        Body:
            For (i = 0, i < 10, 1) Do
                If (i % 2 == 0) Then Continue; EndIf.
                writeln(i);
            EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(1),([],[If([(BinaryOp('==',BinaryOp('%',Id('i'),IntLiteral(2)),IntLiteral(0)),[],[Continue()])],None),CallStmt(Id('writeln'),[Id('i')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,396))
    
    def test_97(self):
        input = """
        Var: x, y, z;
        Function: main
        Parameter: argc, argv
        Body:
            Var: n, s = 0;
            n = argc;
            initiate();
            For(i = 0, i < n, 1) Do
                s = s + argv[i];
            EndFor.
            print(s);
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[],None),FuncDecl(Id('main'),[VarDecl(Id('argc'),[],None),VarDecl(Id('argv'),[],None)],([VarDecl(Id('n'),[],None),VarDecl(Id('s'),[],IntLiteral(0))],[Assign(Id('n'),Id('argc')),CallStmt(Id('initiate'),[]),For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),Id('n')),IntLiteral(1),([],[Assign(Id('s'),BinaryOp('+',Id('s'),ArrayCell(Id('argv'),[Id('i')])))])),CallStmt(Id('print'),[Id('s')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,397))
    
    def test_98(self):
        input = """
        Var: x,y,z;
        Var: a,b,c;
        Function: foo1
        Body:
        EndBody.
        Function: foo2
        Body:
        EndBody.
        """
        expect = Program([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[],None),VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),FuncDecl(Id('foo1'),[],([],[])),FuncDecl(Id('foo2'),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_99(self):
        input = """
        Function: end_game
        Parameter: x, y, z[4][5]
        Body:
            Var: x;
            x = 5;
            x[1] = 6;
            x[2][3] = {2, 3};
        EndBody.
        """
        expect = Program([FuncDecl(Id('end_game'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[4,5],None)],([VarDecl(Id('x'),[],None)],[Assign(Id('x'),IntLiteral(5)),Assign(ArrayCell(Id('x'),[IntLiteral(1)]),IntLiteral(6)),Assign(ArrayCell(Id('x'),[IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(2),IntLiteral(3)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,399))