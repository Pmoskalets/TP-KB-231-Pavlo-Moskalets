import random

# Функція для визначення переможця
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Нічия!"
    elif (user_choice == "камінь" and computer_choice == "ножиці") or \
         (user_choice == "ножиці" and computer_choice == "папір") or \
         (user_choice == "папір" and computer_choice == "камінь"):
        return "Ви виграли!"
    else:
        return "Комп'ютер виграв!"

# Гра
options = ["камінь", "ножиці", "папір"]

print("Гра: Камінь, Ножиці, Папір!")
while True:
    user_choice = input("Ваш вибір (камінь, ножиці, папір або вихід): ").lower()
    if user_choice == "вихід":
        print("Дякую за гру!")
        break
    if user_choice not in options:
        print("Неправильний вибір. Спробуйте ще раз.")
        continue

    computer_choice = random.choice(options)
    print(f"Комп'ютер вибрав: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)
