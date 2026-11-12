import qrcode
import tkinter as tk
from tkinter import messagebox

def gerar_qrcode():
    link = entrada_link.get()

    if not link:
        messagebox.showwarning("Atenção", "Digite um link!")
        return

    imagem = qrcode.make(link)
    imagem.save("meu_qrcode.png")

    messagebox.showinfo("Sucesso", "QR Code criado e salvo!")

# Criando a janela
janela = tk.Tk()
janela.title("Gerador de QR Code")
janela.geometry("350x200")

# Título
titulo = tk.Label(janela, text="Gerador de QR Code", font=("Arial", 16))
titulo.pack(pady=15)

# Campo para digitar o link
entrada_link = tk.Entry(janela, width=40)
entrada_link.pack(pady=10)

# Botão para gerar
botao = tk.Button(
    janela,
    text="Gerar QR Code",
    command=gerar_qrcode
)
botao.pack(pady=10)

# Executar a janela
janela.mainloop()
