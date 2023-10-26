# Solicitando  ao usuário o nome e a quantidade de XP do herói
nome = input("Digite o nome do herói: ")
xp = int(input("Digite a quantidade de XP do herói: "))

# Definindo o nível com base na quantidade de XP
if xp < 1000:
    nivel = "Ferro"
elif 1000 <= xp <= 2000:
    nivel = "Bronze"
elif 2001 <= xp <= 5000:
    nivel = "Prata"
elif 6001 <= xp <= 7000:
    nivel = "Ouro"
elif 7001 <= xp <= 8000:
    nivel = "Platina"
elif 8001 <= xp <= 9000:
    nivel = "Ascendente"
elif 9001 <= xp <= 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"

# Exibe a mensagem com o nome e o nível do herói
print(f"O Herói de nome {nome} está no nível de {nivel}")
