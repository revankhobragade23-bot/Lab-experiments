file = open("input.txt", "r")

lines = file.readlines()
file.close()

print("Number of lines:", len(lines))

first_two_lines = lines[:2]

file = open("output.txt", "w")
file.writelines(first_two_lines)
file.close()

print("First two lines:")
print("".join(first_two_lines))
print("Data written to output.txt")