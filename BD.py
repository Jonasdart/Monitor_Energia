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
            self.cursor = None
            self.conectado = False

      # FUNÇÃO PARA FAZER LOGIN NO BANCO DE DADOS
      def conecta(self, cred):
            self.cred = cred
            try:
                  self.conn = mdb.connect(self.cred[0], self.cred[1], self.cred[2], self.cred[3])
            except:
                  self.conectado = False
                  raise exception("Não Foi Possível Conectar!")
            else:
                  print("\t\t\tConectado com Sucesso!")
                  self.conectado = True
                  self.cursor = self.conn.cursor()

      def horario(self):
            #AQUI PEGAMOS A HORA E DATA ATUAL
            data = datetime.now()
            #AQUI RETORNAMOS A HORA ATUAL EM INTEIRO
            hora = [int(data.strftime('%H')), int(data.strftime('%M'))]
            return hora

      def data(self):
            #AQUI PEGAMOS A HORA E DATA ATUAL
            data = datetime.now()
            #AQUI RETORNAMOS UMA STRING COM A DATA ATUAL
            return data.strftime('%Y-%m-%d')

      def first(self):
            dias = duzz(self.cred).tabelas()
            cond = False
            for i in range(len(dias)):
                  for c in range(len(dias[i])):
                        if self.date in dias[i][c]:
                              cond = True
            if not cond:
                  duzz(self.cred).criar_table(self.date)
      
      def envia(self, cred):
                        
            #PEGANDO A AUTENTICAÇÃO DO BD
            self.cred = cred
            #PEGANDO A HORA
            horario = self.horario()
            #ORGANIZANDO O TXT
            ORG().organiza(horario)
            #PEGANDO DADOS ORGANIZADOS
            dados = ORG().organiza_BD()
            #SALVANDO O VALOR DO CONSUMO
            self.potencia = float(dados[1])
            self.hora = dados[0]
            #SALVANDO O DIA AO QUAL FOI FEITO O CONSUMO
            self.date = self.data()
            #FAZENDO BACKUP DO ARQUIVO COM OS DADOS
            ORG().backup(self.date, horario[0])  

            #SUBINDO DADOS AO BANCO DE DADOS
            self.first()
            duzz(self.cred).subir_dado(dia = self.date, hora =  self.hora, potencia = self.potencia) #Subimos os dados
            os.remove("backup/dados.txt")
      
