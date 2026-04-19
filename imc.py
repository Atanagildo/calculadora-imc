# Calculadora de IMC
# Projeto 1 - Portifólio de Atanagildo Santos

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura * altura)

if imc < 18.5:
    classificacao = "Abaixo do peso ⚠️"
elif imc < 25:
    classificacao = "Peso normal ✅"
elif imc < 30:
    classificacao = "Sobrepeso ⚠️"
else:
    classificacao = "Obesidade 🔴"

print(f"\nOlá, {nome}!")
print(f"Seu IMC é: {imc:.1f}")
print(f"Classificação: {classificacao}")