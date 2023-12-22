from task1 import task1
from task2 import task2
from task3 import task3
from task4 import task4
from task5 import task5

while True:
    command = input("What would you like to see? (imdb/pie/years/actors/genres/exit): ")

    if command == "imdb":
        task1()
    elif command == "pie":
        task2()
    elif command == "years":
        task3()
    elif command == "actors":
        task4()
    elif command == "genres":
        task5()
    elif command == "exit":
        exit()
    else:
        print("Invalid command. Please enter a valid command.")
