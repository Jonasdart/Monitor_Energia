from datetime import datetime

class pai(object):
      def __init__(self):
## AQUI ABRIMOS OS DOIS ARQUIVOS ONDE SALVAMOS OS DADOS RELEVANTES ##
            self.brutos = open("brutos.txt", "r")
            self.dados = open("dados.txt", "a")
            
            self.horario()
      
      def horario(self):
            #AQUI PEGAMOS A HORA ATUAL
            self.data = datetime.now()
            #AQUI TRANSFORMAMOS A HORA ATUAL EM INTEIRO
            self.h_atual = int(self.data.strftime('%H'))

      def organiza(self):
            for l in self.brutos:
                  self.dados.write(f"{self.h_atual}-{l}")
                  print(l)
            self.brutos.close()
            self.dados.close()

pai = pai().organiza()
