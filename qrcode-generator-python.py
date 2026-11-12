import qrcode
import tkinter as tk
from tkinter import messagebox, ttk


def atualizar_campos(event=None):
    tipo = escolha_tipo.get()

    if tipo == "Wi-Fi":
        label_conteudo.config(text="Nome da rede Wi-Fi:")
        label_senha.pack(pady=5)
        entrada_senha.pack(pady=5)
    elif tipo == "Telefone":
        label_conteudo.config(text="Número de telefone:")
        label_senha.pack_forget()
        entrada_senha.pack_forget()
    elif tipo == "E-mail":
        label_conteudo.config(text="Endereço de e-mail:")
        label_senha.pack_forget()
        entrada_senha.pack_forget()
    elif tipo == "Texto":
        label_conteudo.config(text="Digite seu texto:")
        label_senha.pack_forget()
        entrada_senha.pack_forget()
    else:
        label_conteudo.config(text="Digite o link:")
        label_senha.pack_forget()
        entrada_senha.pack_forget()


def gerar_qrcode():
    tipo = escolha_tipo.get()
    conteudo = entrada_conteudo.get().strip()

    if not conteudo:
        messagebox.showwarning("Atenção", "Preencha o campo!")
        return

    if tipo == "Wi-Fi":
        senha = entrada_senha.get()

        if not senha:
            messagebox.showwarning("Atenção", "Digite a senha do Wi-Fi!")
            return

        dados = f"WIFI:T:WPA;S:{conteudo};P:{senha};;"

    elif tipo == "Telefone":
        dados = f"tel:{conteudo}"

    elif tipo == "E-mail":
        dados = f"mailto:{conteudo}"

    else:
        dados = conteudo

    imagem = qrcode.make(dados)
    nome_arquivo = "meu_qrcode.png"
    imagem.save(nome_arquivo)

    messagebox.showinfo(
        "Sucesso",
        f"QR Code criado!\nArquivo: {nome_arquivo}"
    )


# Criando a janela
janela = tk.Tk()
janela.title("Gerador de QR Code")
janela.geometry("400x350")

# Título
titulo = tk.Label(
    janela,
    text="Gerador de QR Code",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=15)

# Seleção do tipo
label_tipo = tk.Label(janela, text="Escolha o tipo de QR Code:")
label_tipo.pack()

escolha_tipo = ttk.Combobox(
    janela,
    values=[
        "Link",
        "Texto",
        "Telefone",
        "E-mail",
        "Wi-Fi"
    ],
    state="readonly"
)

escolha_tipo.current(0)
escolha_tipo.pack(pady=8)
escolha_tipo.bind("<<ComboboxSelected>>", atualizar_campos)

# Campo principal
label_conteudo = tk.Label(janela, text="Digite o link:")
label_conteudo.pack(pady=5)

entrada_conteudo = tk.Entry(janela, width=40)
entrada_conteudo.pack(pady=5)

# Campo de senha do Wi-Fi
label_senha = tk.Label(janela, text="Senha do Wi-Fi:")
entrada_senha = tk.Entry(janela, width=40, show="*")

# Botão
botao = tk.Button(
    janela,
    text="Gerar QR Code",
    command=gerar_qrcode
)
botao.pack(pady=20)

# Executar janela
janela.mainloop()
