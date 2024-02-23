import tkinter as tk
from tkinter import ttk, messagebox
from sintactico import check_code
import lexico

root = tk.Tk()
root.title("Analizador Léxico, Sintáctico y Semántico")
root.configure(bg='green')  

codigo = '''for (int hijo = 8; hijo >7; hijo + 1) { texto}'''
txt = tk.Text(root, width=25, height=10)
txt.pack(side='left', padx=10, pady=10)
txt.insert(tk.END, codigo)

btn = tk.Button(root, text="analizar", command=lambda: check_code(token_table, error_table, txt, lexico.lexer))
btn.pack(side='left', padx=10)

token_frame = tk.Frame(root, bg='green')  
token_frame.pack(side='left', padx=10, pady=10)

token_table = ttk.Treeview(token_frame, columns=('Type', 'Value'), show='headings')
token_table.heading('Type', text='tokens')
token_table.heading('Value', text='valor')
token_table.pack()

error_frame = tk.Frame(root, bg='green')  
error_frame.pack(side='left', padx=10, pady=10)

error_table = ttk.Treeview(error_frame, columns=('Error',), show='headings')
error_table.heading('Error', text='lexico y semantico')
error_table.column('Error', width=200)  
error_table.pack()

root.mainloop()
