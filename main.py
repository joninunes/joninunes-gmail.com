print("*************************************")
print("PROJECAO EM PYTHON PARA COVID-19")
print("By Joni Nunes")
print("*************************************")

projecao = 0

dias = int(input("Quantos dias deseja projetar?"))
x = int(input("Quantas dias desde a primeira morte registrada?"))
mortes = int(input("Quantas mortes existem hoje?"))

projecao = mortes

projecao = projecao + (mortes / x * dias)
print("Em ", dias, "dias teremos ", projecao, "mortos")
