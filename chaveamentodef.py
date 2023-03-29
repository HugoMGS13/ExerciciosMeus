import random
def partida(timew,timer):
    lista = [timew,timer]
    global result
    result = random.choice(lista)
    print(f"A partida será entre {timew} e {timer}")
    print("O vencedor dessa partida foi" , result)
times = input("Escreva 8 times do Pará para o campeonato (separados por vírgula): \n")
lista = times.split(",")
while len(lista) < 8 or len(lista) > 8:
    print("Escreva exatamente 8 times")
    times = input("Escreva 8 times do Pará para o campeonato (separados por vírgula): \n")
    lista = times.split(",")
if len(lista) == 8:
    t1,t2,t3,t4,t5,t6,t7,t8 = times.split(",")
    print("### Vamos para as quartas de final ###")
    partida(t1,t2)
    semi1 = result
    partida(t3,t4)
    semi2 = result
    partida(t5,t6)
    semi3 = result
    partida(t7,t8)
    semi4 = result
    print("### Vamos para as semis!! ###")
    partida(semi1,semi2)
    f1 = result
    partida(semi3,semi4)
    f2 = result
    print("### VAMOS PRAS FINAIS!!! ####")
    partida(f1,f2)
    print("O campeão do Parazão foi", result)