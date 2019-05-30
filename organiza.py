from datetime import datetime
import os

class ORG(object):
      def __init__(self):
## AQUI ABRIMOS OS DOIS ARQUIVOS ONDE SALVAMOS OS DADOS RELEVANTES ##
            self.brutos = open("backup/brutos.txt", "r")
            self.dados = open("backup/dados.txt", "a")
            

      def organiza(self, horario):
            for l in self.brutos:
                  self.dados.write(f"{horario}-{l}\n")
            self.brutos.close()
            self.dados.close()

      def backup(self, data):
            with open('backup/brutos.txt', 'r') as arquivo_existente, open(f'backup/brutos-{data}.txt', 'w') as novo_arquivo:
                for linha in arquivo_existente.readlines():
                    novo_arquivo.write(linha)
            with open('backup/dados.txt', 'r') as arquivo_existente, open(f'backup/dados-{data}.txt', 'w') as novo_arquivo:
                for linha in arquivo_existente.readlines():
                    novo_arquivo.write(linha)
            self.brutos.close()
            self.dados.close()
            os.remove("backup/dados.txt")
            os.remove("backup/brutos.txt")
