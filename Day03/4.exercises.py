# 1 prompting user to enter country they're from and printing hello to them

country = input("What country are you from?: ")
country = country.capitalize()

while True:
    match country:
        case 'USA' | 'Usa':
            print("Hello")
        case 'India':
            print("Namaste")
        case 'Germany':
            print("Bonjour")
        case _:
            break

print("Bip bup")

# 2.

ingredients = ["john smith", "sen plakay", "dora ngacely"]

for ingredient in ingredients:
    print(ingredient.title())  # 3. metoda
