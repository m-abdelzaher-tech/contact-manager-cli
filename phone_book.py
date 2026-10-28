phone_book = {
    "1111111111": "Anas",
    "2222222222": "Mohammed",
    "3333333333": "Khalid",
    "4444444444": "Abdullah",
    "5555555555": "Rawan",
    "6666666666": "Faisal",
    "7777777777": "Layla"
}

def is_valid_number(number):
    return len(number) == 10 and number.isdigit()

def find_name_by_number(number):
    if not is_valid_number(number):
        print("This is invalid number")
        return
    if number in phone_book:
        print(f"{number} : {phone_book[number]}")
    else:
        print("Sorry, the number is not found")

def find_number_by_name(name):
    for num, owner in phone_book.items():
        if owner.lower() == name.lower():
            print(f"{name} : {num}")
            return
    print("Sorry, the name is not found")

find_name_by_number(input("Enter phone number: "))
find_number_by_name(input("Enter name: "))
