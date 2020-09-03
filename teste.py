# coding:utf-8
import sys
import re
tabela_token = {}
token_geral = []
def verifica_reservada(token):
    """Verifica se determinado token é
    reservado e retorna um código para o mesmo"""
    reservada_list = ['int', 'double', 'float', 'real', 'break', 'case',
                      'char', 'const', 'continue']
def open_file:
    """Abre o arquivo de entrada"""
    try:
        nome = sys.argv[1]
        arquivo = open(nome, "r")
    except Exception as e:
        arquivo = open("teste2.c", "r")
    return arquivo
arquivo = open_file()

for i in arquivo:
    linha = linha + 1
    coluna = 0
    for k in i:
        id_tabela = (id_tabela + 1)
        coluna = coluna + 1
        if estado is 0:
            if k is "/" and i[coluna] is "/" and estado == 0 and estado != 4:
                """Comentario"""
                estado = 4
            if re.search(r"^(#)|[/]{2}", i) and estado == 0 and estado != 4:
                """ignora o stdio e linha comentada"""
                break
            if re.match(r"([A-Za-z_])", k) and estado == 0 and estado != 4:
                estado = 1
            if re.match(r"[0-9]", k) and estado == 0 and estado != 4:
                estado = 2
            if re.match(r"[\"]", k) and estado == 0 and estado != 4:
                estado = 3
            if ver_num(k) and ver_iden(k) and estado == 0 and estado != 4:
                verifica_erro(k, token_geral, lista_erros, linha, coluna)

        if estado is 1:
            if re.match(r"(^[a-zA-Z]+[a-zA-Z0-9]+|^[a-zA-Z])", k):
                token = token + k
            if verifica_reservada(token):
                tabela_token[id_tabela] = [str(verifica_reservada(token))]
                token_geral.append([+str(verifica_reservada(token)), token, id_tabela])

        if estado is 2:



