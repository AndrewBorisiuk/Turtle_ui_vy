print("Яку гру ви бажаєте зіграти?")
print("1 - Хрестики-нулики")
print("2 - Вікторина слова")

choice = input("Введіть 1 або 2: ")

if choice == "1":
    import cross
elif choice == "2":
    import guess
else:
    print("Пеперошуємо, будь ласка, введіть 1 або 2")
