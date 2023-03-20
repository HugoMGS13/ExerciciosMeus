rend = float(input("Insira o seu rendimento anual: \n"))
if rend <= 85528:
    imp1 = (18*rend)/100
    imp = imp1 - 556.2
    imp = round(imp, 0)
    if imp <= 0:
        print("Não haverá cobrança de imposto.")
    else:
        print(f"O imposto é {imp} thalers")
elif rend > 85528:
    val1 = rend-85528
    val = (val1*32)/100
    imp = val+14839.2
    print(f"O imposto será {imp} thalers")