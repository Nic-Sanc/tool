import os
import df_function

PROJECT_ID = "prova"

def go_to_choice(choice):
    if choice == 1:
        add_new_intent()
    elif choice == 2:
        df_function.list_intents(PROJECT_ID)
    elif choice == 3:
        remove_intent()
    elif choice == 4:
        return True
    return False

def add_new_intent():
    print()

def remove_intent():
    print()

def main():
    print("######### INTENTS MANAGE TOOL ITALIAN VERSION #########\n")
    closeTool = False
    while(closeTool == False):
        print("1) Aggiungi intent")
        print("2) Elimina intent")
        print("3) Lista degli intent")
        print("4) Esci")
        print("Scelta:",end = ' ')

        optionChoice = int(input())
        if optionChoice in range(0,5):
            closeTool = go_to_choice(optionChoice)
        else:
            print("Selezione errata! Inserire un valore compreso tra 1 e 4")
            os.system('pause')

        os.system('cls')
        
    print("Tool in chiusura!")
    os.system('pause')
            
if __name__ == "__main__":
    main()