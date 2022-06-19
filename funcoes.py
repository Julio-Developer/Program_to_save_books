# -*- coding: utf-8 -*-

# import de variaveis
import os
from random import randint
from time import sleep

# Função para limpar terminal de acordo com o sistema operacional
def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Função para mostrar o menu de opções e receber a opção escolhida pelo usuário
def menu():
    # Boas vindas
    limpar()
    print('Bem vindo ao sistema de cadastro de livros!')
    sleep(1)
    print('\nMenu')
    print('----\n')
    sleep(1)
    print('1. Inserir um novo cadastro')
    sleep(0.5)
    print('2. Mostrar todos os cadastros')
    sleep(0.5)
    print('0. Encerrar\n')
    sleep(0.5)

    # Recebendo a opção e verificando se é válida:
    while True:
        try:
            sleep(0.5)
            opcao = int(input('Digite a opção desejada: ')) 
            if opcao == 1 or opcao == 2 or opcao == 0:
                break
            else:
                sleep(0.5)
                print('Opção inválida!')    
                continue
        except ValueError: 
            sleep(0.5)
            print ('\nOpção inválida!')
    return opcao

# Função para pegar os dados do livro
def id_livro():
    id = randint(0,1000)
    return id

# Funcã́o para o nome do autor
def nome_autor():
    sleep(0.5)
    nome = str(input('Digite o nome do autor: '))
    return nome

# Função para o nome do livro
def nome_livro():
    sleep(0.5)
    nome = str(input('Digite o nome do livro: '))
    return nome

# Função nome editora
def nome_editora():
    sleep(0.5)
    nome = str(input('Digite o nome da editora: '))
    return nome

# Função pra criar e inserir dados no arquivo
def livros(id, nome_livro, nome_autor, nome_editora):
    with open('livros.txt', 'a') as livros:
        dados = [id, nome_livro, nome_autor, nome_editora]
        livros.write(
            f'ID do Livro: {id} > Nome do Livro: {nome_livro} > Nome do Autor: {nome_autor} > Nome da Editora: {nome_editora}\n'
            )
    return dados

# Verificando se o arquivo está vazio
def verificar_arquivo():
    with open('livros.txt', 'r') as livros:
        if livros.read() == '':
            return True
        else:
            return False

# Mostrar os livros cadastrados
def mostrar_livros():
    with open('livros.txt', 'r') as livros:
        for linha in livros:
            print(linha)
            sleep(0.5)

# Função para fechar o arquivo
def fechar_arquivo():
    with open('livros.txt', 'r') as livros:
        livros.close()

# Função para limpar o arquivo
def limpar_arquivo():
    with open('livros.txt', 'w') as livros:
        livros.close()

# contador de livros
def contador_livros():
    with open('livros.txt', 'r') as livros:
        contador = 0
        for linha in livros:
            contador += 1
        return contador