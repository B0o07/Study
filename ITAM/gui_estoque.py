import tkinter as tk
from tkinter import ttk
import database as db

# --- INTERFACE GRÁFICA ---

janela = tk.Tk()
janela.title("ITAM - Cadastro de Inventário")
janela.geometry("400x350")

tk.Label(janela, text="Periférico:").pack(pady=2)
entry_periferico = ttk.Entry(janela, width=40)
entry_periferico.pack()

tk.Label(janela, text="Modelo:").pack(pady=2)
entry_modelo = ttk.Entry(janela, width=40)
entry_modelo.pack()

tk.Label(janela, text="Quantidade:").pack(pady=2)
entry_qtd = ttk.Entry(janela, width=40)
entry_qtd.pack()

# --- Botões ---

tk.Button(janela, text="Cadastrar", command=lambda: db.salvar_dados( entry_periferico.get(), entry_modelo.get(), entry_qtd.get(), entry_periferico, entry_modelo, entry_qtd), bg="#27ae60", fg="white").pack(pady=10)
tk.Button(janela, text="Visualizar Estoque", command=lambda: db.listar_dados(janela), bg="#2980b9", fg="white").pack(pady=10)
tk.Button(janela, text="Sair", command=lambda: db.sair(janela_para_fechar=janela), bg="#c0392b", fg="white").pack(pady=10)

janela.mainloop()
