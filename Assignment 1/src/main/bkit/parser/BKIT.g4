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

program: variable_declaration* function_declaration* EOF;

// for expression
//expression: ORB expression CRB
//            | call_function
//            | expression indices
//            | <assoc = right> (SUBTRACT | SUBTRACT_F) expression
//            | <assoc = right> NOT expression
//            | expression (MULTIPLY | MULTIPLY_F | DIVIDE | DIVIDE_F | MODULO) expression
//            | expression (ADD | ADD_F | SUBTRACT | SUBTRACT_F) expression
//            | expression (AND | OR) expression
//            | expression (EQUAL | NOT_EQUAL | LT | GT | LTE | GTE | NOT_EQUAL_F | LT_F | GT_F | LTE_F | GTE_F) expression
//            | operands | array_value_list_assign;
operands: literal | IDENTIFIER;

// expression: variable_value;
 expression: exp1 (EQUAL | NOT_EQUAL | LT | GT | LTE | GTE | NOT_EQUAL_F | LT_F | GT_F | LTE_F | GTE_F) exp1 | exp1;
 exp1: exp1 (AND | OR) exp2 | exp2;
 exp2: exp2 (ADD | ADD_F | SUBTRACT | SUBTRACT_F) exp3 | exp3;
 exp3: exp3 (MULTIPLY | MULTIPLY_F | DIVIDE | DIVIDE_F | MODULO) exp4 | exp4;
 exp4: exp5 | NOT exp5;
 exp5: exp6 | (SUBTRACT | SUBTRACT_F) exp6;
 exp6: exp7 | exp7 indices;
 exp7: exp8 | call_function;
 exp8: ORB expression CRB | operands | array_value_list_assign;

// for declaring variables
variable_declaration  : VAR COLON variable_initializer (COMMA variable_initializer)* SEMI;
array_name: IDENTIFIER (OSB INTEGER CSB)+;
variable_name: IDENTIFIER | array_name;
variable_initializer: variable_name (ASSIGN variable_value)?;

variable_value: INTEGER | FLOAT | STRING | array_value_list;
array_value: variable_value (COMMA variable_value)*;
array_value_list: OCB array_value CCB | OCB CCB;

variable_value_assign: expression | array_value_list_assign;
array_value_assign: variable_value_assign (COMMA variable_value_assign)*;
array_value_list_assign: OCB array_value_assign CCB | OCB CCB;

// for declaring functions
function_declaration: FUNCTION COLON IDENTIFIER parameters? BODY COLON statement_list ENDBODY DOT;
// function_main: FUNCTION COLON MAIN parameters? BODY COLON statement_list ENDBODY DOT;
parameters: PARAMETER COLON parameter_list;
parameter_list: variable_name (COMMA variable_name)*;


// for statements
statement: variable_declaration* post_statement*;
post_statement: assignment
                |  if_statement
                |  for_statement
                |  while_statement
                |  do_while_statement
                |  break_statement
                |  continue_statement
                |  call_statement
                |  return_statement;
statement_list: statement;

assignment: IDENTIFIER indices? ASSIGN expression SEMI;
indices: (OSB expression CSB)+;

// if
if_statement: IF if_start elseif_statement* else_statement? ENDIF DOT;
if_start: expression THEN statement_list;
elseif_statement: ELSEIF expression THEN statement_list;
else_statement: ELSE statement_list;

// for
for_statement: FOR ORB for_condition CRB DO statement_list ENDFOR DOT;
for_condition: IDENTIFIER ASSIGN expression COMMA expression COMMA expression;

// while
while_statement: WHILE expression statement_list ENDWHILE DOT;

// do-while
do_while_statement: DO statement_list WHILE expression ENDDO DOT;

// break
break_statement: BREAK SEMI;

// continue
continue_statement: CONTINUE SEMI;

// call
in_parameters: expression (COMMA expression)*;
call_function: IDENTIFIER ORB in_parameters? CRB;
call_statement: call_function SEMI;

// return
return_statement: RETURN expression? SEMI;

literal: INTEGER | FLOAT | BOOLEAN | STRING;

// seperators
SEMI: ';' ;
COMMA: ',';
COLON: ':' ;
DOT: '.';
OSB: '[';
CSB: ']';
ORB: '(';
CRB: ')';
OCB: '{';
CCB: '}';

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
// MAIN: 'main';

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

// Built-in functions
// PRINT: 'print';
// PRINTLN: 'printLn';
// PRINTSTRLN: 'printStrLn';
// READ: 'read';

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
FLOAT: DEC_INT (DEC_PART EXP_PART | DEC_PART | EXP_PART);

// string
STRING: '"' CHAR* '"'
{
    self.text = self.text[1: -1];
};

// Error
ERROR_CHAR: .;
ILLEGAL_ESCAPE: '"' CHAR* ILLEGAL_ESC
{
    self.text = self.text[1: ];
};
UNCLOSE_STRING: '"' CHAR* ('\n' | EOF)
{
    if self.text[-1] == '\n':
        self.text = self.text[1: -1];
    else:
        self.text = self.text[1: ];
};
UNTERMINATED_COMMENT: '**' .*? '*'?;

fragment DIGIT: [0-9];
fragment OCT_DIGIT: [0-7];
fragment HEX_DIGIT: [0-9A-F];
fragment DEC_INT: [1-9] DIGIT* | '0'+;
fragment HEX_INT: '0' [xX] [1-9A-F] HEX_DIGIT*;
fragment OCT_INT: '0' [oO] [1-7] OCT_DIGIT*;
fragment DEC_PART: '.' DIGIT*;
fragment EXP_PART: [eE] ('+' | '-')? DIGIT+;
fragment ILLEGAL_ESC: ('\\' ~[bfrnt'\\] | '\\' | '\'');
fragment CHAR: ('\'"' | '\\' [btnfr'\\] | ~['\r\n\\"]);