import random
import string

def generate_password(length=12):
    """
    Generate a secure password with the specified length.
    
    Args:
        length (int): The length of the password (default: 12).
    
    Returns:
        str: The generated password.
    """
    # Define the character sets for different types of characters
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = '!#$%&()*+,-./:;<=>?@[\\]^_{|}~'
    
    # Combine all character sets into one
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    
    # Ensure that the length is at least 8
    length = max(length, 8)
    
    # Generate the password by randomly selecting characters from the combined set
    password = random.sample(lowercase_letters + uppercase_letters, 4)
    password += random.sample(all_characters, length - 4)
    
    # Convert the list of characters to a string
    password = ''.join(password)
    
    return password
