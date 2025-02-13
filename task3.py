def calculate_array_stats():
    print("\nПідрахунок елементів масиву")
    print("-" * 40)

    while True:
        try:
            size = int(input("Введіть розмір масиву: "))
            if size > 0:
                break
            else:
                print("Розмір масиву повинен бути більше 0!")
        except ValueError:
            print("Будь ласка, введіть ціле число!")

    array = []
    print("\nВведіть елементи масиву:")
    
    for i in range(size):
        while True:
            try:
                element = float(input(f"Елемент {i + 1}: "))
                array.append(element)
                break
            except ValueError:
                print("Будь ласка, введіть число!")

    sum_positive = 0
    count_negative = 0

    for element in array:
        if element > 0:
            sum_positive += element
        elif element < 0:
            count_negative += 1


    print("\n" + "=" * 40)
    print("РЕЗУЛЬТАТИ АНАЛІЗУ МАСИВУ:")
    print("=" * 40)
    
    print("\nВведений масив:")
    for i, element in enumerate(array, 1):
        print(f"Елемент {i}: {element:>8.2f}")
    
    print("\nПІДСУМОК:")
    print(f"Сума додатних елементів: {sum_positive:.2f}")
    print(f"Кількість від'ємних елементів: {count_negative}")

if __name__ == "__main__":
    calculate_array_stats() 