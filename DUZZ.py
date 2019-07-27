import MySQLdb as mdb
from SQLManager import SQLManager

class duzz(SQLManager):

      def __init__(self, lista):
            super().__init__()
            self.conn = None
            self.cursor = None
            self.lista = lista
            try:
                  self.conn = mdb.connect(self.lista[0], self.lista[1], self.lista[2], self.lista[3])
            except:
                  raise Exception("Não Foi Possível Acessar o Banco de Dados!")
            else:
                  conectado = True
                  self.cursor = self.conn.cursor()

      def colunas(self, table):
            """
            Descobrindo as Colunas da Tabela
            :param nome_da_tabela:
            :return:

            """
            # para criar o comando em mysql
            super().query_columns(table)

            # Recebendo a lista com os nomes das colunas
            result = self.final_com_retorno()

            # Retornando a lista com os nomes das colunas
            return [r[0] for r in result]

      def tabelas(self):
            try:
                  super().mostrar_tabelas()
            except:
                  print("Não Foi Possível Fazer Solicitação!")
            else:
                  tabelas = self.final_com_retorno()
                  return tabelas

      def buscar_dados(self, tabela, coluna):
            try:
                  super().selecionar(tabela = tabela, coluna = coluna)
            except:
                  print("Não Foi Possivel Solicitar Dados ao BD!")
            else:
                  dados = self.final_com_retorno()
                  
                  return dados

    #FUNÇÃO PARA SALVAR DADOS NO BD
            
      def final_sem_retorno(self):
            try:
                  self.cursor.execute(self.query)
            except:
                  raise Exception("Não Foi Possível Salvar Dados no Banco de Dados!")
            else:
                  self.conn.commit()

      #FUNÇÃO PARA LER DADOS DO BD

      def final_com_retorno(self):
            try:
                  self.cursor.execute(self.query)
            except:
                  raise Exception("Não Foi Possível Usar Dados do Banco de Dados!")
            else:
                  return self.cursor.fetchall()

      def criar_table(self, dia):
            try:
                  super().create_table(name = dia)
            except:
                  print(f"NAO FOI POSSIVEL CRIAR A TABELA {dia}")
            else:
                  self.final_sem_retorno()

      def subir_dado(self, dia, hora, potencia):
            """para atualizar e retirar o excesso de linhas do BD, ultimo comentario"""      
            #SE NMR DE DADOS INSERIDOS FOREM MENOR QUE A QUANTIDADE DA HORA ATUAL
            try:
                  super().insere(tabela = dia, hora = hora, consumo = potencia)
            except:
                  print("\tNão Foi Possível Subir Os Dados Ao BD!\n")
            else:
                  self.final_sem_retorno()
                  print(f"\n\tDados do dia {dia} - hora {hora} Salvos com Sucesso\n")
                  """else:
                        try:
                              super().deletar(tabela = dia, coluna = hora)
                        except:
                              print("\tNão Foi Possível Apagar Os Dados Do BD!")
                        else:
                              print(f"\tDados irrelevantes do dia {dia} - hora {hora} Apagados com Sucesso")
                              cond = 1
                              self.final_sem_retorno()  
                  """
      def verifica(self, dia, hora):
            try:
                  super().selecionar(tabela = dia, coluna = hora)
            except:
                  print("Não Foi Possível Verificar a Quantidade de Dados Alocados")
            else:
                  quantidade = self.final_com_retorno()
                  return len(quantidade)
            
