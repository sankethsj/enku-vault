from cryptography.fernet import Fernet

def generate_encryption_key():
    """
    Generate a secure encryption key.
    
    Returns:
        bytes: The encryption key.
    """
    return Fernet.generate_key()

def encrypt_message(message, key):
    """
    Encrypt a message using the provided encryption key.
    
    Args:
        message (str): The message to encrypt.
        key (bytes): The encryption key.
    
    Returns:
        bytes: The encrypted message.
    """
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    """
    Decrypt an encrypted message using the provided encryption key.
    
    Args:
        encrypted_message (bytes): The encrypted message.
        key (bytes): The encryption key.
    
    Returns:
        str: The decrypted message.
    """
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message
