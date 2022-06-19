# -*- coding: utf-8 -*-

# Requisitos do programa:

# Considere que você é um freelancer desenvolvedor de sistemas desktop. Para iniciar seu portfólio, você decide testar uma ideia de sistema para bibliotecas. Assim, você resolve que criará um programa como Prova de Conceito para validar suas ideias e também para poder mostrar para seus possíveis clientes. Dessa forma, seu programa, em versão beta (versão de testes), deverá permitir armazenar o cadastro de, no máximo, 5 (cinco) livros por vez (por execução do programa).
 
# Para cada livro, a aplicação deverá armazenar as seguintes informações:
# Um código único, gerado automaticamente pelo sistema;
# O nome dos autores da obra;
# O nome da obra;
# O nome da editora.
 
# O programa deverá apresentar um menu de opções ao usuário:
 
# 1. Inserir um novo cadastro:  ao selecionar essa opção, o usuário deverá ser capaz de informar todos os dados de um livro, a saber: seu nome, os autores, o nome da editora; o código do cadastro não deve ser informado pelo usuário pois o programa deve gerar automaticamente. Caso o programa já tenha armazenado o número máximo de livros (cinco), deverá ser exibida uma mensagem de erro: “Sistema de cadastro lotado. Não é possível armazenar mais informações!”. O código de um cadastro deve ser preenchido automaticamente pelo sistema e o usuário não deve ter a opção de alterar esse código. É importante salientar que para cada cadastro, deve-se ter um código distinto, ou seja, não deve ser possível que existam dois cadastros com o mesmo código, ao mesmo tempo;

# 2. Mostrar todos os cadastros: ao selecionar essa opção, o programa deverá imprimir, na tela, para cada livro, seu código, seu nome, os autores e a editora. Essa opção deverá mostrar na tela apenas os dados de livros que foram cadastrados. Caso seja impressa alguma outra informação sobressalente, ou caso faltem informações previamente cadastradas, será considerado um erro de programação. Caso nenhum cliente tenha sido cadastrado, antes de tentar executar essa opção (2 - Mostrar todos os cadastros), o programa deve exibir a mensagem “Lista vazia!”;
 
# 0. Encerrar: o programa dev1e ser encerrado se, e somente se, o usuário escolher essa opção.
 
# Sempre que o usuário desejar executar as opção 1 ou 2 (exceto 0), o programa deve realizar o que é pedido no enunciado e, logo após isso, o programa deve retornar ao menu, dando ao usuário a possibilidade de executar novamente alguma das opções listadas no menu.
 
# Caso o usuário escolha uma opção que não conste no menu, o programa deverá exibir uma mensagem de erro como, por exemplo, “Erro: opção inválida!”; retornando ao menu logo em seguida. Caso contrário, o programa não deverá imprimir essa mensagem de erro, ou seja, se o usuário tentar executar as opções 0, 1 ou 2, o programa não entra em estado de erro.
 
# A sua atividade MAPA deve ser entregue em um arquivo de código-fonte em Python (extensão .py).

'''
ATENÇÃO:

- Se você optar por mandar mais de um tipo de evidência, os arquivos devem estar compactados no formato .rar ou .zip.

-  Sempre que você consultar outros materiais e/ou conteúdos de terceiros, lembre-se de citá-los corretamente atribuindo as devidas autorias. 

- Evite compartilhar sua resolução com colegas da turma. Preserve sua autoria e evite transtornos na replicação de sua resposta.

- Antes de enviar o arquivo, certifique-se de que respondeu a todas a perguntas. Após o envio não são permitidas alterações. Por favor, não insista. 

- Não são permitidas correções parciais no decorrer do módulo, ou seja, o famoso: “professor veja se minha atividade está certa?”. Isso invalida seu processo avaliativo. 

- Lembre-se que a interpretação da atividade também faz parte da avaliação.

'''

# Iniciando o script:

# Importando as bibliotecas:
from funcoes import (id_livro, limpar, menu, nome_autor, nome_editora, 
                    nome_livro, livros, verificar_arquivo, mostrar_livros,
                    fechar_arquivo, limpar_arquivo, contador_livros)
from time import sleep
from tqdm import tqdm

# Variáveis:
ids_usadas = []
quantidade_cadastro = contador_livros()
opcao = None
voltar = None

# Iniciando o programa

# Limpando a tela
limpar()

# Barra de inicialização
print('Iniciando o programa...\n')
sleep(1)
for i in tqdm(range(1, 6)):
    sleep(0.5)

# Repedir o menu até que o usuário escolha a opção 0:
while opcao != 0:
    # Mostrando o menu
    opcao = menu()

    # Verificando a opção escolhida:
    if opcao == 1:
        sleep(0.5)
        print ('Você selecionou a opção 1 (Cadastrar livro)\n')
        limpar()
        # Verificando a quantidade de livros cadastrados (se for maior que 5 sugere limpar o arquivo):
        quantidade_cadastro += 1
        if quantidade_cadastro > 5: 
            sleep(0.5)
            print ('Sistema de cadastro lotado. Não é possível armazenar mais informações!') 
            # Perguntando se o usuário deseja limpar o arquivo:
            while True:
                try:
                    sleep(0.5)
                    limpar_dados = input ('\nDeseja limpar os dados? (S/N): ').upper()
                    if limpar_dados == 'S':
                        verificar = verificar_arquivo()
                        if verificar == False:
                            limpar_arquivo()
                            quantidade_cadastro = 1
                            ids_usadas = []
                            sleep(0.5)
                            print ('Dados limpos com sucesso!\n')
                        break
                    elif limpar_dados == 'N':
                        sleep(0.5)
                        print ('\nNão será possível armazenar mais informações!')
                        sleep(1)
                        break
                    else:
                        sleep(0.5)
                        print ('\nOpção Invalida!\n')
                        sleep(2)
                except ValueError:
                    sleep(0.5)
                    print ('\nOpção inválida!\n')
                    sleep(2)
            if limpar_dados == 'N':
                #voltar menu
                continue
        # Gerando o código do livro e verificando se já existe:
        sleep(0.5)
        print(f'Livro {quantidade_cadastro}')
        id = id_livro()
        sleep(0.5)
        if id not in ids_usadas: print (f'Código do livro: {id}\n') 
        else: 
            id = id_livro()
            sleep(0.5)
            sleep(0.5)
            print (f'Código do livro: {id}\n')

        # Recebendo os dados do livro:

        livro = nome_livro()
        autor = nome_autor()
        editora = nome_editora()

        # Salvando os dados no arquivo:
        livro = livros(id, livro, autor, editora)
        sleep(0.5)
        print ('\nLivro cadastrado com sucesso!')
        sleep(2)

    # Verificando a opção escolhida:
    elif opcao == 2:
        limpar()
        sleep(0.5)
        print ('Você selecionou a opção 2 (Mostrar livros)\n')
        # Verificando se o arquivo está vazio:
        arquivo = verificar_arquivo()

        # Se o arquivo estiver vazio, mostra uma mensagem de erro:
        if arquivo == True:
            sleep(0.5)
            print ('\nNão há livros cadastrados')
            while voltar != 's':
                mostrar_livros()
                try:    
                    sleep(0.5)
                    voltar = input('\nDeseja voltar ao menu? (s/n): ').upper()
                    if voltar == 'S':
                        break
                except ValueError:
                    sleep(0.5)
                    print ('\nOpção inválida!')

        # Se o arquivo não estiver vazio, mostra os livros:
        else:
            while voltar != 's':
                mostrar_livros()
                try:
                    sleep(0.5)
                    voltar = input('\nDeseja voltar ao menu? (s/n): ').upper()
                    if voltar == 'S':
                        break
                except ValueError:
                    sleep(0.5)
                    print ('\nOpção inválida!')

    # Verificando a opção escolhida:
    # Se a opção for 0, fecha o programa:
    elif opcao == 0:
        limpar()
        sleep(0.5)
        print ('Você selecionou a opção 0 (Encerrar)\n')
        sleep(0.5)
        print ('Programa encerrado!')
        sleep(0.5)
        fechar_arquivo()
        exit()
