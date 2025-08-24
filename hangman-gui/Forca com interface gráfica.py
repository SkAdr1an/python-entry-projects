import tkinter as tk
from tkinter import messagebox
import random
import string

class ForcaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")

        self.palavras = ["python", "programacao", "desenvolvimento", "interface", "computador"]
        self.palavra = random.choice(self.palavras)
        self.palavra_oculta = ["_" for _ in self.palavra]
        self.letras_erradas = []
        self.tentativas = 6

        # Corrigido: indentação normal aqui
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.label_palavra = tk.Label(self.frame, text=" ".join(self.palavra_oculta), font=("Helvetica", 24))
        self.label_palavra.pack()

        self.entry_letra = tk.Entry(self.frame, font=("Helvetica", 18), width=3, justify="center")
        self.entry_letra.pack(pady=5)
        self.entry_letra.focus_set()

        self.button_tentar = tk.Button(self.frame, text="Tentar", command=self.tentar)
        self.button_tentar.pack()

        self.label_tentativas = tk.Label(self.frame, text=f"Tentativas restantes: {self.tentativas}", font=("Helvetica", 16))
        self.label_tentativas.pack(pady=10)

        self.label_letras_erradas = tk.Label(self.frame, text="Letras erradas: ", font=("Helvetica", 16))
        self.label_letras_erradas.pack()

        # Enter também tenta
        self.root.bind("<Return>", lambda _: self.tentar())

    def tentar(self):
        letra = self.entry_letra.get().lower().strip()
        self.entry_letra.delete(0, tk.END)

        # Validação: 1 letra do alfabeto
        if len(letra) != 1 or letra not in string.ascii_lowercase:
            messagebox.showinfo("Informação", "Digite apenas uma letra (a–z).")
            return

        if letra in self.letras_erradas or letra in self.palavra_oculta:
            messagebox.showinfo("Informação", "Você já tentou essa letra!")
            return

        if letra in self.palavra:
            for i, l in enumerate(self.palavra):
                if l == letra:
                    self.palavra_oculta[i] = letra
            self.label_palavra.config(text=" ".join(self.palavra_oculta))
        else:
            self.letras_erradas.append(letra)
            self.tentativas -= 1
            self.label_tentativas.config(text=f"Tentativas restantes: {self.tentativas}")
            self.label_letras_erradas.config(text=f"Letras erradas: {', '.join(self.letras_erradas)}")

        if "_" not in self.palavra_oculta:
            messagebox.showinfo("Parabéns!", "Você ganhou!")
            self.resetar()
        elif self.tentativas <= 0:
            messagebox.showinfo("Game Over", f"Você perdeu! A palavra era '{self.palavra}'.")
            self.resetar()

    def resetar(self):
        self.palavra = random.choice(self.palavras)
        self.palavra_oculta = ["_" for _ in self.palavra]
        self.letras_erradas = []
        self.tentativas = 6
        self.label_palavra.config(text=" ".join(self.palavra_oculta))
        self.label_tentativas.config(text=f"Tentativas restantes: {self.tentativas}")
        self.label_letras_erradas.config(text="Letras erradas: ")

if __name__ == "__main__":
    root = tk.Tk()
    app = ForcaApp(root)
    root.mainloop()
