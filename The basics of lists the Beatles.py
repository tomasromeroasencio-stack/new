beatles = []
print(f"\npaso 1 : {beatles}")

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print(f"\npaso 2 : {beatles} ")

for miembros in range(2):
    beatles.append(input("nuevos miembros de la banda :"))
print(f"\npaso 3 : {beatles} ")    

del beatles[-1]
del beatles[-1]
print(f"\npaso 4 : {beatles} ")

beatles.insert(0, "Ringo Starr")
print(f"\nel grupo finalmente es :{beatles}")
print(f"\nla cantidad de miembros del grupo es : {len(beatles)}")