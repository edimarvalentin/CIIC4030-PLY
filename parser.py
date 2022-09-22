#Author: Edimar Valentin Kery <edimar.valentin@upr.edu>

import ply.yacc as yacc

from lexical-analyzer import tokens

#factor -> NUM
def p_term_factor(p):
    'factor: NUM'
    p[0] = p[1]

#factor -> ID
def p_factor_id(p):
    'factor: ID'
    p[0] = p[1]

#term -> factor
def p_term_factor(p):
    'term: factor'
    p[0] = p[1]

#term -> term STAR factor
def p_term_star(p):
    'term: term STAR factor'
    p[0] = p[1] * p[3]

#term -> term SLASH factor
def p_term_slash(p):
    'term: term SLASH factor'
    p[0] = p[1] / p[3]

#term -> term PCT factor
def p_term_pct(p):
    'term: term PCT factor'
    p[0] = p[1] % p[3]

#factor -> LPAREN expr RPAREN
def p_factor_lparen_expr_rparen(p):
    'factor: LPAREN expr RPAREN'
    p[0] = p[2]

#expr -> term
def p_expr_term(p):
    'expr: term'
    p[0] = p[1]

#expr -> expr  PLUS term
def p_expr_plus_term(p):
    'expr: expr PLUS term'
    p[0] = p[1] + p[3]

#expr -> expr MINUS term
def p_expr_minus_term(p):
    'expr: expr MINUS term'
    p[0] = p[1] - p[3]

#expr -> IF LPAREN test RPAREN LBRACE expras RBRACE ELSE LBRACE expras RBRACE
def p_if_

#argsopt - >
def p_argspot(p):
    'argspot:'
    pass

#args -> expr
def p_args_expr(p):
    'args: expr'
    p[0] = p[1]

#args -> expr COMMA args
def p_expr_comma_args(p):
    'expr: expr COMMA args'
    pass

#argsopt -> args
def p_argsopt_args(p):
    'argsopt: args'
    p[0] = p[1]

#factor -> factor LPAREN argsopt RPAREN
def p_factor_argsopt(p):
    'factor: factor LPAREN argsopt RPAREN'
    pass

#parmsopt -> parms
