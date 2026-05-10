import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

# --- CONEXÃO COM O BANCO DE DADOS ---
conn = sqlite3.connect('itam.db')
cursor = conn.cursor()

# Criar tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS perifericos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        periferico TEXT NOT NULL,
        modelo TEXT NOT NULL,
        quantidade INTEGER NOT NULL
    )
''')
conn.commit()

def salvar_dados():
    p = entry_periferico.get().strip()
    m = entry_modelo.get().strip()
    q_texto = entry_qtd.get().strip()

    if not p  or not m  or not q_texto:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
        return
    
    try:
        q_nova = int(q_texto)

        cursor.execute('SELECT id, quantidade FROM perifericos WHERE periferico =? AND modelo = ?', (p, m))
        resultado = cursor.fetchone()

        if resultado:
            id_existente, qtd_existente = resultado
            nova_qtd = qtd_existente + q_nova
            cursor.execute('UPDATE perifericos SET quantidade = ? WHERE id = ?', (nova_qtd, id_existente))
            messagebox.showinfo("Atualização", f"Periférico existente atualizado: {p} - {m}\nQuantidade atualizada para: {nova_qtd}")

        else:
            cursor.execute('INSERT INTO perifericos (periferico, modelo, quantidade) VALUES (?, ?, ?)', (p, m, q_nova))
            messagebox.showinfo("Sucesso", "Periférico cadastrado com sucesso!")

            conn.commit()
            entry_periferico.delete(0, tk.END)
            entry_modelo.delete(0, tk.END)
            entry_qtd.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Erro", "Quantidade deve ser um número inteiro!")

def excluir_item(tabela):
    item_selecionado = tabela.selection()
    if not item_selecionado:
        messagebox.showwarning("Aviso", "Selecione um item para excluir.")
        return
    
    valores = tabela.item(item_selecionado)['values']
    id_item = valores[0]

    confirmar = messagebox.askyesno("Confirmação", f"Tem certeza que deseja excluir o item: {valores[1]} - {valores[2]}?")
    if confirmar:
        cursor.execute('DELETE FROM perifericos WHERE id = ?', (id_item,))
        conn.commit()
        tabela.delete(item_selecionado)
        messagebox.showinfo("Sucesso", "Item excluído com sucesso!")

def listar_dados():
    janela_lista = tk.Toplevel(janela)
    janela_lista.title("Inventário Completo")
    janela_lista.geometry("600x400")

    colunas = ("ID", "Periférico", "Modelo", "Quantidade")
    tabela = ttk.Treeview(janela_lista, columns=colunas, show='headings')

    for col in colunas:
        tabela.heading(col, text=col)
        tabela.column(col, width=100)

    tabela.pack(fill=tk.BOTH, expand=True, pady=10)

    cursor.execute('SELECT id, periferico, modelo, quantidade FROM perifericos')
    for linha in cursor.fetchall():
        tabela.insert('', tk.END, values=linha)
    
    btn_excluir = tk.Button(janela_lista, text="Excluir Item Selecionado", command=lambda: excluir_item(tabela), bg="#e74c3c", fg="white")
    btn_excluir.pack(pady=10)

def sair():
    conn.close()
    janela.quit()

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

tk.Button(janela, text="Cadastrar", command=salvar_dados, bg="#27ae60", fg="white").pack(pady=10)
tk.Button(janela, text="Visualizar Estoque", command=listar_dados, bg="#2980b9", fg="white").pack(pady=10)
tk.Button(janela, text="Sair", command=sair, bg="#c0392b", fg="white").pack(pady=10)

janela.mainloop()

conn.close()