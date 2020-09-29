# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3=")
        buf.write("!\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\5\3\20\n\3\3\3\3\3\3\3\3\3\5\3\26\n\3\7\3\30\n\3\f\3")
        buf.write("\16\3\33\13\3\3\3\3\3\3\4\3\4\3\4\2\2\5\2\4\6\2\3\4\2")
        buf.write("\63\6489\2 \2\b\3\2\2\2\4\n\3\2\2\2\6\36\3\2\2\2\b\t\5")
        buf.write("\4\3\2\t\3\3\2\2\2\n\13\7\30\2\2\13\f\7\5\2\2\f\17\7\61")
        buf.write("\2\2\r\16\7%\2\2\16\20\5\6\4\2\17\r\3\2\2\2\17\20\3\2")
        buf.write("\2\2\20\31\3\2\2\2\21\22\7\4\2\2\22\25\7\61\2\2\23\24")
        buf.write("\7%\2\2\24\26\5\6\4\2\25\23\3\2\2\2\25\26\3\2\2\2\26\30")
        buf.write("\3\2\2\2\27\21\3\2\2\2\30\33\3\2\2\2\31\27\3\2\2\2\31")
        buf.write("\32\3\2\2\2\32\34\3\2\2\2\33\31\3\2\2\2\34\35\7\3\2\2")
        buf.write("\35\5\3\2\2\2\36\37\t\2\2\2\37\7\3\2\2\2\5\17\25\31")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "':'", "'Body'", "'Break'", 
                     "'Continue'", "'Do'", "'Else'", "'ElseIf'", "'EndBody'", 
                     "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
                     "'If'", "'Parameter'", "'Return'", "'Then'", "'While'", 
                     "'EndDo'", "'Var'", "'-'", "'-.'", "'!'", "'*'", "'*.'", 
                     "'\\'", "'\\.'", "'%'", "'+'", "'+.'", "'&&'", "'||'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", 
                     "'<.'", "'>.'", "'<=.'", "'>=.'" ]

    symbolicNames = [ "<INVALID>", "SEMI", "COMMA", "COLON", "BODY", "BREAK", 
                      "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", 
                      "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                      "RETURN", "THEN", "WHILE", "ENDDO", "VAR", "SUBTRACT", 
                      "SUBTRACT_F", "NEGATION", "MULTIPLY", "MULTIPLY_F", 
                      "DIVIDE", "DIVIDE_F", "MODULO", "ADD", "ADD_F", "AND", 
                      "OR", "EQUAL", "NOT_EQUAL", "LT", "GT", "LTE", "GTE", 
                      "NOT_EQUAL_F", "LT_F", "GT_F", "LTE_F", "GTE_F", "WS", 
                      "IDENTIFIER", "COMMENT", "BOOLEAN", "INTEGER", "DEC_INT", 
                      "HEX_INT", "OCT_INT", "FLOAT", "STRING", "ERROR_CHAR", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_declaration_variable = 1
    RULE_literal = 2

    ruleNames =  [ "program", "declaration_variable", "literal" ]

    EOF = Token.EOF
    SEMI=1
    COMMA=2
    COLON=3
    BODY=4
    BREAK=5
    CONTINUE=6
    DO=7
    ELSE=8
    ELSEIF=9
    ENDBODY=10
    ENDIF=11
    ENDFOR=12
    ENDWHILE=13
    FOR=14
    FUNCTION=15
    IF=16
    PARAMETER=17
    RETURN=18
    THEN=19
    WHILE=20
    ENDDO=21
    VAR=22
    SUBTRACT=23
    SUBTRACT_F=24
    NEGATION=25
    MULTIPLY=26
    MULTIPLY_F=27
    DIVIDE=28
    DIVIDE_F=29
    MODULO=30
    ADD=31
    ADD_F=32
    AND=33
    OR=34
    EQUAL=35
    NOT_EQUAL=36
    LT=37
    GT=38
    LTE=39
    GTE=40
    NOT_EQUAL_F=41
    LT_F=42
    GT_F=43
    LTE_F=44
    GTE_F=45
    WS=46
    IDENTIFIER=47
    COMMENT=48
    BOOLEAN=49
    INTEGER=50
    DEC_INT=51
    HEX_INT=52
    OCT_INT=53
    FLOAT=54
    STRING=55
    ERROR_CHAR=56
    ILLEGAL_ESCAPE=57
    UNCLOSE_STRING=58
    UNTERMINATED_COMMENT=59

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_variable(self):
            return self.getTypedRuleContext(BKITParser.Declaration_variableContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.declaration_variable()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_variableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.IDENTIFIER)
            else:
                return self.getToken(BKITParser.IDENTIFIER, i)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.EQUAL)
            else:
                return self.getToken(BKITParser.EQUAL, i)

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.LiteralContext)
            else:
                return self.getTypedRuleContext(BKITParser.LiteralContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_declaration_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_variable" ):
                return visitor.visitDeclaration_variable(self)
            else:
                return visitor.visitChildren(self)




    def declaration_variable(self):

        localctx = BKITParser.Declaration_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(BKITParser.VAR)
            self.state = 9
            self.match(BKITParser.COLON)
            self.state = 10
            self.match(BKITParser.IDENTIFIER)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.EQUAL:
                self.state = 11
                self.match(BKITParser.EQUAL)
                self.state = 12
                self.literal()


            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 15
                self.match(BKITParser.COMMA)
                self.state = 16
                self.match(BKITParser.IDENTIFIER)
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKITParser.EQUAL:
                    self.state = 17
                    self.match(BKITParser.EQUAL)
                    self.state = 18
                    self.literal()


                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(BKITParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKITParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKITParser.STRING, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKITParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.BOOLEAN) | (1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





