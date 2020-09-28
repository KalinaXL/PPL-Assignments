grammar BKIT;

@lexer::header {
# ID: 1813085
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

declaration  : VAR COLON IDENTIFIER SEMI;



ID: [a-z]+ ;

SEMI: ';' ;

COLON: ':' ;

BODY: 'Body';
BREAK: 'Break';
CONTINUE: 'Continue';
DO: 'Do';
ELSE: 'Else';
ELSEIF: 'ElseIf';
ENDBODY: 'EndBody';
ENDIF: 'EndIf';
ENDFOR: 'EndFor';
ENDWHILE: 'EndWhile';
FOR: 'For';
FUNCTION: 'Function';
IF: 'If';
PARAMETER: 'Parameter';
RETURN: 'Return';
THEN: 'Then';
WHILE: 'While';
ENDDO: 'EndDo';
VAR: 'Var' ;

SUBTRACT: '-';
SUBTRACT_F: '-.';
NEGATION: '!';
MULTIPLY: '*';
MULTIPLY_F: '*.';
DIVIDE: '\\';
DIVIDE_F: '\\.';
MODULO: '%';
ADD: '+';
ADD_F: '+.';
AND: '&&';
OR: '||';
EQUAL: '==';
NOT_EQUAL: '!=';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';
NOT_EQUAL_F: '=/=';
LT_F: '<.';
GT_F: '>.';
LTE_F: '<=.';
GTE_F: '>=.';




WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


IDENTIFIER: [a-z] [_a-zA-Z0-9]*;
COMMENT: '**' .*? '**' -> skip;
BOOLEAN: ('True' | 'False');
INTEGER: DEC_INT | OCT_INT | HEX_INT;
DEC_INT: [1-9] DIGIT* | '0'+;
HEX_INT: '0' [xX] HEX_DIGIT+;
OCT_INT: '0' [oO] OCT_DIGIT+;

FLOAT: DIGIT+ (DEC_PART EXP_PART | DEC_PART | EXP_PART);

STRING: '"' CHAR* '"'
{
    self.text = self.text[1: -1];
};
ERROR_CHAR: ~ [_a-zA-Z0-9] | '\\' ~[bfrnt'\\];
ILLEGAL_ESCAPE: '"' CHAR* ILLEGAL_ESC
{
    self.text = self.text[1: ];
};
UNCLOSE_STRING: '"' CHAR*
{
    self.text = self.text[1:];
};
UNTERMINATED_COMMENT: .;

fragment DIGIT: [0-9];
fragment OCT_DIGIT: [0-7];
fragment HEX_DIGIT: [0-9A-F];
fragment DEC_PART: '.' DIGIT*;
fragment EXP_PART: [eE] ('+' | '-')? DIGIT+;
fragment ILLEGAL_ESC: ('\\' ~[bfrnt'\\] | '\\');
fragment CHAR: ('\'"' | '\\' [btnfr'\\] | ~[\r\n\\"]);