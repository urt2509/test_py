from joke import get_random_joke

def main():
    name = input("Please, enter your name: ")
    print(f"Привіт, {name}!")

    while True: 
        user_response = input(f"{name} d you want do read joke: yes/no: ").lower()

        if user_response == "yes": 
            print(get_random_joke())
        elif user_response == "no":
            print(f"Bye-bye, {name}!")
            break 
if __name__ =="__main__":
    main()
        
    
