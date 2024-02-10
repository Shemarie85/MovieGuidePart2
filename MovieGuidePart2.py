# NAME: Sheena Watson
# COURSE NUMBER: CIS261
# LAB TITLE: Week 6 Movie Guide Part 2
def display_menu():
    print("The Movie List Program\n")
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie title")
    print("del - Delete a movie title")
    print("exit - Exit the program")
    
def write_to_file(movie_list):
    f = open("movies.txt", "w")
    for movie in movie_list:
        f.write(movie+"\n")
    f.close()
    
def prepopulate_list():
    movie_list = []
    f = open("movies.txt", "r")
    data = f.readlines()
    for line in data:
        line = line.strip()
        movie_list.append(line)
    return movie_list

def display_titles(movie_list):
    for i in range(0, len(movie_list)):
        num = i +1
        print(str(num)+". "+movie_list[i])
        
def add_title(movie_list):
    title = input("Movie: ")
    movie_list.append(title)
    print(title,"was added.")
    write_to_file(movie_list)
    
def delete_title(movie_list):
    print("")
    num = int(input("Number: "))
    if num > 0 and num <= len(movie_list):
        name = movie_list.pop(num-1)
        print(name +" was deleted")
        write_to_file(movie_list)
    else:
        print("Invalid movie number.")
        
        
def handle_command(movie_list, command):
    command = command.lower()
    if command == "list":
        display_titles(movie_list)
    elif command == "add":
        add_title(movie_list)
    elif command == "del":
        delete_title(movie_list)
    elif command == "exit":
        print("Bye!")
        exit()
    else:
        print("Not a valid command. Please try again")
        
def start():
    movie_list =  prepopulate_list()
    display_menu()
    while True:
        command = input('\nCommand: ')
        handle_command(movie_list, command)
        
start()        

    