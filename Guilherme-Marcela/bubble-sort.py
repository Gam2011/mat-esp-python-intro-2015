# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt #importando o módulo matplotlib

bubble = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8] #aqui criamos a lista crua e fora de ordem.
print("Lista original: ", bubble) # imprimindo a lista original fora de ordem

a = 20 #aqui criamos uma variável com o número de itens da lista.
copo = 0 #aqui criamos a variável copo, que utilizaremos para realizar as trocas de itens.
count_troca = 0 #criamos um contador para as figuras conforme elas forem trocadas
count_it = 0 #mesma coisa com a iteração

plt.figure() #criamos aqui a figura em branco
plt.plot(range(a),bubble,'ok') #aqui preenchemos-na com os dados crus
plt.title("Lista Original") #título
plt.xlabel(u"Posição") #nomeamos o eixo X
plt.ylabel("Valor") #nomeamos o eixo Y
plt.savefig("fig/bubble-inicio.png") #salvamos a figura na pasta fig
plt.close #fecha a figura

for i in range(0 , a - 1): #vamos fazer ele rodar de novo e de novo.
    for j in range(i + 1, a): #o programa irá trabalhar com todos os itens, exceto o último.

        plt.figure() #criamos aqui a figura em branco
        plt.plot(range(a), bubble, 'ok') #aqui preenchemos-na com os dados crus
        plt.plot(i, bubble[i], 'or') #aqui preenchemos-na com os dados crus
        plt.plot(j, bubble[j], 'ob') #aqui preenchemos-na com os dados crus
        count_it = count_it+1 #aumentamos o contador da iteração que será usado pra nomear a figura
        plt.title(u"Iteração {}".format(count_it)) #título
        plt.xlabel(u"Posição") #nomeamos o eixo X
        plt.ylabel("Valor") #nomeamos o eixo Y
        plt.savefig("fig/bubble-it-{}.png".format(count_it)) #salvamos a figura na pasta fig
        plt.close #fecha a figura

        if bubble[i] > bubble[j]: #cada item da lista é comparado com o item a seguir. Se for maior, ele executa as ações que seguem.
            copo = bubble[i] #o item em questão vai para o copo.
            bubble[i] = bubble[j] #o item comparado vira o item em questão.
            bubble[j] = copo #o copo vira o item comparado
            #efetivamente, o que fizemos foi trocar um item pelo outro.

            plt.figure() #criamos aqui a figura em branco
            plt.plot(range(a),bubble,'ok') #aqui preenchemos-na com os dados após esta troca
            count_troca = count_troca+1 #aumentamos o contador de troca que será usado pra nomear a figura
            plt.title("Troca {}".format(count_troca)) #título
            plt.xlabel(u"Posição") #nomeamos o eixo X
            plt.ylabel("Valor") #nomeamos o eixo Y
            plt.savefig("fig/bubble-troca-{}.png".format(count_troca)) #salvamos a figura na pasta fig
            plt.close #fecha a figura

print("Lista em ordem crescente: ", bubble) #após ele repetir o loop 300 vezes imprimimos, por fim, o resultado.

plt.figure() #criamos aqui a figura em branco
plt.plot(range(a),bubble,'ok') #aqui preenchemos-na com os dados organizados
plt.title("Lista Final") #título
plt.xlabel(u"Posição") #nomeamos o eixo X
plt.ylabel("Valor") #nomeamos o eixo Y
plt.savefig("fig/bubble-fim.png") #salvamos a figura na pasta fig
plt.close #fecha a figura

print("Lista dos cinco maiores valores: ", bubble[a-5:]) #aqui ele imprime os cinco maiores valores

print("Lista dos cinco menores valores: ", bubble[:5]) #aqui ele imprime os cinco menores valores