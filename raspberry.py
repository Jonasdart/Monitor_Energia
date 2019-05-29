import time
from datetime import datetime
import RPi.GPIO as GPIO
import serial
import MySQLdb as mdb
from SQLManager import SQLManager

while True:
      #ARQUIVO DOS DADOS BRUTOS
      brutos = open('brutos.txt', 'a')

      #AQUI PEGAMOS A HORA ATUAL
      data = datetime.now()
      minutos = int(data.strftime('%M'))


      #Configura a serial e a velocidade de transmissao
      if minutos is 50:
            try:
                  UNO = serial.Serial("/dev/ttyAMA0", 115200)
                  UNO.open()
            except:
                  print("Não Foi Possível Estabelecer Comunicação Com o A_UNO!")
            else:
                  print("Dados do A_UNO Recebidos Com Sucesso!")
                  GPIO.setmode(GPIO.BOARD)
                  while True:
                        try:
                              kwh = UNO.readlines()
                        except:
                              print("Não Foi Possível Salvar Os Dados!")
                        else:
                              brutos.write(kwh)
                              brutos.close()
                              print("Dados Salvos Com Sucesso!")
                              time.sleep(3600)
                              break
      else:
            time.sleep(60)
