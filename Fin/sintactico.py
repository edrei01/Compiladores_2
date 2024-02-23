from tkinter import messagebox
import ply.yacc as yacc
from lexico import tokens, lexer
import tkinter as tk
from lexico import lexer


def p_init(p):
    '''init : inicio
            | opcion2
            | opcion3
            | opcion4'''
            
def p_inicio(p):
    '''inicio : PARAQOQUE LPAREN variable ID ASSIGN NUMBER PUNTCOM ID operador NUMBER PUNTCOM ID INCREMENT PUNTCOM RPAREN LBRACE  ID RBRACE'''
    
def p_opcion2(p):
    '''opcion2 : AGUSTICIDAD variable ID operador ident'''

def p_opcion3(p):
    '''opcion3 : VASIR LPAREN ID operador ident RPAREN LBRACE ident RBRACE NOVASIR LBRACE ident RBRACE'''    

def p_opcion4(p):
    '''opcion4 : VUELAOQUE SIONO LBRACE ident RBRACE'''
    
def p_variable(p):
    '''variable : UBUBUE
                | PAN'''

def p_operador(p):
    '''operador : GREATER
                | IGUALMA
                | IGUALMENO
                | DOBLEIGUAL
                | MENOR
                | DESIGUAL
                | ASSIGN'''
def p_ident(p):
    '''ident : ID  
             | NUMBER'''
def p_error(p):
    if p:
        error_table.insert('', 'end', values=(f"Error de sintaxis en el token '{p.value}'",))
    else:
        error_table.insert('', 'end', values=("Error de sintaxis en EOF",))

parser = yacc.yacc()

symbol_table = set()

def check_code(token_table, error_table, txt):  # Pasar txt como argumento
    for i in token_table.get_children():
        token_table.delete(i)
    for i in error_table.get_children():
        error_table.delete(i)

    code = txt.get("1.0", tk.END).strip()
    if not code:
        messagebox.showinfo('Resultado', 'No hay código para verificar.')
        return

    symbol_table.clear()

    lexer.input(code)

    for token in lexer:
        if token.type == 'DOUBLESTRING':
            value = token.value[1:-1]
        else:
            value = token.value
        token_table.insert('', 'end', values=(token.type, value))

    result = parser.parse(code, lexer=lexer)

    if not error_table.get_children():
        messagebox.showinfo('Resultado', 'La sintaxis y el análisis semántico son correctos.')
    else:
        messagebox.showerror('Resultado', 'Se encontraron errores de sintaxis o análisis semántico.')
