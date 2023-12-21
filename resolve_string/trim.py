def remove_spaces(string: str) -> str:
    return string.replace(" ", "")


lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

# 把多行字符串合并成一行
input_string = "".join(lines)
print("多行字符串为:")
print(remove_spaces(input_string))


