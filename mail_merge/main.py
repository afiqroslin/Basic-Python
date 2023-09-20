invite = open("Input/Names/invited_names.txt", "r")
letter = open("Input/Letters/starting_letter.txt", "r")
x = letter.read()

for name in invite.readlines():
    names = name.strip()
    filename = f"Output/ReadyToSend/{names}.txt"
    with open(filename, 'w') as f:
        data = x.replace("[name]", names)
        f.write(data)
        f.close()




