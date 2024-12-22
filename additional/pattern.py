command = input("Please enter command: ")

match command:
    case "exit":
        exit()  # Exit from programm
    case "hi":
        print("Hi there!")
    case _:  # Default case
        print("Unknown command")
