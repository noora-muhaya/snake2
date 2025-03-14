
import turtle
import time
import random #gera numeros aleatórios
import winsound # tocar sons 
import tkinter as tk 

delay = 0.1 # tempo de espera entre cada movimento da cobra
score=0 #pontuação atual do jogador 
high_score=0  #maior pontuação registrada

def iniciar_jogo():
    global score, high_score, delay
    tela_inicio.destroy()#fecha a tela iniciar

#configurações de tela
t1=turtle.Screen()
t1.title("trabalho final-jogo de cobra")
t1.bgcolor("#D1A9A9")
t1.setup(width=600, height=600)
t1.tracer(0) #Controla a atualização da tela (0 para desativar animação automática)

#a cabeça de cobra
cobra=turtle.Turtle()
cobra.speed(0)
cobra.shape("square")
cobra.color("black")
cobra.penup()
cobra.goto(0,0)
cobra.direction="stop" #Define a direção inicial como parada

#comida de cobra
comida=turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

tamanho=[] #armazenar os segmentos do corpo da cobra

t2=turtle.Turtle()  #tartaruga que escreve a pontuação
t2.speed(0)
t2.shape("square")
t2.color("white")
t2.penup()
t2.hideturtle()
t2.goto(0,260)
t2.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

#funções de movimento de cobra
def cima():
    if cobra.direction != "down":
        cobra.direction="up"

def baixo():
    if cobra.direction != "up":
        cobra.direction="down"

def esquerda():
    if cobra.direction != "right":
        cobra.direction="left"

def direita():
    if cobra.direction != "left":
        cobra.direction="right"

def mover(): #move a cabeça de cobra na direção 
    if cobra.direction == "up":
        y=cobra.ycor()
        cobra.sety(y+20)

    if cobra.direction == "down":
        y=cobra.ycor()
        cobra.sety(y-20)

    if cobra.direction == "left":
        x=cobra.xcor()
        cobra.setx(x-20)

    if cobra.direction == "right":
        x=cobra.xcor()
        cobra.setx(x+20)
        
#controles de teclado
t1.listen()
t1.onkeypress(cima,"Up")
t1.onkeypress(baixo,"Down")
t1.onkeypress(esquerda,"Left")
t1.onkeypress(direita,"Right")

#função de som
def play_sound(sound_file, time=0):
    winsound.PlaySound(sound_file, winsound.SND_ASYNC)
play_sound("The-Pink-Panther-Theme-Music-موسيقى-النمر-الوردي.wav")

while True: ##sempre irá executar
    t1.update() #atualização da tela

    if cobra.xcor()>290 or cobra.xcor()<-290 or cobra.ycor()>290 or cobra.ycor()<-290: #se a cabeça da cobra toca as boras da janela
        time.sleep(1) #o jogo pausa por 1 segundo
        cobra.goto(0,0) #reposicionar no centro da tela
        cobra.direction="stop" # não se mover antes de começar jogar

        for corpo in tamanho:
            corpo.goto(1000,1000) 

        tamanho.clear() #remover os segmentos da cobra
        score=0 #pontuação atual é redefinida para 0
        delay = 0.1 # pausa o jogo

        t2.clear() #limpa a "caneta"
        t2.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) #A pontuação exibida na tela é atualizada para refletir a pontuação atual e a maior pontuação registrada.


    if cobra.distance(comida)<20: #determinar se a cobra "comeu" a comida.
        x=random.randint(-285,285)
        y=random.randint(-285,285)
        comida.goto(x,y) # comida é movida para uma nova posição aleatória na tela

        novo_corpo=turtle.Turtle() #cria mais um pedaço do corpo
        novo_corpo.speed(0)
        novo_corpo.shape("square")
        novo_corpo.color("brown")
        novo_corpo.penup()
        tamanho.append(novo_corpo) #a lista do tamanho ganha mais um corpo
        #adicionar um novo segmento ao corpo da cobra
        delay -= 0.001
        score+=10 # a pontuação aumenta

        if score > high_score: # verifica a pontuação atual e a maior pontuação
            high_score = score
        t2.clear()
        t2.write("Score: {}  High Score: {}".format(score,high_score),align="center",font=("Courier", 24, "normal"))
        #Atualização da Pontuação na Tela
    
    for index in range(len(tamanho)-1,0,-1): #posiciona o corpo
        x=tamanho[index-1].xcor() #o pedaço do corpo assume a posição do anterior
        y=tamanho[index-1].ycor()
        tamanho[index].goto(x,y)

    if len(tamanho)>0: # faz o corpo seguir a cobra
        x=cobra.xcor()
        y=cobra.ycor()
        tamanho[0].goto(x,y)

    mover()

    for corpo in tamanho:
        if corpo.distance(cobra)<20: # verifica se a cobra encostou no próprio corpo 
            time.sleep(1)
            cobra.goto(0,0) #volta a origem
            cobra.direction="stop"

            for corpo in tamanho:
                corpo.goto(1000,1000) #os pedaços do corpo saem da tela

            tamanho.clear() #apaga o tamanho do corpo, a quantidade fica 0

            score = 0

            delay = 0.1

            t2.clear()
            t2.write("Score: {}  High Score: {}".format(score, high_score), align="center",font=("Courier", 24, "normal"))

  time.sleep(delay)


tela_inicio = tk.Tk() # criação da tela de início
tela_inicio.title("Tela de Início")

botao_iniciar = tk.Button(tela_inicio, text="PLAY", command=iniciar_jogo, font=("Courier", 100)) #cria botão de inicio
botao_iniciar.pack(pady=300)

tela_inicio.mainloop()
