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
        raise UnterminatedComment(result.text)
    else:
        return result;
}

options{
	language=Python3;
}

program: (variable_declaration | function_declaration)+;

// for expression
expression: '(' expression ')'
            | call_statement
            | expression indices
            | (SUBTRACT | SUBTRACT_F) expression
            | NOT expression
            | expression (MULTIPLY | MULTIPLY_F | DIVIDE | DIVIDE_F | MODULO) expression
            | expression (ADD | ADD_F | SUBTRACT | SUBTRACT_F) expression
            | expression (AND | OR) expression
            | expression (EQUAL | NOT_EQUAL | LT | GT | LTE | GTE | NOT_EQUAL_F | LT_F | GT_F | LTE_F | GTE_F) expression
            | operands;
operands: literal | IDENTIFIER;

// for declaring variables
variable_declaration  : VAR COLON variable_initializer (COMMA variable_initializer)* SEMI;

variable_name: IDENTIFIER | ARRAY_NAME;
variable_initializer: variable_name (ASSIGN variable_value)?;

variable_value: expression | array_value_list;
array_value: variable_value (COMMA variable_value)*;
array_value_list: '{' array_value '}';

// for declaring functions
function_declaration: FUNCTION COLON IDENTIFIER parameters? BODY COLON statement_list? ENDBODY DOT;
parameters: PARAMETER COLON parameter_list;
parameter_list: variable_name (COMMA variable_name)*;

// for statements
statement: variable_declaration* post_statement;
post_statement: assignment
                |  if_statement
                |  for_statement
                |  while_statement
                |  do_while_statement
                |  break_statement
                |  continue_statement
                |  call_statement
                |  return_statement;
statement_list: statement+;

assignment: IDENTIFIER indices? ASSIGN expression SEMI;
indices: ('[' expression ']')+;

// if
if_statement: IF if_start elseif_statement* else_statement? ENDIF DOT;
if_start: expression THEN statement_list?;
elseif_statement: ELSEIF expression THEN statement_list?;
else_statement: ELSE statement_list?;

// for
for_statement: FOR '(' for_condition ')' DO statement_list? ENDFOR DOT;
for_condition: IDENTIFIER ASSIGN expression COMMA expressionn COMMA expression;

// while
while_statement: WHILE expression DO statement_list? ENDWHILE DOT;

// do-while
do_while_statement: DO statement_list? WHILE expression ENDDO DOT;\

// break
break_statement: BREAK SEMI;

// continue
continue_statement: CONTINUE SEMI;

// call
in_parameters: expression (COMMA expression)*;
call_statement: IDENTIFIER '(' in_parameters? ')';

// return
return_statement: RETURN expression SEMI;

literal: INTEGER | FLOAT | BOOLEAN | STRING;

SEMI: ';' ;
COMMA: ',';
COLON: ':' ;
DOT: '.';

// Keywords
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

// Operators
ASSIGN: '=';
SUBTRACT: '-';
SUBTRACT_F: '-.';
NOT: '!';
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

// White spaces
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


IDENTIFIER: [a-z] [_a-zA-Z0-9]*;
COMMENT: '**' .*? '**' -> skip;

// Data type

// boolean
BOOLEAN: ('True' | 'False');

// integer
INTEGER: DEC_INT | OCT_INT | HEX_INT;

// float
FLOAT: DIGIT+ (DEC_PART EXP_PART | DEC_PART | EXP_PART);

// string
STRING: '"' CHAR* '"'
{
    self.text = self.text[1: -1];
};

// array
ARRAY_NAME: IDENTIFIER ('[' INTEGER ']')+;

// Error
ERROR_CHAR: .;
ILLEGAL_ESCAPE: '"' CHAR* ILLEGAL_ESC
{
    self.text = self.text[1: ];
};
UNCLOSE_STRING: '"' CHAR*
{
    self.text = self.text[1:];
};
UNTERMINATED_COMMENT: '**' .*? '*'?;

fragment DIGIT: [0-9];
fragment OCT_DIGIT: [0-7];
fragment HEX_DIGIT: [0-9A-F];
fragment DEC_INT: [1-9] DIGIT* | '0'+;
fragment HEX_INT: '0' [xX] HEX_DIGIT+;
fragment OCT_INT: '0' [oO] OCT_DIGIT+;
fragment DEC_PART: '.' DIGIT*;
fragment EXP_PART: [eE] ('+' | '-')? DIGIT+;
fragment ILLEGAL_ESC: ('\\' ~[bfrnt'\\] | '\\');
fragment CHAR: ('\'"' | '\\' [btnfr'\\] | ~[\r\n\\"]);