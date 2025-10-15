'''pessoas = [['João',10], ['Pedro',15], ['José',18]]

print(pessoas)

print(pessoas[0][0])

print(pessoas[1][0])

print(pessoas[2])

teste=list()

teste.append('lindolfo')
teste.append(43)

print(teste)

galera=list()
galera.append(teste[:]) #cópia

print(galera)

teste[0]='Maria'
teste[1]=22

print(teste)
print(galera)
'''
turma = [['Ana',15],['João',20],['Pedro',32],["Raul",44]]

'''print(turma)
print(turma[0])
print(turma[1][1])

for p in turma:
    print(p)

for p in turma:
    print(p[0])
'''

for p in turma:
    print(f'{p[0]} tem {p[1]} anos de idade')