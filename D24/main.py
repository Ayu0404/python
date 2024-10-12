with open('D24/Input/Letters/starting_letter.txt') as letter:
    lines=letter.read()

    with open('D24/Input/Names/invited_names.txt') as recipient:
        names=recipient.readlines()

    for name in names:
        name=name.strip()
        with open(f'D24/Output/ReadyToSend/{name}.txt','w') as op:
            new_letter=lines.replace('[name]',name)
            op.write(new_letter)
