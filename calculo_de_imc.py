try:
    nome = input("Digite seu nome: ")
    alt = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))

    IMC = peso / (alt*alt)

    if IMC <= 18.4:
        print("Você está abaixo do peso !")
    elif IMC >=18.5 and IMC <= 24.9:
        print("Seu peso está normal")
    elif IMC >= 25.0 and IMC <= 29.9:
        print("Você está acima do peso !")
    elif IMC >= 30.0 and IMC <= 34.9:
        print("Você está com Obesidade Grau I !!!")
    elif IMC >= 35.0 and IMC <= 39.9:
        print("Você está com Obesidade Grau II !!!")
    else:
        print("Você está com Obesidade Grau III(Mórbida) !!!")
    print("----------------------------------------------------------------------------------------------------------")
    print(f"\n{nome}, seu IMC é: {IMC:.1f}")

except ValueError:
    print("Erro: Por favor, digite valores numéricos válidos para altura e peso.")
except ZeroDivisionError:
    print("Erro: A altura não pode ser zero.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
