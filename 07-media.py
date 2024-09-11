# elaborar um algoritmo que solicicta 4 notas ao usuario.
# o programa deve calcular a media e
# verificar se media e igual ou menor que 80.
# se a media for igual ou menor que 80, o programa deve exibir a mensagem "
# "Aprovado" caso contrario exibir a mensagem "Reprovado"

nota1 = float(input("digite a nota 1: "))
nota2 = float(input("digite a nota 2: "))
nota3 = float(input("digite a nota 3: "))
nota4 = float(input("digite a nota 4: "))


media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A media das notas é {media:.2f}")

if media <= 80:
  print("aprovado")
else:
  print("reprovado")
