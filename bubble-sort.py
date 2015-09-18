# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt #importando o módulo matplotlib

bubble = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8] #aqui criamos a lista crua e fora de ordem.
print("Lista original: ", bubble) # imprimindo a lista original fora de ordem

a = 20 #aqui criamos uma variável com o número de itens da lista.
copo = 0 #aqui criamos a variável copo, que utilizaremos para realizar as trocas de itens.
count = 300 #aqui criamos uma contagem bem grande, pra garantir que o programa fará o trabalho completo

plt.figure()
plt.plot(range(a),bubble,'ok')
plt.title("Lista Original")
plt.xlabel(u"Posição")
plt.ylabel("Valor")
plt.savefig("C:/Users/Gam/Documents/pratica-shell/pratica-py-gam/fig/bubble-inicio.png")
plt.show()

while count > 0: #enquanto a variável contagem não se esgotar, o programa roda de novo e de novo.
    for i in range(0,a-1): #o programa irá trabalhar com todos os itens, exceto o último.
        count = count - 1 #a cada vez que ele rodar, a contagem desce um tique.
        if bubble[i] > bubble[i+1]: #cada item da lista é comparado com o item a seguir. Se for maior, ele executa as ações que seguem.
            copo = bubble[i] #o item em questão vai para o copo.
            bubble[i] = bubble[i+1] #o item comparado vira o item em questão.
            bubble[i+1] = copo #o copo vira o item comparado
#efetivamente, o que fizemos foi trocar um item pelo outro.

print("Lista em ordem crescente: ", bubble) #após ele repetir o loop 300 vezes imprimimos, por fim, o resultado.

plt.figure()
plt.plot(range(a),bubble,'ok')
plt.title("Lista Original")
plt.xlabel(u"Posição")
plt.ylabel("Valor")
plt.savefig("C:/Users/Gam/Documents/pratica-shell/pratica-py-gam/fig/bubble-fim.png")
plt.show()

print("Lista dos cinco maiores valores: ", bubble[a-5:]) #aqui ele imprime os cinco maiores valores

print("Lista dos cinco menores valores: ", bubble[:5]) #aqui ele imprime os cinco menores valores