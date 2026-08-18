print("Яку гру ви бажаєте зіграти?")
print("1 - Хрестики-нулики")
print("2 - Вікторина слова")
print("3 - Квітка")

choice = input("Введіть 1, 2 або 3: ")

if choice == "1":
    import cross
elif choice == "2":
    import guess
elif choice == "3":
    import flower
else:
    print("Пеперошуємо, будь ласка, введіть 1, 2 або 3")
