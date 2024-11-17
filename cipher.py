# add your code here
def caesar_ciper_encrypt(plain_text,shift):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            upper_case = char.isupper()
            char = char.lower()
            new_char = alpha[(alpha.index(char) + shift)%26]
            encrypted_text += new_char.upper()if upper_case else new_char
        else:
            encrypted_text += char
    return encrypted_text

plain_text = input(" Please enter a sentance")
shift_value = 5 
encrypted_text = caesar_ciper_encrypt(plain_text, shift_value)
print("The encrypted sentance is:", encrypted_text)


