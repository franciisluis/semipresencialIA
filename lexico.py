# coding:utf-8
import sys
import re
import _collections
import collections
#https://www.regextester.com/21
tabela_simbolos = []
tabela_simbolos.append("Tabela de Símbolos")
token_entrada = {}
tabela_erro = []
tabela_erro.append("Erros nas linhas:")
linha = 0
tabela_temp = []
tabela_temp2 = []
def exibe_imprime(nome, lista):
    """escreve no arquivo de saida"""
    arq = open(nome, "w")
    if(len(lista) == 0):
        arq.write("Lista vazia\n")
    for i in lista:
        arq.write(str(i) + "\n")

def exibe_imprime2(nome, lista):
    """escreve no arquivo de saida"""
    arq = open(nome, "w")
    if (len(lista) == 0):
        arq.write("Lista vazia\n")
    for i in lista:
        arq.write(str(token_entrada[i]) + "\n")

    arq.close()
def verifica_reservada(token):
    """Verifica se determinado token é
    reservado e retorna um código para o mesmo"""
    reservada_list = ['int', 'double', 'float', 'real', 'break', 'case','char', 'const', 'continue']

    for reservada in reservada_list:
        if reservada.lower() == token.replace("\n", "").lower():
            #tokensDeEntrada("[{}]".format(count) + " " + token.replace("\n", "").upper())
            return 1

def verifica_identificador(token,linha):
    if verifica_reservada(token) != 1:
        #if re.fullmatch(r"^[a-zA-Z]+[a-zA-Z0-9]+|^[a-zA-Z]", token):
        #if re.search(r'[\Sa-zA-Z]+[\Sa-zA-Z0-9]+|^[a-zA-Z]', token): FUNCIONA TB se adicionar o re.serarch("")
        if re.findall("^([a-zA-Z][a-zA-Z0-9]*)$", token):
            #if re.search(" ", token):
                #return 0
            #if token not in tabela_simbolos:
            pos = len(tabela_simbolos)
            pos2 = 1
            if str(token) not in tabela_simbolos:
                if token not in tabela_temp: #para guardar os token, para não repetir
                    tabela_temp.append(str(token))
                #print(token)
                    tabela_simbolos.append(str(pos) + " - "+ str(token))
                    if token not in tabela_temp2:
                        tabela_temp2.append(str(token))
            for i in tabela_temp2:
                #print(i)
                if i == token:
                    token_entrada[linha] = [str(linha) + " " + "IDENTIFICADOR" + " " + str(pos2)]
                pos2 = pos2 + 1

            return pos
        return 0
    return 0
def verifica_constnumer(token):
    #if re.match(r"^[0-9]{1,2}", token):
    if re.findall("^([0-9][0-9]{0,1})$", token):
        pos = len(tabela_simbolos)
        pos2 = 1
        if str(token) not in tabela_simbolos:
            if token not in tabela_temp:
                tabela_temp.append((str(token)))
                tabela_simbolos.append(str(pos) + " - "+ str(token))
                if token not in tabela_temp2:
                    tabela_temp2.append(str(token))
        for i in tabela_temp2:
            #print (i)
            if i == token:
                token_entrada[linha] = [str(linha) + " " + "NUMERO INTEIRO" + " " + str(pos2)]
            pos2 = pos2 + 1
        #inteiro
        return 1
    #elif re.match(r"^[0-9]{1,2}[.][0-9]{1,2}", token):
    elif re.findall("^([0-9][0-9][.][0-9][0-9]{0,1})$", token) or re.findall("^([0-9][.][0-9][0-9]{0,1})$",token):
        pos = len(tabela_simbolos)
        pos2 = 1
        if str(token) not in tabela_simbolos:
            if token not in tabela_temp:
                tabela_temp.append(str(token))
                tabela_simbolos.append(str(pos) + " - " + str(token))
                if token not in tabela_temp2:
                    tabela_temp2.append(str(token))
        for i in tabela_temp2:
            #print(i)
            if i == token:
                token_entrada[linha] = [str(linha) + " " + "NUMERO REAL" + " " + str(pos2)]
            pos2 = pos2 + 1
        return pos
    return 0
        #real
def verifica_comentario(token):
    if re.match(r"^[//]+[a-zA-Z0-9 }{,.^?~=+\-_\/*\-+.\|]+", token):
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
    token_entrada[0] =["Tokens de entrada"]
    linha = linha + 1
   # print token
    if verifica_reservada(token) == 1:
        token_entrada[linha] = [str(linha) +" "+ str(token.rstrip('\n'))]
    #elif re.match(r"^[a-zA-Z]+[a-zA-Z0-9]+|^[a-zA-Z]", token):
    elif re.findall("^([a-zA-Z][a-zA-Z0-9]*)$", token):
        verifica_identificador(token,linha)
        #token_entrada[linha] = ["IDENTIFICADOR" + str(pos)]
    #elif re.match(r"^[0-9]{1,2}", token):
    elif re.findall("^([0-9][0-9]{0,1})$", token) or re.findall("^([0-9][0-9][.][0-9][0-9]{0,1})$", token) or re.findall("^([0-9][.][0-9][0-9]{0,1})$",token):
        verifica_constnumer(token)
    #elif re.match(r"^[//]+[a-zA-Z0-9 }{,.^?~=+\-_\/*\-+.\|]+", token):
    elif re.findall("^//",token):
        verifica_comentario(token)
        token_entrada[linha] = [str(linha) +" " + "COMENTARIO"]
    else:
        tabela_erro.append(str(linha)+" "+token)
def imprime():
    for i in token_entrada:
        print(token_entrada[i])
    for cont in tabela_simbolos:
        print(cont)
    for a in tabela_erro:
        print(a)
imprime()
exibe_imprime2("tokens_entrada",token_entrada)
exibe_imprime("tabela_simbolo",tabela_simbolos)
exibe_imprime("lista_erros",tabela_erro)
