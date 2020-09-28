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
        buf.write("\n\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\2\2\3\2\2\2\2\b\2\4")
        buf.write("\3\2\2\2\4\5\7\30\2\2\5\6\7\5\2\2\6\7\7\61\2\2\7\b\7\4")
        buf.write("\2\2\b\3\3\2\2\2\2")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "';'", "':'", "'Body'", "'Break'", 
                     "'Continue'", "'Do'", "'Else'", "'ElseIf'", "'EndBody'", 
                     "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
                     "'If'", "'Parameter'", "'Return'", "'Then'", "'While'", 
                     "'EndDo'", "'Var'", "'-'", "'-.'", "'!'", "'*'", "'*.'", 
                     "'\\'", "'\\.'", "'%'", "'+'", "'+.'", "'&&'", "'||'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", 
                     "'<.'", "'>.'", "'<=.'", "'>=.'" ]

    symbolicNames = [ "<INVALID>", "ID", "SEMI", "COLON", "BODY", "BREAK", 
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

    RULE_declaration = 0

    ruleNames =  [ "declaration" ]

    EOF = Token.EOF
    ID=1
    SEMI=2
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




    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = BKITParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(BKITParser.VAR)
            self.state = 3
            self.match(BKITParser.COLON)
            self.state = 4
            self.match(BKITParser.IDENTIFIER)
            self.state = 5
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





