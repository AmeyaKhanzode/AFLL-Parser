import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'EQUALS',
    'IDENTIFIER',
    'IF',
    'ELSE',
    'LESS',
    'GREATER',
    'COLON'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_LESS = r'<'
t_GREATER = r'>'
t_COLON = r':'
t_ignore = ' \t'

reserved = {
    'if': 'IF',
    'else': 'ELSE'
}


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)


def p_statement_assignment(p):
    'statement : IDENTIFIER EQUALS expression'
    p[0] = ("assign", p[1], p[3])


def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = (p[1], p[2], p[3])  # Return the expression as a tuple


def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]


def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = ("variable", p[1])


def p_expression_parens(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]


def p_expression_comparison(p):
    '''expression : expression LESS expression
                  | expression GREATER expression'''
    p[0] = (p[1], p[2], p[3])  # Return comparison as a tuple


def p_if_else_statement(p):
    '''statement : IF expression COLON statement
                 | IF expression COLON statement ELSE COLON statement'''
    if len(p) == 5:
        p[0] = ("if", p[2], p[4])
    else:
        p[0] = ("if_else", p[2], p[4], p[7])


def p_statement_sequence(p):
    '''statement : statement statement'''
    p[0] = p[1]  # Just return the first statement for now


def p_error(p):
    print("Syntax error")


parser = yacc.yacc()

data1 = "x = 10"
data2 = "if x < 10: x = x + 1"
data3 = "if x < 10: x = x + 1 else: x = x - 1"
data4 = "if x > 5: y = y + 2 else: y = y - 2"
data5 = "if 5 < 10: z = 3 + 7 else: z = 5 - 2"
data6 = "if (x < 20): x = 15 else: x = 5"
data7 = "if y > 0: x = x + 1 else: x = x - 1"

print(parser.parse(data1))
print(parser.parse(data2))
print(parser.parse(data3))
print(parser.parse(data4))
print(parser.parse(data5))
print(parser.parse(data6))
print(parser.parse(data7))
