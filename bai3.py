with open('copy.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
five_lines = lines[:5]

with open('output.txt', 'w', encoding='utf-8') as f:
    f.writelines(five_lines)
    f.write("\nĐặng Khánh Linh")