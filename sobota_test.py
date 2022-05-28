lista = ["arbuz", "ser", "pieczywo", "pomidor"]
for i in lista:
    print(i)

lista.append("masło")
print(lista)
lista.append("sok pomarańczowy")
lista. append("pepsi")
print(lista)

#x = "Pada deszcz"
#x = "Deszcz nie pada"
x = "Świeci słońce"

if x == "Pada deszcz":
    print("Koniecznie zabierz parasol idąć do sklepu!")
elif x == "Deszcz nie pada":
    print("Pogoda za oknem ok, możesz iść bez parasola :)")
elif x == "Świeci słońce":
    print("Zabierz okulary przeciwsłoneczne")
else:
    print("Niezidentyfikowana przez system pogoda za oknem")

print("test nowego brancha")
print ("test nanoszenia zmian w repozytorium zdalnym i przenoszenia do lokalnego")
