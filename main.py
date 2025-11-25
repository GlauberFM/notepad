import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, Text, Frame, Button


class BlocoDeNotasSimples:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title("Bloco de Notas")

        # Guarda o caminho do arquivo atual
        self.arquivo_atual = None

        # Área de texto
        self.texto: Text = Text(self.root, wrap='word')
        self.texto.pack(expand=True, fill='both')

        # Frame dos botões
        self.area_botoes: Frame = Frame(self.root)
        self.area_botoes.pack()

        # Botão salvar
        self.botao_salvar: Button = Button(self.area_botoes, text="Salvar", command=self.salvar)
        self.botao_salvar.pack(side=tk.LEFT)

        # Botão carregar
        self.botao_carregar: Button = Button(self.area_botoes, text="Carregar", command=self.carregar)
        self.botao_carregar.pack(side=tk.LEFT)

    def salvar(self) -> None:
        # Se já existe um arquivo, só sobrescreve
        if self.arquivo_atual:
            with open(self.arquivo_atual, 'w') as file:
                file.write(self.texto.get(1.0, tk.END))
            print(f"Arquivo salvo em: {self.arquivo_atual}")
            return

        # Se não existe ainda, pergunta onde salvar
        caminho: str = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Arquivos de texto", "*.txt")]
        )

        if caminho:
            self.arquivo_atual = caminho
            with open(caminho, "w") as file:
                file.write(self.texto.get(1.0, tk.END))
            print(f"Arquivo salvo em: {caminho}")

    def carregar(self) -> None:
        caminho: str = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Arquivos de texto", "*.txt")]
        )

        if caminho:
            self.arquivo_atual = caminho
            with open(caminho, "r") as file:
                conteudo = file.read()
            self.texto.delete(1.0, tk.END)
            self.texto.insert(tk.INSERT, conteudo)
            print(f"Arquivo carregado: {caminho}")

    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    root: Tk = tk.Tk()
    app = BlocoDeNotasSimples(root)
    app.run()


if __name__ == "__main__":
    main()
