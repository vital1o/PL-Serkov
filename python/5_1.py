def count_words_starting_with_e():
    text = input("Введите текст: ")
    words = text.split()  # разбив на слова
    count = sum(1 for word in words if word.lower().startswith('е'))  # получение кол-во слов на е
    return count

print(count_words_starting_with_e())