
todos = []

while True:
    user_action = input("Type add, show or end: ")
    user_action = user_action.strip()
    x = 0

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':  # 2. bitwise or, we print items in two input instances
            for item in todos:
                x += 1
                item = item.title()
                print(x, item)
        case 'end':
            break
        case _:  # 1. kdykoliv nematchneme case davame _ (muzeme jakykoliv nazev promenne)
            print("Gey, you entered an unknown command")

print("Bye!")

