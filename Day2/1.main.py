user_prompt = "Enter a todo: , to end this write \"0\": "

list_todo = []

x = 0
while x == 0:
    todo = input(user_prompt)
    if todo == "0":
        x += 1
        break
    list_todo.append(todo)
    print("current list of your todo's: ", list_todo)
    print("Next...")


print("final list of your todo's: ", list_todo)
