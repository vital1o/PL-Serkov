def replace_colons():
    text = input("Введите текст: ")
    count = text.count(':')
    new_text = text.replace(':', '%')
    print("Новая строка:", new_text)
    print("Количество замен:", count)

replace_colons()