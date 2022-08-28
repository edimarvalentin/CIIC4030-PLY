import ply.lex as lex

#List of token names

tokens = ('ID', 'DEF', 'VAR', 'INT', 'IF', 'ELSE', 
	'NUM', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 
	'BECOMES', 'EQ', 'NE', 'LT', 'GT', 'LE', 'GE', 
	'PLUS', 'MINUS', 'STAR', 'SLASH', 'PCT', 'COMMA',
	'SEMMI', 'COLON', 'ARROW', 'COMMENT', 'WHITESPACE')

#REGEX rules for simple tokens

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
