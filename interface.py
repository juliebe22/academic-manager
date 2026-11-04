import tkinter as tk
from tkinter import ttk, messagebox
from pymongo.errors import DuplicateKeyError

from alunos import (
    cadastrar_aluno,
    listar_alunos,
    atualizar_aluno,
    excluir_aluno
)


class AcademicManager:

    def __init__(self, root):

        self.root = root

        self.root.title("Academic Manager")
        self.root.geometry("1050x650")
        self.root.minsize(900, 550)

        self.root.configure(bg="#f2f4f8")

        self.id_selecionado = None

        self.criar_interface()
        self.carregar_alunos()

    # Criar interface
    def criar_interface(self):

        titulo = tk.Label(
            self.root,
            text="ACADEMIC MANAGER",
            font=("Arial", 22, "bold"),
            bg="#f2f4f8",
            fg="#243b64"
        )

        titulo.pack(pady=20)

        # Formulário
        formulario = ttk.LabelFrame(
            self.root,
            text="Dados do aluno",
            padding=15
        )

        formulario.pack(
            fill="x",
            padx=25,
            pady=10
        )

        self.nome = tk.StringVar()
        self.matricula = tk.StringVar()
        self.curso = tk.StringVar()
        self.email = tk.StringVar()
        self.periodo = tk.StringVar()

        campos = [
            ("Nome completo", self.nome),
            ("Matrícula", self.matricula),
            ("Curso", self.curso),
            ("E-mail", self.email),
            ("Período", self.periodo)
        ]

        for i, (texto, variavel) in enumerate(campos):

            linha = i // 3
            coluna = (i % 3) * 2

            ttk.Label(
                formulario,
                text=texto
            ).grid(
                row=linha,
                column=coluna,
                padx=8,
                pady=8,
                sticky="w"
            )

            ttk.Entry(
                formulario,
                textvariable=variavel,
                width=30
            ).grid(
                row=linha,
                column=coluna + 1,
                padx=8,
                pady=8
            )

        # Botões
        botoes = ttk.Frame(self.root)

        botoes.pack(pady=10)

        ttk.Button(
            botoes,
            text="Cadastrar",
            command=self.cadastrar
        ).grid(row=0, column=0, padx=5)

        ttk.Button(
            botoes,
            text="Atualizar",
            command=self.atualizar
        ).grid(row=0, column=1, padx=5)

        ttk.Button(
            botoes,
            text="Excluir",
            command=self.excluir
        ).grid(row=0, column=2, padx=5)

        ttk.Button(
            botoes,
            text="Limpar",
            command=self.limpar
        ).grid(row=0, column=3, padx=5)

        # Pesquisa
        pesquisa_frame = ttk.Frame(self.root)

        pesquisa_frame.pack(
            fill="x",
            padx=25,
            pady=10
        )

        ttk.Label(
            pesquisa_frame,
            text="Pesquisar aluno:"
        ).pack(side="left", padx=5)

        self.pesquisa = tk.StringVar()

        entrada_pesquisa = ttk.Entry(
            pesquisa_frame,
            textvariable=self.pesquisa,
            width=40
        )

        entrada_pesquisa.pack(side="left", padx=5)

        entrada_pesquisa.bind(
            "<KeyRelease>",
            lambda evento: self.carregar_alunos()
        )

        ttk.Button(
            pesquisa_frame,
            text="Buscar",
            command=self.carregar_alunos
        ).pack(side="left", padx=5)

        ttk.Button(
            pesquisa_frame,
            text="Mostrar todos",
            command=self.mostrar_todos
        ).pack(side="left", padx=5)

        # Tabela
        tabela_frame = ttk.Frame(self.root)

        tabela_frame.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=15
        )

        colunas = (
            "nome",
            "matricula",
            "curso",
            "email",
            "periodo"
        )

        self.tabela = ttk.Treeview(
            tabela_frame,
            columns=colunas,
            show="headings"
        )

        self.tabela.heading("nome", text="Nome")
        self.tabela.heading("matricula", text="Matrícula")
        self.tabela.heading("curso", text="Curso")
        self.tabela.heading("email", text="E-mail")
        self.tabela.heading("periodo", text="Período")

        self.tabela.column("nome", width=200)
        self.tabela.column("matricula", width=110)
        self.tabela.column("curso", width=200)
        self.tabela.column("email", width=200)
        self.tabela.column("periodo", width=80)

        scrollbar = ttk.Scrollbar(
            tabela_frame,
            orient="vertical",
            command=self.tabela.yview
        )

        self.tabela.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabela.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(side="right", fill="y")

        self.tabela.bind(
            "<<TreeviewSelect>>",
            self.selecionar_aluno
        )

    # CREATE
    def cadastrar(self):

        dados = self.obter_dados()

        if dados is None:
            return

        try:

            cadastrar_aluno(dados)

            messagebox.showinfo(
                "Sucesso",
                "Aluno cadastrado com sucesso!"
            )

            self.limpar()
            self.carregar_alunos()

        except DuplicateKeyError:

            messagebox.showerror(
                "Erro",
                "Esta matrícula já está cadastrada."
            )

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                f"Não foi possível cadastrar: {erro}"
            )

    # Validar formulário
    def obter_dados(self):

        nome = self.nome.get().strip()
        matricula = self.matricula.get().strip()
        curso = self.curso.get().strip()
        email = self.email.get().strip()
        periodo = self.periodo.get().strip()

        if not nome or not matricula or not curso or not periodo:

            messagebox.showwarning(
                "Atenção",
                "Preencha nome, matrícula, curso e período."
            )

            return None

        if not periodo.isdigit() or int(periodo) < 1:

            messagebox.showwarning(
                "Atenção",
                "Informe um período acadêmico válido."
            )

            return None

        if email and ("@" not in email or "." not in email.split("@")[-1]):

            messagebox.showwarning(
                "Atenção",
                "Informe um e-mail válido."
            )

            return None

        return {
            "nome": nome,
            "matricula": matricula,
            "curso": curso,
            "email": email,
            "periodo": periodo
        }

    # READ
    def carregar_alunos(self):

        for item in self.tabela.get_children():

            self.tabela.delete(item)

        termo = self.pesquisa.get().strip()

        filtro = {}

        if termo:

            filtro = {
                "$or": [
                    {"nome": {"$regex": termo, "$options": "i"}},
                    {"matricula": {"$regex": termo, "$options": "i"}},
                    {"curso": {"$regex": termo, "$options": "i"}}
                ]
            }

        try:

            alunos = listar_alunos(filtro)

            for aluno in alunos:

                self.tabela.insert(
                    "",
                    "end",
                    iid=str(aluno["_id"]),
                    values=(
                        aluno.get("nome", ""),
                        aluno.get("matricula", ""),
                        aluno.get("curso", ""),
                        aluno.get("email", ""),
                        aluno.get("periodo", "")
                    )
                )

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                f"Não foi possível consultar os alunos: {erro}"
            )

    # Selecionar aluno na tabela
    def selecionar_aluno(self, evento):

        selecionado = self.tabela.selection()

        if not selecionado:
            return

        self.id_selecionado = selecionado[0]

        dados = self.tabela.item(
            self.id_selecionado,
            "values"
        )

        self.nome.set(dados[0])
        self.matricula.set(dados[1])
        self.curso.set(dados[2])
        self.email.set(dados[3])
        self.periodo.set(dados[4])

    # UPDATE
    def atualizar(self):

        if not self.id_selecionado:

            messagebox.showwarning(
                "Atenção",
                "Selecione um aluno na tabela."
            )

            return

        dados = self.obter_dados()

        if dados is None:
            return

        try:

            atualizar_aluno(
                self.id_selecionado,
                dados
            )

            messagebox.showinfo(
                "Sucesso",
                "Dados atualizados com sucesso!"
            )

            self.limpar()
            self.carregar_alunos()

        except DuplicateKeyError:

            messagebox.showerror(
                "Erro",
                "Esta matrícula já pertence a outro aluno."
            )

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                f"Não foi possível atualizar: {erro}"
            )

    # DELETE
    def excluir(self):

        if not self.id_selecionado:

            messagebox.showwarning(
                "Atenção",
                "Selecione um aluno na tabela."
            )

            return

        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            "Deseja realmente excluir este aluno?"
        )

        if confirmar:

            try:

                excluir_aluno(self.id_selecionado)

                messagebox.showinfo(
                    "Sucesso",
                    "Aluno excluído com sucesso!"
                )

                self.limpar()
                self.carregar_alunos()

            except Exception as erro:

                messagebox.showerror(
                    "Erro",
                    f"Não foi possível excluir: {erro}"
                )

    # Limpar formulário
    def limpar(self):

        self.nome.set("")
        self.matricula.set("")
        self.curso.set("")
        self.email.set("")
        self.periodo.set("")

        self.id_selecionado = None

        selecionado = self.tabela.selection()

        if selecionado:
            self.tabela.selection_remove(*selecionado)

    # Mostrar todos os alunos
    def mostrar_todos(self):

        self.pesquisa.set("")
        self.carregar_alunos()