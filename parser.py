#Author: Edimar Valentin Kery <edimar.valentin@upr.edu>

import ply.yacc as yacc

from lexi import tokens

#defdefs -> defdef defdefs
def p_defdefs_defdef_defdefs(p):
    'defdefs : defdef defdefs'
    pass

#defdefs -> defdef
def p_defdefs_defdef(p):
    'defdefs : defdef'
    p[0] = p[1]

#defdef -> DEF ID LPAREN parmsopt RPAREN COLON type BECOMES LBRACE vardefsopt defdefsopt expras RBRACE
def p_defdef_def_id(p):
    'defdef : DEF ID LPAREN parmsopt RPAREN COLON type BECOMES LBRACE vardefsopt defdefsopt expras RBRACE'
    pass

#parmsopt -> parms
def p_parmsopt_parms(p):
    'parmsopt : parms'
    pass

#parmsopt ->
def p_parmsopt(p):
    'parmsopt :'
    pass

#parms -> vardef COMMA parms
def p_parms_vardef_comma_parms(p):
    'parms : vardef COMMA parms'
    pass

#parms -> vardef
def p_parms_vardef(p):
    'parms : vardef'
    p[0] = p[1]

#vardef -> ID COLON type
def p_vardef_id_colon_type(p):
    'vardef : ID COLON type'
    pass

#type -> INT
def p_type_int(p):
    'type : INT'
    p[0] = p[1]

#type -> LPAREN typesopt RPAREN ARROW type
def p_type_laparen_typesopt_rparen_arrow_type(p):
    'type : LPAREN typesopt RPAREN ARROW type'
    pass

#typesopt -> types
def p_typesopt_types(p):
    'typesopt : types'
    p[0] = p[1]

#typesopt ->
def p_typesopt(p):
    'typesopt :'
    pass

#types -> type COMMA types
def p_types_type_COMMA_types(p):
    'types : type COMMA types'
    pass

#types -> type
def p_types_type(p):
    'types : type'
    p[0] = p[1]

#vardefsopt ->  VAR vardef SEMI vardefsopt
def p_vardefsopt_var_vardef_semi_vardefsopt(p):
    'vardefsopt : VAR vardef SEMI vardefsopt'
    pass

#vardefsopt -> 
def p_vardefsopt(p):
    'vardefsopt :'
    pass

#defdefsopt -> defdefs
def p_defdefsopt_defdef(p):
    'defdefsopt : defdefs'
    pass

#defdefsopt ->
def p_defdefsopt(p):
    'defdefsopt :'
    pass

#expras -> expra SEMI expras
def p_expras_expra_semi_expras(p):
    'expras : expra SEMI expras'
    pass

#expras -> expra
def p_expras_expra(p):
    'expras : expra'
    p[0] = p[1]

#expra -> ID BECOMES expr
def p_expra_id_becomes_expr(p):
    'expra : ID BECOMES expr'
    pass

#expra -> expr
def p_expra_expr(p):
    'expra : expr'
    p[0] = p[1]

#expr -> IF LPAREN test RPAREN LBRACE expras RBRACE ELSE LBRACE expras RBRACE
def p_expr_if_lparen_test(p):
    'expr : IF LPAREN test RPAREN LBRACE expras RBRACE ELSE LBRACE expras RBRACE'
    pass

#expr -> term
def p_expr_term(p):
    'expr : term'
    p[0] = p[1]

#expr -> expr  PLUS term
def p_expr_plus_term(p):
    'expr : expr PLUS term'
    p[0] = p[1] + p[3]

#expr -> expr MINUS term
def p_expr_minus_term(p):
    'expr : expr MINUS term'
    p[0] = p[1] - p[3]

#term -> factor
def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

#term -> term STAR factor
def p_term_star(p):
    'term : term STAR factor'
    p[0] = p[1] * p[3]

#term -> term SLASH factor
def p_term_slash(p):
    'term : term SLASH factor'
    p[0] = p[1] / p[3]

#term -> term PCT factor
def p_term_pct(p):
    'term : term PCT factor'
    p[0] = p[1] % p[3]

#factor -> ID
def p_factor_id(p):
    'factor : ID'
    p[0] = p[1]

#factor -> NUM
def p_factor_num(p):
    'factor : NUM'
    p[0] = p[1]

#factor -> LPAREN expr RPAREN
def p_factor_lparen_expr_rparen(p):
    'factor : LPAREN expr RPAREN'
    p[0] = p[2]

#factor -> factor LPAREN argsopt RPAREN
def p_factor_factor_lparen_argsopt_rparen(p):
    'factor : factor LPAREN argsopt RPAREN'
    pass

#test -> expr NE expr
def p_test_expr_ne_expr(p):
    'test : expr NE expr'
    p[0] = p[1] != p[3]

#test -> expr LT expr
def p_test_expr_lt_expr(p):
    'test : expr LT expr'
    p[0] = p[1] < p[3]

#test -> expr LE expr
def p_test_expr_le_expr(p):
    'test : expr LE expr'
    p[0] = p[1] <= p[3]

#test -> expr GE expr
def p_test_expr_ge_expr(p):
    'test : expr GE expr'
    p[0] = p[1] >= p[3]

#test -> expr GT expr
def p_test_expr_gt_expr(p):
    'test : expr GT expr'
    p[0] = p[1] > p[3]

#test -> expr EQ expr
def p_test_expr_eq_expr(p):
    'test : expr EQ expr'
    p[0] = p[1] == p[3]

#argsopt -> args
def p_argsopt_args(p):
    'argsopt : args'
    p[0] = p[1]

#argsopt - >
def p_argspot(p):
    'argsopt :'
    pass

#args -> expr COMMA args
def p_expr_comma_args(p):
    'expr : expr COMMA args'
    pass

#args -> expr
def p_args_expr(p):
    'args : expr'
    p[0] = p[1]

#Error rule for syntax errors
def p_error(p):
    print("Syntax error")

#Build parser
parser = yacc.yacc()

while True:
    try:
        s = input('calc >')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
