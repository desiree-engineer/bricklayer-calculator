print ("WELCOME TO CALCULATOR FOR BRICKLAYER")
print("NOSSOS CALCULOS DISPONVEIS SÃO:"
    "\n1 - Calculo de area" 
    "\n2 - Cálculo de volume"
    "\n3 - Calculo de quantidade de Tijolos"
    "\n4 - Calculo de inclinação"
    "\n5 - Conversão de centimetro para metro"
    "\n6 - Conversão de metro para centimetro"
    "\n7 - Conversão de m2 para cm2"
    "\n8 - Conversão de cm2 para m2\n"
)
selecao=(int(input("Digite aqui o código do calculo desejado:")))
if selecao==1:
   largura=(float(input("Digite a largura em metros ")))
   comprimento=(float(input("Digite o comprimento em metros ")))            
   area=largura*comprimento
   print("Iniciando Cálculo da area...")
   print(f"A Area é: {area}m2")
elif selecao==2:
    comprimento=(float(input("Digite o comprimento em metros ")))
    largura=(float(input("Digite a largura em metros ")))
    altura=(float(input("Digite a altura em metros ")))
    volume=comprimento*largura*altura
    print("Iniciando Cálculo de volume...")
    print(f"O volume é: {volume}m3")
elif selecao==3:
    Quantidade_lajota=(int(input("Digite a quantidade de lajota (considerando lajota 30x30)  ")))
    area=(float(input("Digite o valor da area  ")))
    total_lajota=area/0.09
    total_lajota=int(total_lajota)
    total_lajota2=total_lajota*1.10
    total_lajota2=int(total_lajota2)
    print("Iniciando Cálculo de quantidade de Tijolos...")
    print(f"O total de lajotas sem considerar perdas é {total_lajota}")
    print(f"O total de lajotas considerando 10% de perdas é {total_lajota2}")
elif selecao==4:
    desnivel=(float(input("Digite o valor do desnivel em centimetros ")))
    comprimento= (float(input("Digite o comprimentro em metros ")))
    inclinacao=(desnivel/(comprimento*100))*100
    print("Iniciando Cálculo de inclinação...")
    print(f"A inclinação é de {inclinacao}%")
elif selecao==5:
    centimetro= (float(input("Digite os centimetros ")))
    metros= centimetro/100
    print("Iniciando Conversão de centimetro para metro...")
    print(f"{centimetro}centimetro(s) é igual a {metros}metro(s)")
elif selecao==6:
    metro= (float(input("Digite o metro(s) ")))
    centimetro= metro*100
    print("Iniciando Conversão de metro para centimetro...")
    print(f"{metro}metro(s) é igual a {centimetro}centimetro(s) ")
elif selecao==7:
    metro2= (float(input("Digite o m2 ")))
    centimetro2= metro2*10000
    print("Iniciando Conversão de m2 para cm2...")
    print(f"{metro2}m2 é igual a {centimetro2}cm2(s) ")
else:
    centimetro2= (float(input("Digite o cm2 ")))
    metro2= centimetro2/10000
    print("Iniciando Conversão de cm2 para m2...")
    print(f"{centimetro2}cm2 é igual a {metros2}m2")