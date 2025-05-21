nome = input("Digite seu nome: ")
alt = float(input("Digite sua altura: "))
kg = float(input("Digite seu peso: "))

IMC = kg / (alt*alt)

if IMC <= 18.4:
    print("Você está abaixo do peso !")
elif IMC >=18.5 and IMC <= 24.9:
    print("Seu peso está normal")
elif IMC >= 25.0 and IMC <= 29.9:
    print("Você está acima do peso !")
elif IMC >= 30.0 and IMC <= 34.9:
    print("Você está com Obseidade Grau I !!!")
elif IMC >= 35.0 and IMC <= 39.9:
    print("Você está com Obesidade Grau II !!!")
else:
    print("Você está com Obesidade Grau III(Mórbida) !!!")
print("----------------------------------------------------------------------------------------------------------")
print(f"\n{nome}, seu IMC é: {IMC:.1f}")