class Sintatico(object):
    def __init__(self):
        self.tokens = []
        self.lista = []
        self.tabela = []
        self.tabela_declaracao = {}
        self.elemento = ["NUM", " ID ", " Literal ","int","float","char","while","if"]
        self.tipo = ["int","float","char"]
        self.pos_global = -1
        self.indica_erro = 0
        self.warning = 0
        self.cont = 0
        self.flag = 0

    def E(self, simb, lista, pos):
        #Pertence a expressão aritmética
        if(simb in " NUM " or simb in " ID " or simb in "Literal" or simb == "("):
            self.T(simb, lista, pos)
            self.Elinha(simb,list,pos)
            self.logicos(simb,list,pos)
        else:
            self.erro(simb,pos)
            self.indica_erro = 1
            return pos
        return pos
    def logicos(selfself, simb, lista, pos):#logico
        if(simb is ">" or simb is "<"):
            return self.T(simb, lista, pos)
        else:
            return pos
    def T(self, simb,lista, pos):
        if(simb in " NUM " or simb in " ID " or simb in "Literal" or simb == "("):
            self.F(simb, lista, pos)
            self.logicos(simb, lista, pos)
            self.Tlinha(simb, lista, pos)
        else:
            self.erro(simb, pos)
            self.indica_erro = 1
            return pos
        return pos
    def F(self,simb,lista, pos):
        if(simb == "("):
            simb, pos = self.get_next_token(lista, pos)
            self.E(simb, lista, pos)
            if(simb != ")"):
                exit()
        elif(simb in " NUM " in or simb in " ID " or simb in "Literal"):
            simb, pos = self.get_next_token(lista,pos)
            return self.Elinha(simb, lista, pos)
        else:
            self.erro(simb, pos)
            self.indica_erro = 1
            return pos
        return pos
    def get_next_token(self,lista,pos):
        #captura proximo token



