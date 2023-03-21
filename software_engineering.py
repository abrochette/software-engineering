def encode_pw(password):
    new_password = str()
    for i in str(password):
        if i == '0':
            new_password += '3'
        if i == '1':
            new_password += '4'
        if i == '2':
            new_password += '5'
        if i == '3':
            new_password += '6'
        if i == '4':
            new_password += '7'
        if i == '5':
            new_password += '8'
        if i == '6':
            new_password += '9'
        if i == '7':
            new_password += '10'
        if i == '8':
            new_password += '11'
        if i == '9':
            new_password += '12'
    return new_password


def decode_pw(new_password):
    password = str()
    for i in str(new_password):
        if i == '3':
            password += '0'
        if i == '4':
            password += '1'
        if i == '5':
            password += '2'
        if i == '6':
            password += '3'
        if i == '7':
            password += '4'
        if i == '8':
            password += '5'
        if i == '9':
            password += '6'
        if i == '1':
            continue
        if i == '0':
            password += '7'
        if i == '2':
            password += '8'
        if i == '3':
            password += '9'
    return password


print("Menu")
print("-------------")
print("1. Encode")
print("2. Decode")
print("3. Quit")
option = int(input("Please enter an option:"))
if option == 1:
    password = input("Please enter a password to encode:")
    new_password = print(encode_pw(password))
    print("Your password has been encoded and stored!")
if option == 2:
    password = decode_pw(new_password)
    print("The encoded password is " + new_password + ",and the original password is" + password + ".")
if option == 3:
    exit