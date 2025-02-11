def caesar_decrypt(ciphertext, shift):

    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():  # Only shift alphabetic characters
            shift_amount = shift % 26  # Handle shifts larger than 26
            if char.islower():
                # Shift lowercase letters
                decrypted_char = chr((ord(char) - 97 - shift_amount) % 26 + 97)
            else:
                # Shift uppercase letters
                decrypted_char = chr((ord(char) - 65 - shift_amount) % 26 + 65)
            decrypted_text += decrypted_char
        else:
            # Leave non-alphabetic characters unchanged
            decrypted_text += char
    return decrypted_text

def brute_force_caesar(ciphertext):

    print("\nBrute-force results:")
    for shift in range(26):
        decrypted_text = caesar_decrypt(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")

def main():
    print("Welcome to the Caesar Cipher Decryptor!")
    ciphertext = input("Enter the encrypted message: ")
    
    shift_input = input("Enter the shift value (leave blank to brute-force): ")
    
    if shift_input.strip():  # If user enters a shift value
        shift = int(shift_input)
        decrypted_text = caesar_decrypt(ciphertext, shift)
        print(f"Decrypted Message: {decrypted_text}")
    else:  # If no shift value is entered, brute-force the cipher
        brute_force_caesar(ciphertext)

if __name__ == "__main__":
    main()
