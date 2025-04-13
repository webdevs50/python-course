## Nested Loops
for x in range(3):
    for y in range(4):
        print(f"({x}, {y})")


x_list = [1, 1, 1, 1, 5]




for x_count in x_list:
    output = ''
    for y in range(x_count):
        output += "x"
    print(output)