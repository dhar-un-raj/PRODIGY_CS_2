# **Image Encryption and Decryption Tool**
## **Description**
This Python script provides a simple method to encrypt and decrypt images using basic pixel manipulation techniques. It swaps the red and blue channels of each pixel for encryption and reverses the process for decryption.

## **Features**
- Encryption: The image pixels are modified to create a "weird" visual effect.

- Decryption: The original image is restored by reversing the transformations applied during encryption

## **Requirements**
- Python 3.x

- Pillow library (pip install pillow)

## **Usage**
1. Clone the repository:

   `git clone https://github.com/dhar-un-raj/image-encryption-tool.git`

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

## **Acknowledgments**
- Pillow library for image processing.

## **Contributing**

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.



---
During my shifts, I consistently documented repeated incidents along with detailed findings and analysis to identify root causes and implement corrective measures, contributing to the reduction of recurring issues. I actively worked on false positive optimization by reviewing alert patterns, fine-tuning detection rules, and collaborating with the respective teams to enhance the accuracy of threat detection. As part of my responsibilities, I regularly checked for log sources that had stopped emitting events and promptly followed up with the concerned teams to ensure timely resolution and continuous log flow. Additionally, I summarized all critical activities, incident responses, and key observations at the end of each shift and ensured they were clearly mentioned in the handover to maintain effective communication and operational continuity.
