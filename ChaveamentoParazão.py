import random
print("Vamos para as quartas de final do Parazão")
time1 = input("Digite o nome do primeiro competidor: \n")
time2 = input("Digite o nome do segundo competidor: \n")
lista1 = [time1,time2]
result1 = random.choice(lista1)
print(f"O vencedor desse foi {result1}")
print("Vamos pra segunda rodada")
time3 = input("Digite o nome do terceiro competidor: \n")
time4 = input("Digite o nome do quarto competidor: \n")
lista2 = [time3,time4]
result2 = random.choice(lista2)
print(f"O vencedor desse duelo foi {result2}")
print("Vamos pra terceira rodada")
time5 = input("Digite o nome do quinto competidor: \n")
time6 = input("Digite o nome do sexto competidor: \n")
lista3 = [time5,time6]
result3 = random.choice(lista3)
print(f"O vencedor desse duelo foi {result3}")
print("Vamos pra quarta-rodada")
time7 = input("Digite o nome do sétimo competidor: \n")
time8 = input("Digite o nome do oitavo competidor: \n")
lista4 = [time7,time8]
result4 = random.choice(lista4)
print(f"O vencedor desse duelo foi {result4}")
print("Vamos pra semi-final")
listasemi1 = [result1,result2]
resultsemi1 = random.choice(listasemi1)
print(f"O primeiro duelo da semi-final será entre {result1} e {result2}") 
print(f"O vencedor do primeiro duelo da semi-final foi {resultsemi1}")
listasemi2 = [result3,result4]
resultsemi2 = random.choice(listasemi2)
print(f"O segundo duelo da semi-final será entre {result3} e {result4}") 
print(f"O vencedor do segundo duelo da semi-final foi {resultsemi2}")
print("Vamos pras Finais")
final = [resultsemi1,resultsemi2]
campeão = random.choice(final)
print(f"A final será entre {resultsemi1} e {resultsemi2}") 
print(f"O campeão do parazão foi {campeão}")
