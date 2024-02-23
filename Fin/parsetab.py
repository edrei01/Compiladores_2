
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AGUSTICIDAD ASSIGN DESIGUAL DIV DOBLEIGUAL DOUBLESTRING ENTERO GREATER ID IGUALMA IGUALMENO INCREMENT LBRACE LPAREN MAS MENOR MENOS MULTI NOVASIR NUMBER PAN PARAQOQUE PUNTCOM RBRACE RPAREN SEMI SIONO STRING UBUBUE VASIR VUELAOQUEinit : inicio\n            | opcion2\n            | opcion3\n            | opcion4inicio : PARAQOQUE LPAREN variable ID ASSIGN NUMBER PUNTCOM ID operador NUMBER PUNTCOM ID INCREMENT PUNTCOM RPAREN LBRACE  ID RBRACEopcion2 : AGUSTICIDAD variable ID operador identopcion3 : VASIR LPAREN ID operador ident RPAREN LBRACE ident RBRACE NOVASIR LBRACE ident RBRACEopcion4 : VUELAOQUE SIONO LBRACE ident RBRACEvariable : UBUBUE\n                | PANoperador : GREATER\n                | IGUALMA\n                | IGUALMENO\n                | DOBLEIGUAL\n                | MENOR\n                | DESIGUAL\n                | ASSIGNident : ID  \n             | NUMBER'
    
_lr_action_items = {'PARAQOQUE':([0,],[6,]),'AGUSTICIDAD':([0,],[7,]),'VASIR':([0,],[8,]),'VUELAOQUE':([0,],[9,]),'$end':([1,2,3,4,5,31,32,34,36,52,57,],[0,-1,-2,-3,-4,-18,-19,-6,-8,-7,-5,]),'LPAREN':([6,8,],[10,14,]),'UBUBUE':([7,10,],[12,12,]),'PAN':([7,10,],[13,13,]),'SIONO':([9,],[15,]),'ID':([11,12,13,14,16,19,21,22,23,24,25,26,27,28,29,39,40,47,48,55,],[17,-9,-10,18,20,31,31,-11,-12,-13,-14,-15,-16,-17,31,41,31,49,31,56,]),'LBRACE':([15,38,46,54,],[19,40,48,55,]),'GREATER':([17,18,41,],[22,22,22,]),'IGUALMA':([17,18,41,],[23,23,23,]),'IGUALMENO':([17,18,41,],[24,24,24,]),'DOBLEIGUAL':([17,18,41,],[25,25,25,]),'MENOR':([17,18,41,],[26,26,26,]),'DESIGUAL':([17,18,41,],[27,27,27,]),'ASSIGN':([17,18,20,41,],[28,28,33,28,]),'NUMBER':([19,21,22,23,24,25,26,27,28,29,33,40,43,48,],[32,32,-11,-12,-13,-14,-15,-16,-17,32,37,32,45,32,]),'RBRACE':([30,31,32,42,50,56,],[36,-18,-19,44,52,57,]),'RPAREN':([31,32,35,53,],[-18,-19,38,54,]),'PUNTCOM':([37,45,51,],[39,47,53,]),'NOVASIR':([44,],[46,]),'INCREMENT':([49,],[51,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'inicio':([0,],[2,]),'opcion2':([0,],[3,]),'opcion3':([0,],[4,]),'opcion4':([0,],[5,]),'variable':([7,10,],[11,16,]),'operador':([17,18,41,],[21,29,43,]),'ident':([19,21,29,40,48,],[30,34,35,42,50,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> inicio','init',1,'p_init','sintactico.py',5),
  ('init -> opcion2','init',1,'p_init','sintactico.py',6),
  ('init -> opcion3','init',1,'p_init','sintactico.py',7),
  ('init -> opcion4','init',1,'p_init','sintactico.py',8),
  ('inicio -> PARAQOQUE LPAREN variable ID ASSIGN NUMBER PUNTCOM ID operador NUMBER PUNTCOM ID INCREMENT PUNTCOM RPAREN LBRACE ID RBRACE','inicio',18,'p_inicio','sintactico.py',11),
  ('opcion2 -> AGUSTICIDAD variable ID operador ident','opcion2',5,'p_opcion2','sintactico.py',14),
  ('opcion3 -> VASIR LPAREN ID operador ident RPAREN LBRACE ident RBRACE NOVASIR LBRACE ident RBRACE','opcion3',13,'p_opcion3','sintactico.py',17),
  ('opcion4 -> VUELAOQUE SIONO LBRACE ident RBRACE','opcion4',5,'p_opcion4','sintactico.py',20),
  ('variable -> UBUBUE','variable',1,'p_variable','sintactico.py',23),
  ('variable -> PAN','variable',1,'p_variable','sintactico.py',24),
  ('operador -> GREATER','operador',1,'p_operador','sintactico.py',27),
  ('operador -> IGUALMA','operador',1,'p_operador','sintactico.py',28),
  ('operador -> IGUALMENO','operador',1,'p_operador','sintactico.py',29),
  ('operador -> DOBLEIGUAL','operador',1,'p_operador','sintactico.py',30),
  ('operador -> MENOR','operador',1,'p_operador','sintactico.py',31),
  ('operador -> DESIGUAL','operador',1,'p_operador','sintactico.py',32),
  ('operador -> ASSIGN','operador',1,'p_operador','sintactico.py',33),
  ('ident -> ID','ident',1,'p_ident','sintactico.py',35),
  ('ident -> NUMBER','ident',1,'p_ident','sintactico.py',36),
]
