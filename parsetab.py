
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ARROW BECOMES COLON COMMA COMMENT DEF ELSE EQ GE GT ID IF INT LBRACE LE LPAREN LT MINUS NE NUM PCT PLUS RBRACE RPAREN SEMI SLASH STAR VAR WHITESPACEdefdefs : defdef defdefsdefdefs : defdefdefdef : DEF ID LPAREN parmsopt RPAREN COLON type BECOMES LBRACE vardefsopt defdefsopt expras RBRACEparmsopt : parmsparmsopt :parms : vardef COMMA parmsparms : vardefvardef : ID COLON typetype : INTtype : LPAREN typesopt RPAREN ARROW typetypesopt : typestypesopt :types : type COMMA typestypes : typevardefsopt : VAR vardef SEMI vardefsoptvardefsopt :defdefsopt : defdefsdefdefsopt :expras : expra SEMI exprasexpras : expraexpra : ID BECOMES exprexpra : exprexpr : IF LPAREN test RPAREN LBRACE expras RBRACE ELSE LBRACE expras RBRACEexpr : termexpr : expr PLUS termexpr : expr MINUS termterm : factorterm : term STAR factorterm : term SLASH factorterm : term PCT factorfactor : IDfactor : NUMfactor : LPAREN expr RPARENfactor : factor LPAREN argsopt RPARENtest : expr NE exprtest : expr LT exprtest : expr LE exprtest : expr GE exprtest : expr GT exprtest : expr EQ exprargsopt : argsargsopt :expr : expr COMMA argsargs : expr'
    
_lr_action_items = {'DEF':([0,2,28,30,44,48,58,],[3,3,-16,3,-16,-3,-15,]),'$end':([1,2,4,48,],[0,-2,-1,-3,]),'ID':([2,3,4,6,13,28,30,31,32,33,36,44,45,48,49,50,51,52,53,54,55,56,57,58,74,75,76,77,78,79,81,91,],[-2,5,-1,7,7,-16,-18,7,35,-17,47,-16,47,-3,35,47,47,47,47,47,47,47,47,-15,47,47,47,47,47,47,35,35,]),'IF':([2,4,28,30,32,33,36,44,45,48,49,52,53,57,58,74,75,76,77,78,79,81,91,],[-2,-1,-16,-18,40,-17,40,-16,40,-3,40,40,40,40,-15,40,40,40,40,40,40,40,40,]),'NUM':([2,4,28,30,32,33,36,44,45,48,49,50,51,52,53,54,55,56,57,58,74,75,76,77,78,79,81,91,],[-2,-1,-16,-18,43,-17,43,-16,43,-3,43,43,43,43,43,43,43,43,43,-15,43,43,43,43,43,43,43,43,]),'LPAREN':([2,4,5,11,16,17,24,26,28,30,32,33,35,36,40,42,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,60,68,69,70,74,75,76,77,78,79,80,81,91,],[-2,-1,6,16,16,16,16,16,-16,-18,36,-17,-31,36,53,57,-32,-16,36,-31,-3,36,36,36,36,36,36,36,36,36,-15,-33,57,57,57,36,36,36,36,36,36,-34,36,36,]),'RPAREN':([6,8,9,10,14,15,16,18,19,20,21,27,29,41,42,43,46,47,57,60,62,63,64,65,66,68,69,70,71,72,80,82,83,84,85,86,87,93,],[-5,12,-4,-7,-8,-9,-12,-6,23,-14,-11,-13,-10,-24,-27,-32,60,-31,-42,-33,-25,-26,-44,-43,73,-28,-29,-30,80,-41,-34,-35,-36,-37,-38,-39,-40,-23,]),'COLON':([7,12,],[11,17,]),'COMMA':([10,14,15,20,29,35,39,41,42,43,46,47,59,60,62,63,64,65,67,68,69,70,80,82,83,84,85,86,87,93,],[13,-8,-9,24,-10,-31,52,-24,-27,-32,52,-31,52,-33,-25,-26,52,-43,52,-28,-29,-30,-34,52,52,52,52,52,52,-23,]),'INT':([11,16,17,24,26,],[15,15,15,15,15,]),'SEMI':([14,15,29,34,35,38,39,41,42,43,47,59,60,62,63,64,65,68,69,70,80,93,],[-8,-9,-10,44,-31,49,-22,-24,-27,-32,-31,-21,-33,-25,-26,-44,-43,-28,-29,-30,-34,-23,]),'BECOMES':([15,22,29,35,],[-9,25,-10,45,]),'ARROW':([23,],[26,]),'LBRACE':([25,73,90,],[28,81,91,]),'VAR':([28,44,],[31,31,]),'STAR':([35,41,42,43,47,60,62,63,68,69,70,80,],[-31,54,-27,-32,-31,-33,54,54,-28,-29,-30,-34,]),'SLASH':([35,41,42,43,47,60,62,63,68,69,70,80,],[-31,55,-27,-32,-31,-33,55,55,-28,-29,-30,-34,]),'PCT':([35,41,42,43,47,60,62,63,68,69,70,80,],[-31,56,-27,-32,-31,-33,56,56,-28,-29,-30,-34,]),'PLUS':([35,39,41,42,43,46,47,59,60,62,63,64,65,67,68,69,70,80,82,83,84,85,86,87,93,],[-31,50,-24,-27,-32,50,-31,50,-33,-25,-26,50,-43,50,-28,-29,-30,-34,50,50,50,50,50,50,-23,]),'MINUS':([35,39,41,42,43,46,47,59,60,62,63,64,65,67,68,69,70,80,82,83,84,85,86,87,93,],[-31,51,-24,-27,-32,51,-31,51,-33,-25,-26,51,-43,51,-28,-29,-30,-34,51,51,51,51,51,51,-23,]),'RBRACE':([35,37,38,39,41,42,43,47,59,60,61,62,63,64,65,68,69,70,80,88,92,93,],[-31,48,-20,-22,-24,-27,-32,-31,-21,-33,-19,-25,-26,-44,-43,-28,-29,-30,-34,89,93,-23,]),'NE':([41,42,43,47,60,62,63,64,65,67,68,69,70,80,93,],[-24,-27,-32,-31,-33,-25,-26,-44,-43,74,-28,-29,-30,-34,-23,]),'LT':([41,42,43,47,60,62,63,64,65,67,68,69,70,80,93,],[-24,-27,-32,-31,-33,-25,-26,-44,-43,75,-28,-29,-30,-34,-23,]),'LE':([41,42,43,47,60,62,63,64,65,67,68,69,70,80,93,],[-24,-27,-32,-31,-33,-25,-26,-44,-43,76,-28,-29,-30,-34,-23,]),'GE':([41,42,43,47,60,62,63,64,65,67,68,69,70,80,93,],[-24,-27,-32,-31,-33,-25,-26,-44,-43,77,-28,-29,-30,-34,-23,]),'GT':([41,42,43,47,60,62,63,64,65,67,68,69,70,80,93,],[-24,-27,-32,-31,-33,-25,-26,-44,-43,78,-28,-29,-30,-34,-23,]),'EQ':([41,42,43,47,60,62,63,64,65,67,68,69,70,80,93,],[-24,-27,-32,-31,-33,-25,-26,-44,-43,79,-28,-29,-30,-34,-23,]),'ELSE':([89,],[90,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'defdefs':([0,2,30,],[1,4,33,]),'defdef':([0,2,30,],[2,2,2,]),'parmsopt':([6,],[8,]),'parms':([6,13,],[9,18,]),'vardef':([6,13,31,],[10,10,34,]),'type':([11,16,17,24,26,],[14,20,22,20,29,]),'typesopt':([16,],[19,]),'types':([16,24,],[21,27,]),'vardefsopt':([28,44,],[30,58,]),'defdefsopt':([30,],[32,]),'expras':([32,49,81,91,],[37,61,88,92,]),'expra':([32,49,81,91,],[38,38,38,38,]),'expr':([32,36,45,49,52,53,57,74,75,76,77,78,79,81,91,],[39,46,59,39,64,67,64,82,83,84,85,86,87,39,39,]),'term':([32,36,45,49,50,51,52,53,57,74,75,76,77,78,79,81,91,],[41,41,41,41,62,63,41,41,41,41,41,41,41,41,41,41,41,]),'factor':([32,36,45,49,50,51,52,53,54,55,56,57,74,75,76,77,78,79,81,91,],[42,42,42,42,42,42,42,42,68,69,70,42,42,42,42,42,42,42,42,42,]),'args':([52,57,],[65,72,]),'test':([53,],[66,]),'argsopt':([57,],[71,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> defdefs","S'",1,None,None,None),
  ('defdefs -> defdef defdefs','defdefs',2,'p_defdefs_defdef_defdefs','parser.py',9),
  ('defdefs -> defdef','defdefs',1,'p_defdefs_defdef','parser.py',14),
  ('defdef -> DEF ID LPAREN parmsopt RPAREN COLON type BECOMES LBRACE vardefsopt defdefsopt expras RBRACE','defdef',13,'p_defdef_def_id','parser.py',19),
  ('parmsopt -> parms','parmsopt',1,'p_parmsopt_parms','parser.py',24),
  ('parmsopt -> <empty>','parmsopt',0,'p_parmsopt','parser.py',29),
  ('parms -> vardef COMMA parms','parms',3,'p_parms_vardef_comma_parms','parser.py',34),
  ('parms -> vardef','parms',1,'p_parms_vardef','parser.py',39),
  ('vardef -> ID COLON type','vardef',3,'p_vardef_id_colon_type','parser.py',44),
  ('type -> INT','type',1,'p_type_int','parser.py',49),
  ('type -> LPAREN typesopt RPAREN ARROW type','type',5,'p_type_laparen_typesopt_rparen_arrow_type','parser.py',54),
  ('typesopt -> types','typesopt',1,'p_typesopt_types','parser.py',59),
  ('typesopt -> <empty>','typesopt',0,'p_typesopt','parser.py',64),
  ('types -> type COMMA types','types',3,'p_types_type_COMMA_types','parser.py',69),
  ('types -> type','types',1,'p_types_type','parser.py',74),
  ('vardefsopt -> VAR vardef SEMI vardefsopt','vardefsopt',4,'p_vardefsopt_var_vardef_semi_vardefsopt','parser.py',79),
  ('vardefsopt -> <empty>','vardefsopt',0,'p_vardefsopt','parser.py',84),
  ('defdefsopt -> defdefs','defdefsopt',1,'p_defdefsopt_defdef','parser.py',89),
  ('defdefsopt -> <empty>','defdefsopt',0,'p_defdefsopt','parser.py',94),
  ('expras -> expra SEMI expras','expras',3,'p_expras_expra_semi_expras','parser.py',99),
  ('expras -> expra','expras',1,'p_expras_expra','parser.py',104),
  ('expra -> ID BECOMES expr','expra',3,'p_expra_id_becomes_expr','parser.py',109),
  ('expra -> expr','expra',1,'p_expra_expr','parser.py',114),
  ('expr -> IF LPAREN test RPAREN LBRACE expras RBRACE ELSE LBRACE expras RBRACE','expr',11,'p_expr_if_lparen_test','parser.py',119),
  ('expr -> term','expr',1,'p_expr_term','parser.py',124),
  ('expr -> expr PLUS term','expr',3,'p_expr_plus_term','parser.py',129),
  ('expr -> expr MINUS term','expr',3,'p_expr_minus_term','parser.py',134),
  ('term -> factor','term',1,'p_term_factor','parser.py',139),
  ('term -> term STAR factor','term',3,'p_term_star','parser.py',144),
  ('term -> term SLASH factor','term',3,'p_term_slash','parser.py',149),
  ('term -> term PCT factor','term',3,'p_term_pct','parser.py',154),
  ('factor -> ID','factor',1,'p_factor_id','parser.py',159),
  ('factor -> NUM','factor',1,'p_factor_num','parser.py',164),
  ('factor -> LPAREN expr RPAREN','factor',3,'p_factor_lparen_expr_rparen','parser.py',169),
  ('factor -> factor LPAREN argsopt RPAREN','factor',4,'p_factor_factor_lparen_argsopt_rparen','parser.py',174),
  ('test -> expr NE expr','test',3,'p_test_expr_ne_expr','parser.py',179),
  ('test -> expr LT expr','test',3,'p_test_expr_lt_expr','parser.py',184),
  ('test -> expr LE expr','test',3,'p_test_expr_le_expr','parser.py',189),
  ('test -> expr GE expr','test',3,'p_test_expr_ge_expr','parser.py',194),
  ('test -> expr GT expr','test',3,'p_test_expr_gt_expr','parser.py',199),
  ('test -> expr EQ expr','test',3,'p_test_expr_eq_expr','parser.py',204),
  ('argsopt -> args','argsopt',1,'p_argsopt_args','parser.py',209),
  ('argsopt -> <empty>','argsopt',0,'p_argspot','parser.py',214),
  ('expr -> expr COMMA args','expr',3,'p_expr_comma_args','parser.py',219),
  ('args -> expr','args',1,'p_args_expr','parser.py',224),
]
