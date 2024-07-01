from PIL import Image

def encrypt_image(input_path, output_path, key=None):
    try:
        img = Image.open(input_path)
        pixels = img.load()
        width, height = img.size

        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]

                # swapping red and blue channels
                encrypted_pixel = (b, g, r)

                pixels[i, j] = encrypted_pixel

        img.save(output_path)
        print("Image encrypted successfully!")
    except Exception as e:
        print(f"An error occurred during encryption: {e}")

def decrypt_image(input_path, output_path, key=None):
    try:
        img = Image.open(input_path)
        pixels = img.load()
        width, height = img.size

        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]

                # swapping red and blue channels back
                decrypted_pixel = (b, g, r)

                pixels[i, j] = decrypted_pixel

        img.save(output_path)
        print("Image decrypted successfully!")
    except Exception as e:
        print(f"An error occurred during decryption: {e}")

# image paths
input_image = r"C:\Users\guhan\Desktop\Image Encryption and Decryption\Funny.jpg" #Replace with your Image Path
encrypted_image = r"C:\Users\guhan\Desktop\Image Encryption and Decryption\encrypted.jpg"
decrypted_image = r"C:\Users\guhan\Desktop\Image Encryption and Decryption\decrypted.jpg"

# Encrypt the image
encrypt_image(input_image, encrypted_image)

# Decrypt the image
decrypt_image(encrypted_image, decrypted_image)
