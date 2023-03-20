def imc():

    print("**** Calculadora de Imc ****")
    
    weight_input = int(input("Seu peso: "))
    height_input = int(input("Sua altura: "))

    weight = weight_input
    height = height_input / 100

    calcular_imc = round(weight / (height * height))

    if (calcular_imc < 18.5):
        print(f"Seu IMC é {calcular_imc} e sua classificação é MAGREZA.")
    elif (calcular_imc >= 18.5 and 24.9):
        print(f"Seu IMC é {calcular_imc} e sua classificação é NORMAL.")
    elif (calcular_imc >= 25 and calcular_imc < 29.9):
        print(f"Seu IMC é {calcular_imc} e sua classificação é SOBREPESO.")
    elif (calcular_imc >= 30 and calcular_imc < 34.9):
        print(f"Seu IMC é {calcular_imc} e sua classificação é OBESIDADE DE GRAU 1.")
    elif (calcular_imc >= 35 and calcular_imc < 39.9):
        print(f"Seu IMC é {calcular_imc} e sua classificação é OBESIDADE DE GRAU 2.")
    elif (calcular_imc >= 40):
        print(f"Seu IMC é {calcular_imc} e sua classificação é OBESIDADE DE GRAU 3.")



if (__name__ == "__main__"):
    imc()