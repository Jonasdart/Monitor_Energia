import time
from datetime import datetime
from serial import Serial
from organiza import ORG
from BD import BD

#PEGANDO DADOS PARA AUTENTICAR O BD
while True:
      cred = ['localhost']
      cred.append(input("Informe o Usuario: "))
      cred.append(input("Digite a Senha: "))
      cred.append("Consumo")
      try:
            #CHAMANDO A FUNÇÃO DE LOGIN
            BD().conecta(cred)
      except:
            #CASO NAO CONECTE SOLICITAR OS DADOS NOVAMENTE
            print("\t\tNAO FOI POSSIVEL ACESSAR MODULO LOGIN")
            cred.clear()
      else:
            #CASO CONECTE AO BD, TENTAR SE CONECTAR AO ARDUINO
            while True:
                  try:

                        print("\n\n\t\t    Estabelecendo Conexão Com o A.UNO")
                        UNO = Serial('/dev/ttyACM0', 9600)
                        time.sleep(2.5)
                              
                  except:
                        print("\t\t    Não Foi Possível Estabelecer Comunicação Com o A_UNO!")
                  else:
                        print("\t\t    Conexão Com o A.UNO Estabelecida!\n\n")
                        ORG().exclui()
                        break
            break

cond = 0
print("\t\t\tLIMPANDO O BUFFER DA SERIAL...\n\n")
while True:
      time.sleep(1)
      UNO.write(str.encode('1'))
      if cond is not 4:
            time.sleep(0.5)
            leitura = (UNO.readline())
            cond += 1
      else:
            UNO.write(str.encode('0'))
            break
while True:
      segundos = 0
      kw = 0.0
      valor = 0.0
      while segundos is not 60:
            #FAZENDO LEITURA DE CADA MINUTO PEGANDO DADOS A CADA DOIS SEGUNDOS
            time.sleep(2)
            segundos += 2
                        
            #ARQUIVO DOS DADOS BRUTOS
            brutos = open('backup/brutos.txt', 'a')
            UNO.write(str.encode('1'))
            """if segundos is 2 and cond is not 4:
                  time.sleep(0.5)
                  leitura = float(UNO.readline())
                  segundos = 0
                  cond += 1
            else:"""
            
            leitura = UNO.readline()
            try:
                  valor = float(leitura)
            except:
                  print(f"\nErro ao receber dado do arduino, dado aproximado: {leitura}\n")
            else:
                  leitura = valor

            print(f" {segundos} \tSegundos\t", end = " -")
            kw += leitura
            print(f"  {leitura} \tW Consumidos")
            UNO.write(str.encode('0'))
      brutos.write(f"{kw}- \n")
      brutos.close()
      BD().envia(cred)
