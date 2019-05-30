import MySQLdb as mdb
from SQLManager import SQLManager
import time
from datetime import datetime
from DUZZ import duzz
from organiza import ORG
import os
import shutil


class BD(SQLManager):
      
      def __init__(self):
            super().__init__()
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

      def horario(self):
            #AQUI PEGAMOS A HORA E DATA ATUAL
            data = datetime.now()
            #AQUI RETORNAMOS A HORA ATUAL EM INTEIRO
            return int(data.strftime('%H'))

      def data(self):
            #AQUI PEGAMOS A HORA E DATA ATUAL
            data = datetime.now()
            #AQUI RETORNAMOS UMA STRING COM A DATA ATUAL
            return data.strftime('%Y-%m-%d')

      def first(self, hora):
            if hora is 3:
                  duzz(self.cred).criar_table(self.date)
      
      def envia(self):
            hora = self.horario()
            ORG().organiza(hora)
            self.dados = open('backup/dados.txt', 'r')
            itens = self.dados.readline().split("-")
            self.potencia = float(itens[1])
            self.date = self.data()
            #self.first(hora)
            duzz(self.cred).subir_dado(self.date, itens[0], self.potencia)
            
            if hora is 23:
                  self.date = self.data()
                  self.dados.close()
                  ORG().backup(data)
                  time.sleep(60)
