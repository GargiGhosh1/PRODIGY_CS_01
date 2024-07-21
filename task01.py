def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Determine the appropriate case range (uppercase or lowercase)
            start = ord('A') if char.isupper() else ord('a')
            # Perform the shift and handle wrapping
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetical characters remain unchanged
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            # Determine the appropriate case range (uppercase or lowercase)
            start = ord('A') if char.isupper() else ord('a')
            # Perform the shift and handle wrapping
            decrypted_char = chr((ord(char) - start - shift) % 26 + start)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  
    return decrypted_text

# Main program
def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").strip().lower()
        if choice not in ['encrypt', 'decrypt']:
            print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")
            continue
        
        message = input("Enter your message: ").strip()
        shift = int(input("Enter the shift value (a positive integer): "))
        
        if choice == 'encrypt':
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'decrypt':
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")
        
        repeat = input("Do you want to encrypt/decrypt another message? (yes/no): ").strip().lower()
        if repeat != 'yes':
            break

if __name__ == "__main__":
    main()
