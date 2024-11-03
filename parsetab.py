
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDECOLON DIVIDE ELSE EQUALS GREATER IDENTIFIER IF LESS LPAREN MINUS NUMBER PLUS RPAREN TIMESstatement : IDENTIFIER EQUALS expressionexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expressionexpression : NUMBERexpression : IDENTIFIERexpression : LPAREN expression RPARENexpression : expression LESS expression\n                  | expression GREATER expressionstatement : IF expression COLON statement\n                 | IF expression COLON statement ELSE COLON statementstatement : statement statement'
    
_lr_action_items = {'IDENTIFIER':([0,1,3,4,5,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,28,29,],[2,2,8,2,8,-6,-7,8,-1,2,8,8,8,8,8,8,2,-2,-3,-4,-5,-9,-10,-8,2,2,]),'IF':([0,1,4,7,8,10,11,19,20,21,22,23,24,25,26,28,29,],[3,3,3,-6,-7,-1,3,3,-2,-3,-4,-5,-9,-10,-8,3,3,]),'$end':([1,4,7,8,10,19,20,21,22,23,24,25,26,29,],[0,-13,-6,-7,-1,-11,-2,-3,-4,-5,-9,-10,-8,-12,]),'EQUALS':([2,],[5,]),'NUMBER':([3,5,9,12,13,14,15,16,17,],[7,7,7,7,7,7,7,7,7,]),'LPAREN':([3,5,9,12,13,14,15,16,17,],[9,9,9,9,9,9,9,9,9,]),'ELSE':([4,7,8,10,19,20,21,22,23,24,25,26,29,],[-13,-6,-7,-1,27,-2,-3,-4,-5,-9,-10,-8,-12,]),'COLON':([6,7,8,20,21,22,23,24,25,26,27,],[11,-6,-7,-2,-3,-4,-5,-9,-10,-8,28,]),'PLUS':([6,7,8,10,18,20,21,22,23,24,25,26,],[12,-6,-7,12,12,-2,-3,-4,-5,12,12,-8,]),'MINUS':([6,7,8,10,18,20,21,22,23,24,25,26,],[13,-6,-7,13,13,-2,-3,-4,-5,13,13,-8,]),'TIMES':([6,7,8,10,18,20,21,22,23,24,25,26,],[14,-6,-7,14,14,14,14,-4,-5,14,14,-8,]),'DIVIDE':([6,7,8,10,18,20,21,22,23,24,25,26,],[15,-6,-7,15,15,15,15,-4,-5,15,15,-8,]),'LESS':([6,7,8,10,18,20,21,22,23,24,25,26,],[16,-6,-7,16,16,-2,-3,-4,-5,16,16,-8,]),'GREATER':([6,7,8,10,18,20,21,22,23,24,25,26,],[17,-6,-7,17,17,-2,-3,-4,-5,17,17,-8,]),'RPAREN':([7,8,18,20,21,22,23,24,25,26,],[-6,-7,26,-2,-3,-4,-5,-9,-10,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,1,4,11,19,28,29,],[1,4,4,19,4,29,4,]),'expression':([3,5,9,12,13,14,15,16,17,],[6,10,18,20,21,22,23,24,25,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> IDENTIFIER EQUALS expression','statement',3,'p_statement_assignment','main.py',65),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','main.py',70),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','main.py',71),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','main.py',72),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','main.py',73),
  ('expression -> NUMBER','expression',1,'p_expression_number','main.py',78),
  ('expression -> IDENTIFIER','expression',1,'p_expression_identifier','main.py',83),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_parens','main.py',88),
  ('expression -> expression LESS expression','expression',3,'p_expression_comparison','main.py',93),
  ('expression -> expression GREATER expression','expression',3,'p_expression_comparison','main.py',94),
  ('statement -> IF expression COLON statement','statement',4,'p_if_else_statement','main.py',99),
  ('statement -> IF expression COLON statement ELSE COLON statement','statement',7,'p_if_else_statement','main.py',100),
  ('statement -> statement statement','statement',2,'p_statement_sequence','main.py',108),
]
