with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    text_of_letter = letter_file.read()
    for n in names:
        stripped_name = n.strip()
        letter = text_of_letter.replace("[name]", stripped_name)
        with open(f"../Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(letter)
