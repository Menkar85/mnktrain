# Напишите программу для добавления задач (todo_list).
# Для каждой из задач можно задать категорию и срок ее исполнения.
# Добавьте возможность вывода списка задач.

jobs = []
while True:
    print("Simple todo:")
    print("1. Add job")
    print("2. List jobs")
    print("3. Exit")
    choise1 = input("Enter number: ")
    match choise1:
        case '1':
            job = input("Enter a job: ")
            category = input("Enter category: ")
            time = input("Enter a time: ")
            jobs.append([job, category, time])
        case '2':
            for i in jobs:
                print(f"Job: {i[0]}; Category: {i[1]}; Time: {i[2]}")
            print()
        case '3':
            break
        case _:
            print("Please enter number from list above.\n")
