from matplotlib.pyplot import *
from pylab import *
from tkinter import *
from DUZZ import duzz
from BD import BD
from SQLManager import *
from organiza import ORG

class tela(SQLManager):
    def __init__(self):
        self.potencia = list()
        self.horas = list()
        
        self.m_menu()

    def f_dias(self):
        self.dia = list()
        self.dias = duzz(self.cred).tabelas()
        for dia in self.dias:
            self.dia.append(ORG().trata(str(dia)))

    def dia_mes(self, mes):
        dias = self.pega_item(2, mes = mes)
        retorno = list()
        for dia in dias:
            retorno.append(f"2019-{mes}-{dia}")

        return retorno
                
    def grafico(self, ref, tipo):
        """
        return is False
        
        PLOTA O GRAFICO DESEJADO,
        SENDO TIPO:
                    1 = GRAFICO MENSAL;
                    2 = GRAFICO DIARIO;
        SENDO REF:
                    VALOR REFERENTE AO DIA/MES
        """
        
        self.f_dias()
        dados = self.dados(ref, tipo)
        eixo_x = dados[0]
        eixo_y = dados[1]
        #SE O TIPO DE GRAFICO FOR MENSAL
        if tipo == 1:
            posicao = arange(len(eixo_x))
            bar(posicao, eixo_y, align="center")
            xticks(posicao, eixo_x, rotation = 20)
            grid(True)

            matplotlib.pyplot.ylim(0, 1.5)
            matplotlib.pyplot.title(f" Consumo de energia mês {ref}")
            matplotlib.pyplot.xlabel("Dias")
            matplotlib.pyplot.ylabel("Consumo KWh")
            matplotlib.pyplot.show()
        #SE O TIPO DE GRAFICO FOR DIARIO
        else:
            posicao = arange(len(eixo_x))
            bar(posicao, eixo_y, align="center")
            xticks(posicao, eixo_x, rotation = 20)
            grid(True)

            matplotlib.pyplot.ylim(0, 0.2)
            matplotlib.pyplot.title(f" Consumo de energia dia {ref}")
            matplotlib.pyplot.xlabel("Horas")
            matplotlib.pyplot.ylabel("Consumo KWh")
            matplotlib.pyplot.show()
            

    def dados(self, ref, tipo):
        """
        return is True
        
        RETORNA OS DADOS PARA PLOTAR NO GRAFICO,
        SENDO TIPO:
                    1 = GRAFICO MENSAL;
                    2 = GRAFICO DIARIO;
        SENDO REF:
                    VALOR REFERENTE AO DIA/MES
        """
        
        retorno = list()
        
        if tipo == 1:
            dados = list()
            kwh = list()
            dias = self.dia_mes(mes = ref)
            for dia in dias:
                conta = 0
                kw = 0.0
                horas = duzz(self.cred).colunas(dia)
                for hora in horas:
                    pot_hora = 0.0
                    dados = duzz(self.cred).buscar_dados(dia, hora)
                    for dado in dados:
                        potencia = ORG().trata_potencia(str(dado))
                        pot_hora += float(potencia)
                        kw += float(potencia)
                    if pot_hora > 0:
                        conta += 1
                kw = kw / (1800 * conta)
                kw = kw / 1000
                kwh.append(kw)
                
            #ADICIONANDO NA LISTA DE RETORNO OS DIAS E AS LEITURAS
            retorno.append(dias)        #EIXO X = 0
            retorno.append(kwh)         #EIXO y = 1
            
        else:
            kwh = list()
            horas = list()
            horas.append(duzz(self.cred).colunas(ref))
            for hora in horas[0]:
                dados = duzz(self.cred).buscar_dados(ref, hora)
                kw = 0.0
                for dado in dados:
                    potencia = ORG().trata_potencia(str(dado))
                    kw += float(potencia)
                kw = (kw / 1800) / 1000
                kwh.append(kw)
            #ADICIONANDO NA LISTA DE RETORNO AS HORAS E AS LEITURAS
            retorno.append(horas[0])    #EIXO X = 0
            retorno.append(kwh)         #EIXO Y = 1
            
        return retorno

    def tela_inicial(self):
        self.menu.destroy()
        self.menu = Tk()
        self.menu.title("Monitoramento - Sabrina")
        self.menu["bg"] = "#040c31"
        self.menu.geometry("1060x580+0+0")

        self.logoff = Button(self.menu, text = "Fazer Log-off", bg = "yellow", fg = "black", height = "10", width = "20", bd = "10", relief = "flat")
        self.logoff["command"] = self.deslogar

        self.diario = Button(self.menu, text = "Monitoramento Diario", height = "10", width = "20", bd = "10", relief = "flat")
        self.mensal = Button(self.menu, text = "Monitoramento Mensal",height = "10", width = "20", bd = "10", relief = "flat")
        self.diario["command"] = self.tela_diario
        self.mensal["command"] = self.tela_mensal
        
        self.logoff.place(x = "188", y = "150")
        self.diario.place(x = "422", y = "150")
        self.mensal.place(x = "660", y = "150")

        self.menu.mainloop()

    def pega_item(self, item, mes = None):
        
        """
        retorna os itens pedidos
        sendo:
                0 = ANO;
                1 = MES;
                2 = DIA;
                
        """

        self.retorno = list()
        lista = list()
        dias = duzz(self.cred).tabelas()

        if item == 2:
            try:
                mes != None
            except:
                raise exception("O Mês deve ser passado como argumento")
            else:
                for dia in dias:
                    lista.append(ORG().trata(str(dia)))
                for i in lista:
                    retorno = ORG().data(i)
                    if retorno[1] == mes:
                        self.retorno.append(str(retorno[item]))

        else:
        
            for dia in dias:
                lista.append(ORG().trata(str(dia)))
            for i in lista:
                retorno = ORG().data(i)
                self.retorno.append(str(retorno[item]))

        return sorted(set(self.retorno))
        

    def tela_mensal(self):
        self.menu.destroy()
        self.menu = Tk()
        self.menu.title("Monitoramento - Sabrina")
        self.menu.geometry("1060x380+0+0")
        #TITULO
        titulo = Label(self.menu, text = "MESES MONITORADOS", width = "30", foreground = "white", bg = "#040c31")
        titulo.grid(row = 0, column = 0)

        self.voltar = Button(self.menu, text = "Voltar", bg = "#040c31", fg = "white")
        self.voltar["command"] = self.tela_inicial
        
        meses = self.pega_item(1)
        
        i = 0
        while i < len(meses):
            valor = meses[i]
            self.exibir_botao(i, valor, tipo = 1)
            i += 1

        self.voltar.grid()
        self.menu.mainloop()

    def exibir_botao(self, i, valor, tipo):
        botao = Button(self.menu, text=f"{valor}", command = lambda: self.grafico(valor, tipo))    
        botao.grid()

    def tela_diario(self):
        self.menu.destroy()
        self.menu = Tk()
        self.menu.title("Monitoramento - Sabrina")
        self.menu.geometry("1060x380+0+0")
        #TITULO
        titulo = Label(self.menu, text = "DIAS MONITORADOS", width = "30", foreground = "white", bg = "#040c31")
        titulo.grid(row = 0, column = 0)

        self.voltar = Button(self.menu, text = "Voltar", bg = "#040c31", fg = "white")
        self.voltar["command"] = self.tela_inicial
        

        self.f_dias()
        i = 0
        while i < len(self.dia):
            valor = self.dia[i]
            self.exibir_botao(i, valor, tipo = 2)
            i += 1

        self.voltar.grid()
        self.menu.mainloop()

    def menu_login(self):

        # POSICIONANDO A TELA

        ## AQUI CONFIGURAMOS OS CAMPOS DE TEXTO ##
        lbl1 = Label(self.menu, text = "Login: ", width = "30", foreground = "white", bg = "#040c31")
        lbl2 = Label(self.menu, text = "Senha: ", width = "30", foreground = "white", bg = "#040c31")
        self.lbl_erro = Label(self.menu,text="", width = "35", bd = "10", relief = "flat",
                              foreground = "white", bg = "#040c31")
        self.pega_login = Entry(self.menu, width = "30", bd = "10", relief = "flat")
        self.pega_senha = Entry(self.menu, width = "30", bd = "10", relief = "flat", show = "*")
        botao = Button(self.menu, text = "ENTRAR", width = "35", bd = "10", relief = "flat")
        lbl1.pack(padx = "10", pady = "10")
        self.pega_login.pack(padx = "10", pady = "10")
        lbl2.pack(padx = "10", pady = "10")
        self.pega_senha.pack(padx = "10", pady = "10")
        botao.pack(padx = "10", pady = "10")
        #self.lbl_erro.pack()

        # PREPARANDO O LOGIN COM AS CREDENCIAIS

        botao["command"] = self.confirma_login

    def confirma_login(self):
        self.cred = ["localhost"]
        self.cred.append(self.pega_login.get())
        self.cred.append(self.pega_senha.get())
        self.cred.append("Consumo")
        try:
            BD().conecta(self.cred)
        except:
            self.cred.clear()
        else:
            self.tela_inicial()

    def deslogar(self):
        self.menu.destroy()
        self.m_menu()

    def m_menu(self):
        self.menu = Tk()
        self.menu.title("Monitor - Monitoramento de Consumo")
        self.menu["bg"] = "#040c31"
        self.menu.geometry("360x300+0+0")
        self.menu_login()
        self.menu.mainloop()

grafico = tela()
