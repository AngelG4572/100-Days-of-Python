with open("./Input/Names/invited_names.txt") as data:
    unedited_names = data.readlines()
    for txt in unedited_names:
        new_name = txt.strip("\n")

        with open(f"./Output/ReadyToSend/letter_for_{new_name}", mode="w") as letter:
            contents = open("./Input/Letters/starting_letter.txt").read()
            new_content = contents.replace("[name]", new_name)
            letter.write(new_content)
