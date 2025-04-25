idade = float(input('Qual sua idade? '))

if idade < 12:
    print("Criança");
elif idade < 18:
    print("Adolescente");
elif idade < 59:
    print("Adulto");
else:
    print("idoso")