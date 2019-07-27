from datetime import datetime
import os

class ORG(object):
      def __init__(self):
## AQUI TRATAMOS OS DADOS RELEVANTES ##
            self.dados = open("backup/dados.txt", "a")    

      def organiza(self, horario):
            self.brutos = open("backup/brutos.txt", "r")
            for l in self.brutos:
                  self.dados.write(f"{horario}-{l}- \n")
            self.brutos.close()
            self.dados.close()
            os.remove("backup/brutos.txt")

      def backup(self, data, hora):
            self.data = data
            self.hora = hora
            try:
                  ver = open(f'backup/dados-{self.data}.txt', 'r')
            except:
                  with open('backup/dados.txt', 'r') as arquivo_existente, open(f'backup/dados-{self.data}.txt', 'w') as novo_arquivo:
                      for linha in arquivo_existente.readlines():
                          novo_arquivo.write(linha)
            else:
                  ver.close()
                  self.dados.close()
                  self.dados = open("backup/dados.txt", "r")
                  for l in self.dados:
                        backup = open (f'backup/dados-{self.data}.txt', 'a')
                        backup.write(l)
                        backup.close()
            self.dados.close()

      def trata (self, string):
            self.string = string.split("'")
            self.dados.close()
            return self.string[1]

      def data(self, string):
            self.string = string.split("-")
            self.dados.close()
            #retorno[0] = ano = retorno[1] = mes - retorno[2] = dia
            return self.string

      def exclui (self):
            try:
                  os.remove("backup/brutos.txt")
                  os.remove("backup/dados.txt")
            except:
                  pass
            
      def trata_potencia (self, string):
            self.string = string.split("(")
            self.string = self.string[1].split(",")
            self.string = self.string[0]
            return self.string
            
      def organiza_BD(self):
            self.dados = open("backup/dados.txt", "r")
            kw = 0.0
            for itens in self.dados:
                  dados = str(itens)
                  lista = dados.split(",")
                  c = lista[0].split("[")
                  potencia = dados.split("-")
                  potencia = potencia[1]
                  kw += float(potencia)
                  dados = [c[1], kw]
                  return dados
            self.dados.close()
