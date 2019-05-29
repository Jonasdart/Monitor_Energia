import MySQLdb as mdb
from SQLManager import SQLManager
import time
from datetime import datetime
from DUZZ import duzz

class BD(SQLManager):
      dados = open('dados.txt', 'r')
      
      def __init__(self):
            #CRIANDO CONTROLE DO BD
            self.conn = None
            self.crusor = None
            self.conectado = False
            
            #PEGANDO DADOS PARA AUTENTICAR O BD
            while True:
                  self.cred = ['localhost']
                  if not self.conectado:
                        self.cred.append(input("Informe o Usuario: "))
                        self.cred.append(input("Digite a Senha: "))
                        self.cred.append("dados_brutos")
                        try:
                              #CHAMANDO A FUNÇÃO DE LOGIN
                              self.conecta(self.cred)
                        except:
                              #CASO NAO CONECTE SOLICITAR OS DADOS NOVAMENTE
                              print("DADOS NAO CONFEREM")
                              self.cred.clear()
                        else:
                              #CASO CONECTE SAIR DA REPETIÇÃO E SEGUIR EXECUTANDO
                              if self.conectado is True:
                                    break
                  else:
                        break

      # FUNÇÃO PARA FAZER LOGIN NO BANCO DE DADOS
      def conecta(self, lista):
            self.lista = lista
            print(self.lista)
            try:
                  self.conn = mdb.connect(self.lista[0], self.lista[1], self.lista[2], self.lista[3])
            except:
                  print("NAO CONECTOU")
                  self.conectado = False
            else:
                  print("Conectado com Sucesso!")
                  self.conectado = True
                  self.cursor = self.conn.cursor()

      
nome = BD().horario()
