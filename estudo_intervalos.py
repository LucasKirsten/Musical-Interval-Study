# -*- coding: UTF-8 -*-
from random import randint as r
from Tkinter import *
from tkMessageBox import *

dic = {'C': 'F', 'Db': '2m', 'D': '2M', 'Eb': '3m', 'E': '3M', 'F': '4J', 'F#': '4+', 'Gb': '5-', 'G': '5J', 'G#': '5+', 'Ab': '6m', 'A': '6M', 'Bb': '7m', 'B': '7M'}

class Interface():
    def __init__(self):
        #variaveis necessarias
        toplevel = Tk()
	toplevel.iconbitmap(default='icon.ico')
        self.toplevel = toplevel
        self.toplevel.title('Estudo dos intervalos')
        self.toplevel.minsize(width='300', height='100')
        self.erros = 0
        self.todas_notas = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.todos_intervalos = ['F', '2m', '2M', '3m', '3M', '4J', '4+ 5-', '5J', '5+ 6m', '6M', '7m', '7M']
        self.intervalos = {}        
        self.fonte = ('Arial','12')
        self.escala = 0
        
        #interface inicial
            #menu
        # controle para ver qual a forma de estudo que será feita
        # controle = 1 : Perg: nota; resp: intervalo
        # controle = 2 : Perg: intervalo; resp: nota
        self.controle = IntVar()
        self.controle.set(1)
        menubar = Menu(toplevel)
        formamenu = Menu(menubar, tearoff=0)
        formamenu.add_radiobutton(label='Nota - Intervalo', variable = self.controle, value=1)
        formamenu.add_radiobutton(label='Intervalo - Nota', variable = self.controle, value=2)
        menubar.add_cascade(label="Forma de Estudo", menu=formamenu)
        
        #tutorial de como responder
        def tutorial():
            texto='\tIntervalo:\t\tResposta: \n\
            Fundamental\t\tF \n\
            2ª menor\t\t2m \n\
            2ª maior\t\t2M \n\
            3ª menor\t\t3m \n\
            3ª maior\t\t3M \n\
            4ª justa\t\t4J \n\
            4ª aumentada\t\t4+ \n\
            5ª diminuta\t\t5- \n\
            5ª justa\t\t5J \n\
            5ª aumentada\t\t5+ \n\
            6ª menor\t\t6m \n\
            6ª maior\t\t6M \n\
            7ª menor\t\t7m \n\
            7ª maior\t\t7M \n\n\
            Para intervalos iguais escreva os dois com espaço.\n\
            Exemplos, na ordem correta: \"4+ 5-\" e \"5+ 6m\"'
            showinfo('Tutorial', texto)
        
        optmenu = Menu(menubar, tearoff=0)
        optmenu.add_command(label='Tutorial', command=tutorial)
        optmenu.add_command(label='Voltar Menu', command=self.reiniciar)
        optmenu.add_command(label='Sair', command=toplevel.quit)
        menubar.add_cascade(label='Opções', menu=optmenu)
        
        toplevel.config(menu=menubar)
        
        self.frame_inicial = Frame(toplevel)
        self.frame_inicial.pack()
        texto_inicial = Label(self.frame_inicial, text='Escolha a escala para treinar', font=self.fonte).grid(row=0,column=1)
        botao_do = Button(self.frame_inicial, text='Dó', font=self.fonte, width= 10, command = lambda : self.definir_escala(self.todas_notas.index('C'),True)).grid(row=1,column=0,pady=5)
        botao_re = Button(self.frame_inicial, text='Ré', font=self.fonte, width= 10, command = lambda : self.definir_escala(self.todas_notas.index('D'),True)).grid(row=1,column=1)
        botao_mi = Button(self.frame_inicial, text='Mi', font=self.fonte, width= 10, command = lambda : self.definir_escala(self.todas_notas.index('E'),True)).grid(row=1,column=2)
        botao_fa = Button(self.frame_inicial, text='Fa', font=self.fonte, width= 10, command = lambda : self.definir_escala(self.todas_notas.index('F'),True)).grid(row=2,column=0, pady=5)
        botao_sol = Button(self.frame_inicial, text='Sol', font=self.fonte, width= 10, command = lambda : self.definir_escala(self.todas_notas.index('G'),True)).grid(row=2,column=1)
        botao_la = Button(self.frame_inicial, text='Lá', font=self.fonte, width= 10, command = lambda : self.definir_escala(self.todas_notas.index('A'),True)).grid(row=2,column=2)
        botao_si = Button(self.frame_inicial, text='Si', font=self.fonte, width= 10, command = lambda : self.definir_escala(self.todas_notas.index('B'),True)).grid(row=3,column=1, pady=5)
    
        toplevel.mainloop()    
    
    #confere se a resposta esta correta
    def conferir_resposta(self, event):
        #pega a resposta dada e destroi a widget
        resposta = self.verificaResposta.get()
        self.verificaResposta.destroy()
        
        if (resposta == self.intervalos[self.pratica]):
            del self.intervalos[self.pratica]
            if (len(self.intervalos)==0):
                self.definir_escala(self.escala,False)
                self.notaExibida['text'] = "Voce errou "+str(self.erros)+" vezes!!!"
            else:
                self.iniciar(1)
                return 1
        else:
            self.notaExibida['text'] = "Errado, resposta: "+self.intervalos[self.pratica]
            self.erros = self.erros + 1

        self.botao_proximo = Button(self.frame_principal, text='Próximo', font=self.fonte)
        self.botao_proximo.pack(side=BOTTOM)
        self.botao_proximo.bind('<Button-1>', self.iniciar)
        self.botao_proximo.bind('<Return>', self.iniciar)
        
    def iniciar(self, event):
        # inicia os estudos

        # destrói widgets que não serão usadas
        try:
            self.botao_proximo.destroy()
        except:
            pass
        try:
            self.notaExibida.destroy()
        except:
            pass
        try:
            self.frame_principal.destroy()
        except:
            pass
        self.frame_inicial.destroy()
        
        #frame principal que será sempre usada
        self.frame_principal = Frame(self.toplevel)
        self.frame_principal.pack()
        
        #pega as notas (ou intervalos)
        notas = self.intervalos.keys()
        #número das notas (ou intervalos) musicais
        tamanho_notas = len(notas)-1
        #sorteia um número que equivalerá a alguma nota (ou intervalo)
        pratica = r(0, tamanho_notas)
        #nota (ou intervalo) que será estudado
        self.pratica = notas[pratica]
        
        # exibe a nota
        self.notaExibida = Label(self.frame_principal, text=self.pratica, font=self.fonte)
        self.notaExibida.pack(side=TOP)
        
        # pede a resposta
        self.verificaResposta = Entry(self.frame_principal, font=self.fonte)
        self.verificaResposta.pack(side=BOTTOM)
        self.verificaResposta.bind('<Return>', self.conferir_resposta)
        
    #define a escala correta a ser usada com as notas e intervalos
    def definir_escala(self, escala, inicializar):
        
        #recebe o valor de iteração para a escala selecionada
        self.escala = escala
        
        #impede que um número seja maior do que o número de notas e intervalos, fazendo o número ciclico
        def it(numero):
            valor = numero
            if (numero>(len(self.todas_notas)-1)):
                valor = numero - len(self.todas_notas)
            return valor
        
        #preenche o dicionário que irá conter nota - intervalo (se a variavel de controle=1)
        num = 0;
        while (len(self.intervalos)<len(self.todas_notas)):
            if (self.controle.get()==1):
                self.intervalos[self.todas_notas[it(escala)]] = self.todos_intervalos[it(num)]
            else:
                self.intervalos[self.todos_intervalos[it(num)]] = self.todas_notas[it(escala)]
            escala = escala + 1
            num = num + 1
        
        #verifica se foi realmente os botões iniciais que chamaram a função
        if (inicializar):
            #inicia os estudos
            self.iniciar(1)
        
    # reiniciar para escolher opções e/ou escala
    def reiniciar(self):
        self.toplevel.destroy()
        self.__init__()

#inicialização do objeto interface
Interface()
		