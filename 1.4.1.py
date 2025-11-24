#2
with open('example.txt', 'r', encoding='utf-8') as file:
    first_line = file.readline()
    print(first_line.strip())
with open('example.txt', 'r', encoding='utf-8') as file:
        first_10_chars = file.read(10)
        print(repr(first_10_chars))
with open('example.txt', 'r', encoding='utf-8') as file:
        for line in file:
                print(line.strip())
#3
with open('output.txt', 'w', encoding='utf-8') as file:
        file.write("Начало файла\n")
with open('output.txt', 'a', encoding='utf-8') as file:
        file.write("Продолжение файла\n")
with open('output.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print("Содержимое файла:")
        print(content)