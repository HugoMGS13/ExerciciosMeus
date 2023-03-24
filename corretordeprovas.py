def dist(X, m, Y, n):
	if m == 0:
		return n
	if n == 0:
		return m
	cost = 0 if (X[m - 1] == Y[n - 1]) else 1
	return min(dist(X, m - 1, Y, n) + 1,		
			dist(X, m, Y, n - 1) + 1,  
			dist(X, m - 1, Y, n - 1) + cost)
quest = int(input("Digite o número de questões que a prova contém: \n"))
gab = input("Escreva o gabarito da prova: \n")
gab.split()
listgab = []
listresult = []
if (len(gab) < quest or len(gab) > quest):
    print("As respostas e o gabarito não estão na mesma quantidade")
if (len(gab) == quest):
    resp = input("Escreva as respostas do aluno: \n")
    listgab.append(gab)
    resp.split()
    listresult.append(resp)
    for i in listgab:
        for a in listresult:
            if a == i:
                print("O aluno acertou 100","%", "das questões.")
            else:
                print("o aluno errou" ,dist(i,len(i),a,len(a)), "questões e acertou" , quest-dist(i,len(i),a,len(a)))
