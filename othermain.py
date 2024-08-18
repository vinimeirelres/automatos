import criarafd
import tkinter as tk

def afd():
    criarafd.cria_afd()


root = tk.Tk()
root.title("My App")


button = tk.Button(root, text="CRIE UM AFD", command=afd)
button.pack()

label = tk.Label(root, text="Olá, Mundo!", font=("Arial", 16))

# Posiciona o rótulo na janela
label.pack(pady=20)

root.mainloop()
