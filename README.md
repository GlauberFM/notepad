Notepad

Este projeto é um bloco de notas simples desenvolvido em Python utilizando a biblioteca Tkinter. Ele permite criar, editar, salvar e carregar arquivos de texto de forma prática. O programa foi estruturado em classe, facilitando manutenção e expansão futura.

Funcionalidades

Área de texto com quebra automática de linha.

Botão para salvar o conteúdo em um arquivo .txt.

Botão para carregar arquivos .txt.

Salvamento inteligente: caso o arquivo já exista, o conteúdo é atualizado sem pedir um novo nome.

Como executar

Certifique-se de ter o Python instalado em sua máquina.

Execute o arquivo principal:

python nome_do_arquivo.py


A interface será aberta e você poderá escrever, salvar e carregar seus textos.

Estrutura do código

Classe SimpleNotepad: concentra toda a interface e funcionalidades.

save_file(): salva o texto no arquivo atual ou cria um novo.

load_file(): carrega o conteúdo de um arquivo escolhido.

run(): inicia o loop principal da interface.

Requisitos

Python 3.x

Tkinter (normalmente já incluído no Python)

Objetivo

O projeto foi criado para estudo e prática de interface gráfica com Tkinter, além de manipulação de arquivos em Python.
