#shay vanlandschoot
#10-4-24
#caeser cpher



alpha = 'abcdefghijklmnopqrstuvwxzy'

new_message = ''

message = input('enter message here: ').lower()
key = int(input('enter key here'))
#print(f'{message}')

for character in message:
    if character in alpha:
        position = alpha.find(character)
        new_position = (position + key) % 26
        new_character = alpha[new_position]
        new_message += new_character
    
    else:
        new_message += character
print('your new message is ' + new_message)
