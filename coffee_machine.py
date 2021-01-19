class CoffeeMachine:

    def __init__(self):
        self.water_left = 400
        self.milk_left = 540
        self.beans_left = 120
        self.cups_left = 9
        self.money_left = 550
        self.esp_water, self.esp_beans, self.esp_price = 250, 16, 4
        self.lat_water, self.lat_milk, self.lat_beans, self.lat_price = 350, 75, 20, 7
        self.cap_water, self.cap_milk, self.cap_beans, self.cap_price = 200, 100, 12, 6

    def main(self):
        print("Write action (buy, fill, take, remaining, exit):")
        choice_action = input()
        print()
        if choice_action == "buy":
            CoffeeMachine.buy(self)
        elif choice_action == "fill":
            CoffeeMachine.fill(self)
        elif choice_action == "take":
            CoffeeMachine.take(self)
        elif choice_action == "remaining":
            CoffeeMachine.remaining(self)
        elif choice_action == "exit":
            exit()
        else:
            print("Sorry, only 'buy', 'fill', 'take', 'remaining' or 'exit' are available", end='\n')

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee_type = input()
        if coffee_type == "1":
            CoffeeMachine.buy_espresso(self)
        elif coffee_type == "2":
            CoffeeMachine.buy_latte(self)
        elif coffee_type == "3":
            CoffeeMachine.buy_cappuccino(self)
        elif coffee_type == "back":
            CoffeeMachine.main(self)
        else:
            print("Available options are 1, 2 or 3")
        print()
        CoffeeMachine.main(self)

    def buy_espresso(self):
        if self.water_left >= self.esp_water:
            if self.beans_left >= self.esp_beans:
                if self.cups_left >= 1:
                    print("I have enough resources, making you a coffee!")
                    self.water_left -= self.esp_water
                    self.beans_left -= self.esp_beans
                    self.cups_left -= 1
                    self.money_left += self.esp_price
                else:
                    print("Sorry, not enough coffee cups!")
            else:
                print("Sorry, not enough beans!")
        else:
            print("Sorry, not enough water!")
        print()
        CoffeeMachine.main(self)

    def buy_latte(self):
        if self.water_left >= self.lat_water:
            if self.milk_left >= self.lat_milk:
                if self.water_left >= self.lat_beans:
                    if self.cups_left >= 1:
                        print("I have enough resources, making you a coffee!")
                        self.water_left -= self.lat_water
                        self.milk_left -= self.lat_milk
                        self.beans_left -= self.lat_beans
                        self.cups_left -= 1
                        self.money_left += self.lat_price
                    else:
                        print("Sorry, not enough coffee cups!")
                else:
                    print("Sorry, not enough coffee beans!")
            else:
                print("Sorry, not enough coffee milk!")
        else:
            print("Sorry, not enough water!")
        print()
        CoffeeMachine.main(self)

    def buy_cappuccino(self):
        if self.water_left >= self.cap_water:
            if self.milk_left >= self.cap_milk:
                if self.beans_left >= self.cap_beans:
                    if self.cups_left >= 1:
                        print("I have enough resources, making you a coffee!")
                        self.water_left -= self.cap_water
                        self.milk_left -= self.cap_milk
                        self.beans_left -= self.cap_beans
                        self.cups_left -= 1
                        self.money_left += self.cap_price
                    else:
                        print("Sorry, not enough coffee cups!")
                else:
                    print("Sorry, not enough coffee beans!")
            else:
                print("Sorry, not enough milk!")
        else:
            print("Sorry, not enough water!")
        print()
        CoffeeMachine.main(self)

    def fill(self):
        print("Write how many ml of water do you want to add:")
        water_add = int(input())
        print("Write how many ml of milk do you want to add:")
        milk_add = int(input())
        print("Write how many grams of coffee beans do you want to add:")
        beans_add = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        cups_add = int(input())
        # sum by ingredient:
        self.water_left += water_add
        self.milk_left += milk_add
        self.beans_left += beans_add
        self.cups_left += cups_add
        print()
        CoffeeMachine.main(self)

    def take(self):
        print("I gave you $" + str(self.money_left))
        self.money_left = 0
        print()
        CoffeeMachine.main(self)

    def remaining(self):
        print("The coffee machine has:")
        print(self.water_left, "of water")
        print(self.milk_left, 'of milk')
        print(self.beans_left, 'of coffee beans')
        print(self.cups_left, "of disposable cups")
        print(f'${self.money_left} of money')
        print()
        CoffeeMachine.main(self)

    def exit(self):
        pass


a = CoffeeMachine()
a.main()
