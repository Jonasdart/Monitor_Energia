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
      cred.append("dados_brutos")
      try:
            #CHAMANDO A FUNÇÃO DE LOGIN
            BD().conecta(cred)
      except:
            #CASO NAO CONECTE SOLICITAR OS DADOS NOVAMENTE
            print("\t\tNAO FOI POSSIVEL ACESSAR MODULO LOGIN")
            cred.clear()
      else:
            #CASO CONECTE SAIR DA REPETIÇÃO E SEGUIR EXECUTANDO
            break

while True:
      #ARQUIVO DOS DADOS BRUTOS
      brutos = open('backup/brutos.txt', 'a')

      #AQUI PEGAMOS A HORA ATUAL
      data = datetime.now()
      minutos = int(data.strftime('%M'))


      #Configura a serial e a velocidade de transmissao
      if minutos is 0:
            try:
                  print("\n\n\t\t  Estabelecendo Conexão Com o A.UNO")
                  UNO = Serial('/dev/ttyACM0', 9600)
                  
                  
            except:
                  print("\t\t  Não Foi Possível Estabelecer Comunicação Com o A_UNO!")
            else:
                  print("\t\t  Conexão Com o A.UNO Estabelecida!")
                  print(f"\n\n\t\t\tFAZENDO LEITURA DAS {BD().horario()}")
                  print(f"\n\n\t\t\tPROXIMA LEITURA ÀS {BD().horario()+1}")
                  time.sleep(3540)
                  while True:
                        leitura = str(UNO.readline())
                        if len(leitura) > 0:
                              break
                  kwh = ORG().trata(leitura)
                  print(f"\n\t\t\tUso KWh = {kwh}")
                  brutos.write(f"{kwh}\n")
                  brutos.close()
                  BD().envia(cred)
      
      else:
            time.sleep(60)
