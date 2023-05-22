# Day 6
# Today we play with text files in the same folder
# :-)
# Windows pouziva backslahes \, linux a mac pote /.

while True:
    user_action = input("Type add, complete, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"  # bereme nove to-do

            file = open(r'D:\Python\Python projects\files\todos.txt', 'r')  # otevirame file s todos (absolutni cesta)
            todos = file.readlines()  # tvorime list nove zde, prectenim souboru
            file.close()  # nektere casti programu by mohli znenit nas file kdybychom nezavreli

            todos.append(todo)

            file = open('../files/todos.txt', 'w')  # 'w' for write, 'r' would be for read (relativni cesta)
            file.writelines(todos)  # cesta --> ../ ve slozce nad nami najdeme slozku files s hledanym todos.txt
            file.close()

        case 'complete':
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item}")
            number = int(input("Number of the todo to complete: "))
            number = number - 1
            todos.pop(number)

        case 'show':
            file = open('../files/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                row = f"{index+1}. {item}"
                print(row)

        case 'edit':
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item}")
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

        case 'exit':
            break

print("Bye!")
