# **Image Encryption and Decryption Tool**
## **Description**
This Python script provides a simple method to encrypt and decrypt images using basic pixel manipulation techniques. It swaps the red and blue channels of each pixel for encryption and reverses the process for decryption.

## **Features**
- Encryption: Swaps red and blue channels of each pixel.

- Decryption: Reverses the red and blue channel swap.

- Simple: Uses basic pixel manipulation for encryption and decryption.

## **Requirements**
- Python 3.x

- Pillow library (pip install pillow)

## **Usage**
1. Clone the repository:

   `git clone https://github.com/your_username/image-encryption-tool.git`

   `cd image-encryption-tool`

3. Encrypt an image:

   `python encrypt_image.py path_to_input_image.png path_to_output_encrypted_image.png`

5. Decrypt an image:

   `python decrypt_image.py path_to_input_encrypted_image.png path_to_output_decrypted_image.png`

## **Example**
### Encrypt an image:

`python encrypt_image.py path_to_your_image.png encrypted_image.png`

### Decrypt an image:
`python decrypt_image.py encrypted_image.png decrypted_image.png`

## **Notes**
- Replace path_to_your_image.png with the actual path to your image.

- Ensure you have permissions to read from the input directory and write to the output directory.

- This tool uses basic pixel manipulation techniques and is intended for educational purposes. For more secure encryption, consider using established cryptographic libraries.

## **Contributing**

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

---
