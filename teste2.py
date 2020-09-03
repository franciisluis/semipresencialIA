# coding:utf-8
import sys
import re
#https://www.regextester.com/21
tabela_simbolos = []
token_entrada = {}
tabela_erro = []
linha = 0


def verifica_reservada(token):
    """Verifica se determinado token é
    reservado e retorna um código para o mesmo"""
    reservada_list = ['int', 'double', 'float', 'real', 'break', 'case','char', 'const', 'continue']

    for reservada in reservada_list:
        if reservada.lower() == token.replace("\n", "").lower():
            #tokensDeEntrada("[{}]".format(count) + " " + token.replace("\n", "").upper())
            return 1

def verifica_identificador(token):
    if verifica_reservada(token) != 1:
        if re.match(r"^[a-zA-Z]+[a-zA-Z0-9]+|^[a-zA-Z]", token):
            if token not in tabela_simbolos:
                print token
                tabela_simbolos.append(str(token))
                return 1
    return 0
def verifica_constnumer(token):
    if re.match(r"^[0-9]{1,2}", token):
        tabela_simbolos.append(str(token))
        #inteiro
        return 1
    elif re.match(r"^[0-9]{1,2}[.][0-9]{1,2}", token):
        tabela_simbolos.append(str(token))
        return 1
    return 0
        #real
def verifica_comentario(token):
    if re.match(r"^[//]+[a-zA-Z0-9 }{,.^?~=+\-_\/*\-+.\|]+", token):
        tabela_simbolos.append( str(token))
        return 1
        #Comentario
    return 0
def verifica_erro(token, linha):
    tabela_erro.append(str(token))

def open_file():
    """Abre o arquivo de entrada"""
    try:
        nome = sys.argv[1]
        arquivo = open(nome, "r")
    except Exception as e:
        arquivo = open("teste2.c", "r")
    return arquivo
arquivo = open_file()
i=1
for token in arquivo:
    linha = linha + 1
   # print token
    if verifica_reservada(token) == 1:
        token_entrada[linha] = [str(token)]
    elif verifica_identificador(token) == 1:
        token_entrada[linha] = ["IDENTIFICADOR"]
    elif verifica_constnumer(token) == 1:
        token_entrada[linha] = ["NUMERO"]
    elif verifica_comentario(token) == 1:
        token_entrada[linha] = ["COMENTARIO"]
    else:
        tabela_erro = [str(token)]

#for i in token_entrada:
     #   print token_entrada[i]
#for cont in tabela_simbolos:
 # print cont
#for a in tabela_erro:
    #print a

