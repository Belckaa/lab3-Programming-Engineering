def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Неможливо поділити на нуль"
def main():
    print("Виберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")

    choice = input("Введіть номер операції (1,2,3,4): ")
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))

    if choice == '1':
        print(f"Результат: {add(num1, num2)}")
    elif choice == '2':
        print(f"Результат: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Результат: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Результат: {divide(num1, num2)}")
    else:
        print("Невірний вибір")

if __name__ == "__main__":
    main()
