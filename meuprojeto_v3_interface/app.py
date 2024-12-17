import tkinter as tk
from tkinter import messagebox, ttk
from func import adicionar_cliente, carregar_dados, salvar_dados, registrar_venda
from analytics import cliente_top_faturamento

# Caminho do arquivo JSON
ARQUIVO_JSON = "clientes.json"

# Carregar os dados no início
clientes = carregar_dados(ARQUIVO_JSON)

# Funções de interface
def adicionar_cliente_tk():
    try:
        codigo = int(entry_codigo.get())
        nome = entry_nome.get()
        endereco = entry_endereco.get()
        contato = entry_contato.get()

        novo_cliente = {
            "Codigo": codigo,
            "Nome": nome,
            "Endereco": endereco,
            "Contato": contato
        }

        adicionar_cliente(clientes, novo_cliente)
        salvar_dados(ARQUIVO_JSON, clientes)
        messagebox.showinfo("Sucesso", "Cliente adicionado com sucesso!")
        limpar_campos()
        atualizar_lista_clientes()

    except ValueError:
        messagebox.showerror("Erro", "Preencha os campos corretamente.")

def registrar_venda_tk():
    try:
        codigo = int(entry_codigo.get())
        descricao = entry_descricao.get()
        valor = float(entry_valor.get())

        venda = {"Descrição": descricao, "Valor": valor}

        if registrar_venda(clientes, codigo, venda):

            salvar_dados(ARQUIVO_JSON, clientes)
            messagebox.showinfo("Sucesso", "Venda registrada com sucesso!")
            atualizar_lista_clientes()

        else:
            messagebox.showwarning("Aviso", "Cliente não encontrado.")

    except ValueError:
        messagebox.showerror("Erro", "Preencha os campos corretamente.")

def analisar_faturamento_tk():
    resultado = cliente_top_faturamento(clientes)
    messagebox.showinfo("Análise de Faturamento", resultado)

def atualizar_lista_clientes():
    listbox_clientes.delete(0, tk.END)
    for cliente in clientes:
        cliente_formatado = f"{cliente['Codigo']} - {cliente['Nome']} - {cliente.get('Contato', '')}"
        listbox_clientes.insert(tk.END, cliente_formatado)

def limpar_campos():
    entry_codigo.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_contato.delete(0, tk.END)
    entry_descricao.delete(0, tk.END)
    entry_valor.delete(0, tk.END)

# Configuração da janela principal
root = tk.Tk()
root.title("Sistema de Gestão Cadastral")

# Widgets da interface
frame_cadastro = tk.LabelFrame(root, text="Cadastro de Cliente", padx=10, pady=10)
frame_cadastro.pack(padx=10, pady=10)

tk.Label(frame_cadastro, text="Código").grid(row=0, column=0, sticky="w")
entry_codigo = tk.Entry(frame_cadastro)
entry_codigo.grid(row=0, column=1)

tk.Label(frame_cadastro, text="Nome").grid(row=1, column=0, sticky="w")
entry_nome = tk.Entry(frame_cadastro)
entry_nome.grid(row=1, column=1)

tk.Label(frame_cadastro, text="Endereço").grid(row=2, column=0, sticky="w")
entry_endereco = tk.Entry(frame_cadastro)
entry_endereco.grid(row=2, column=1)

tk.Label(frame_cadastro, text="Contato").grid(row=3, column=0, sticky="w")
entry_contato = tk.Entry(frame_cadastro)
entry_contato.grid(row=3, column=1)

tk.Button(frame_cadastro, text="Adicionar Cliente", command=adicionar_cliente_tk).grid(row=4, column=0, columnspan=2, pady=10)

frame_venda = tk.LabelFrame(root, text="Registrar Venda", padx=10, pady=10)
frame_venda.pack(padx=10, pady=10)

tk.Label(frame_venda, text="Descrição").grid(row=0, column=0, sticky="w")
entry_descricao = tk.Entry(frame_venda)
entry_descricao.grid(row=0, column=1)

tk.Label(frame_venda, text="Valor").grid(row=1, column=0, sticky="w")
entry_valor = tk.Entry(frame_venda)
entry_valor.grid(row=1, column=1)

tk.Button(frame_venda, text="Registrar Venda", command=registrar_venda_tk).grid(row=2, column=0, columnspan=2, pady=10)

frame_clientes = tk.LabelFrame(root, text="Clientes Cadastrados", padx=10, pady=10)
frame_clientes.pack(padx=10, pady=10)

listbox_clientes = tk.Listbox(frame_clientes, width=50, height=10)
listbox_clientes.pack(side=tk.LEFT, padx=20)
scrollbar = tk.Scrollbar(frame_clientes)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox_clientes.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_clientes.yview)

tk.Button(root, text="Analisar Faturamento", command=analisar_faturamento_tk).pack(pady=10)

# Atualiza a lista ao iniciar
atualizar_lista_clientes()

# Inicia o loop da interface
root.mainloop()
