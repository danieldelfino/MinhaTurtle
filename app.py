from turtle import Turtle

t = Turtle()


def obter_distancia():
    resposta = int(input('Quantos pixels devemos movimentar para a frente?'))
    return resposta


def rotacionar_turtle(Turtle):
    movimentar_para_lado = input(
        'Rotacionar para d:direita, e:esquerda, n:rotacionar')
    if movimentar_para_lado == 'd':
        rotacionar_para_direita(Turtle)
    elif movimentar_para_lado == 'e':
        rotacionar_para_esquerda(Turtle)


def rotacionar_para_direita(Turtle):
    angulo = int(input('Quanto para a direita devemos rotacionar?'))
    t.right(angulo)


def rotacionar_para_esquerda(Turtle):
    angulo = int(input('Quanto rotacionar para a esquerda?'))
    t.left(angulo)


while True:
    direcao = input('Para qual direção devemos ir? "f:frente ou "t:tras"')
    if direcao == 'f':
        distancia = obter_distancia()
        rotacionar_turtle(t)
        t.forward(distancia)
        if direcao == 't':
            distancia = obter_distancia()
            rotacionar_turtle(t)
            t.backward(distancia)
        resposta = input('Deseja continuar andando?')
        if resposta not in ('sim', 's'):
            break