from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser

# cores
co0 = "#000000"  # preta
co1 = "#feffff"  # branca
co2 = "#ff1378"  # rosa
co3 = "#38576b"  # cor do valor
co4 = "#403d3d"  # cor da letra

# criando janela
janela = Tk()
janela.title("")
janela.geometry("310x300")
janela.configure(bg=co1)
janela.resizable(False, False)

# Frames
frame_cima = Frame(janela, width=310, height=50, bg=co1, relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
frame_baixo = Frame(janela, width=310, height=300, bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# configurando frame_cima
l_nome = Label(frame_cima, text="LOGIN", height=1, anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima, width=275, text="", height=1, anchor=NW, font=("Ivy 1"), bg=co2)
l_linha.place(x=10, y=45)

credenciais = ['Vini', '123']

def verificar_senha():
    nome = e_nome.get()
    senha = str(e_pass.get())

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo Admin!!!')

    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login', 'Seja bem vindo de volta ' + credenciais[0])

        for widget in frame_baixo.winfo_children():
            widget.destroy()

        for widget in frame_cima.winfo_children():
            widget.destroy()

        nova_janela()
    else:
        messagebox.showwarning('Erro', 'Verifique o nome de usuario ou a palavra passe')

def nova_janela():
    l_nome = Label(frame_cima, text="Usuario: " + credenciais[0], height=1, anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
    l_nome.place(x=5, y=5)

    l_linha = Label(frame_cima, width=275, text="", height=1, anchor=NW, font=('Ivy 1'), bg=co2)
    l_linha.place(x=10, y=45)

    global icon_editar
    img = Image.open("foto.png")
    img = img.resize((300, 300))
    icon_editar = ImageTk.PhotoImage(img)
    l_icon = Label(frame_baixo, image=icon_editar, anchor=NE)
    l_icon.place(x=10, y=10)

    def abrir_video():
        url = "https://www.youtube.com/watch?v=kwJTpJjLJi4"
        webbrowser.open(url)

    l_icon.bind("<Button-1>", lambda e: abrir_video())

l_nome = Label(frame_baixo, text="Nome *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightbackground=co1, relief="solid")
e_nome.place(x=14, y=50)

l_pass = Label(frame_baixo, text="password *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_pass.place(x=10, y=95)
e_pass = Entry(frame_baixo, show='*', width=25, justify='left', font=("", 15), highlightbackground=co1, relief="solid")
e_pass.place(x=15, y=130)

botao_confirmar = Button(frame_baixo, text="Entra", width=39, height=2, bg=co2, fg=co1,
                        font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE, command=verificar_senha)
botao_confirmar.place(x=15, y=180)

janela.mainloop()

