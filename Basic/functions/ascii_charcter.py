print(f"Program started!\n\n")

print(f"Please enter an ascii code:\n\n")
asciicode = abs(int(input()))

if asciicode in range(32, 127):
    print(f"The character represented by the ASCII code {asciicode} is \n\n{chr(asciicode)}\n\n")
else:
    print("Please input a valid number from 32 - 126.")
