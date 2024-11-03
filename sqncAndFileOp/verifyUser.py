from cryptography.fernet import Fernet
import re #for regular expression

# Function to generate a key for encryption and decryption
def generate_key():
    return Fernet.generate_key()

# Function to encrypt the Reference ID
def encrypt_reference_id(reference_id, key):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(reference_id.encode())
    return encrypted

# Function to decrypt the Reference ID
def decrypt_reference_id(encrypted_reference_id, key):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_reference_id).decode()
    return decrypted

# Function to validate the Reference ID
def validate_reference_id(reference_id):
    pattern = r'^[A-Za-z0-9@#%!&*()_+=-]{12}$'  # allows alphanumeric and some special characters
    return bool(re.match(pattern, reference_id))

def main():
    # Read the Reference ID from the user
    reference_id = input("Enter the Reference ID (12 characters, letters, numbers, and some special characters): ")

    # Validate the Reference ID
    if not validate_reference_id(reference_id):
        print("Invalid Reference ID. It should be 12 characters long and can include letters, numbers, and @#%!&*()_+=-.")
        return

    # Generate a key for encryption
    key = generate_key()
    print(f"Encryption Key (store this securely): {key.decode()}")

    # Encrypt the Reference ID
    encrypted_id = encrypt_reference_id(reference_id, key)
    print(f"Encrypted Reference ID: {encrypted_id.decode()}")

    # Ask if the user wants to decrypt
    decrypt_option = input("Do you want to decrypt the Reference ID? (yes/no): ").strip().lower()
    
    if decrypt_option == 'yes':
        decrypted_id = decrypt_reference_id(encrypted_id, key)
        print(f"Decrypted Reference ID: {decrypted_id}")

if __name__ == "__main__":
    main()
