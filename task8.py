with open('task8_text.txt', 'r', encoding='utf-8') as f:
    file1 = f.read()

with open('task8_text_reversed.txt', 'w', encoding='utf-8') as f:
    f.writelines(reversed(file1))

print("Исходный файл:")
with open('task8_text.txt', 'r', encoding='utf-8') as f:
    print(f.read())

print("\nНовый файл:")
with open('task8_text_reversed.txt', 'r', encoding='utf-8') as f:
    print(f.read())