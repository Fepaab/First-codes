warrior_money = 450.0 #Valor Inicial do dinheiro
master_sword = 150.0 #Valor Fixo
mana_potion = 100.0 #Valor Fixo
healers_potion = 75.0 #Valor Fixo
y_n = 'y'

while (y_n == 'y'):

    x = input("Good night warrior, would like to buy something? Y/N: ")
    answr = x.upper()
    if answr == "Y" or "YES":
        print("Here it is the name and the prices os the products")
        
        print("1 - Master Sword: $", master_sword)
        print("2 - Mana Potion: $", mana_potion)
        print("3 - Healer's Potion: $", healers_potion)
        print("Money available: $", warrior_money)
    elif answr == "N" or "NO":                                                                               #professor que fez e ainda não entendi mto D:
        print("bye bye")
        break

    warrior_choise = int(input("Choose your item: "))

    if (warrior_choise == 1): #Master Sword
        print("You choose the Master Sword")
        warrior_money -= master_sword
        print(f"You have ${warrior_money} left")

    elif (warrior_choise == 2): #Mana Potion
        print("You choose the Mana Potion")
        warrior_money -= mana_potion
        print(f"You have ${warrior_money} left")

    elif (warrior_choise == 3): #Poção de Cura
        print("You choose the Healer's Potion")
        warrior_money -= healers_potion
        print(f"You have ${warrior_money} left")

    y_n=input("Would you like to buy something else?: ")                                    #professor que fez e ainda não entendi mto D:
