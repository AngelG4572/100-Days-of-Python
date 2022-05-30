with open("../Mail Merge Project/Input/Names/invited_names.txt") as data:
    unedited_names = data.readlines()
    for txt in unedited_names:
        new_name = txt.strip("\n")

        with open(f"../Mail Merge Project/Output/ReadyToSend/letter_for_{new_name}", mode="w") as letter:
            contents = open("../Mail Merge Project/Input/Letters/starting_letter.txt").read()
            new_content = contents.replace("[name]", new_name)
            letter.write(new_content)
