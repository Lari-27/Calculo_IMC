# Solicita ao usuário que insira o peso em quilogramas e a altura em metros
peso_str = input("Digite seu peso em quilogramas (use vírgula se necessário): ")
altura_str = input("Digite sua altura em metros (use vírgula se necessário): ")

# Substitui vírgulas por pontos para garantir que o Python possa interpretar números decimais
peso_str = peso_str.replace(',', '.')
altura_str = altura_str.replace(',', '.')

# Converte as strings em números decimais
peso = float(peso_str)
altura = float(altura_str)

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o resultado
print("Seu Índice de Massa Corporal (IMC) é:", imc)

# Interpretação do IMC
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Seu peso está saudável.")
elif 25 <= imc < 30:
    print("Você está com sobrepeso.")
else:
    print("Você está obeso.")


