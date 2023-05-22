title = input("zadej nazev titulu: ")

pocet_znaku = 0

for i in title:
    print(pocet_znaku+1, title[pocet_znaku])
    pocet_znaku += 1

lenght = len(title)

print("Title lenght is:", pocet_znaku)
print("using lenght also works:", lenght)
