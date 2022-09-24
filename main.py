from random import choice
characteres = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%¨&&*()'
senha = ''
quantidade = int(input("digite a quantidade de characteres de sua senha: "))

for i in range(quantidade):
    senha += choice(characteres)
print(f"Sua senha foi gerada: {senha}")