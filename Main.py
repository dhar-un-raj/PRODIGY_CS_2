from PIL import Image
import random

def encrypt_image(input_path, output_path):
    """
    Encrypts an image by applying weird transformations and saves it as an image.

    Args:
        input_path (str): Path to the input image.
        output_path (str): Path to save the encrypted image.
    """
    try:
        img = Image.open(input_path)
        width, height = img.size
        pixels = img.load()

        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                # Custom transformation: Invert colors and shuffle channels
                r, g, b = 255 - r, 255 - g, 255 - b
                r, g, b = b, r, g
                pixels[x, y] = (r, g, b)

        img.save(output_path)
        print("Image encrypted successfully!")
    except Exception as e:
        print(f"An error occurred during encryption: {e}")

def decrypt_image(input_path, output_path):
    """
    Decrypts an image by reverting the weird transformations and saves it as an image.

    Args:
        input_path (str): Path to the encrypted image.
        output_path (str): Path to save the decrypted image.
    """
    try:
        img = Image.open(input_path)
        width, height = img.size
        pixels = img.load()

        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                # Inverse transformation: Shuffle channels back and invert colors
                r, g, b = g, b, r
                r, g, b = 255 - r, 255 - g, 255 - b
                pixels[x, y] = (r, g, b)

        img.save(output_path)
        print("Image decrypted successfully!")
    except Exception as e:
        print(f"An error occurred during decryption: {e}")

# Image paths
input_image = r"Image Path\Image.jpg"  # Replace with your Image Path
encrypted_image = r"Image Path\encrypted.jpg"
decrypted_image = r"Image Path\decrypted.jpg"

# Encrypt the image
encrypt_image(input_image, encrypted_image)

# Decrypt the image by restoring the original
decrypt_image(encrypted_image, decrypted_image)
