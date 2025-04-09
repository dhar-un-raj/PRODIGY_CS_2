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

####### High availability cluster parameters #######

## Option: HANodeName
#       The high availability cluster node name.
#       When empty, server is working in standalone mode; a node with empty name is registered with address for the frontend to connect to.
#
# Mandatory: no
# Default:
# HANodeName=

## Option: NodeAddress
#       IP or hostname with optional port to specify how frontend should connect to the server.
#       Format: <address>[:<port>]
#
#       If IP or hostname is not set, then ListenIP value will be used. In case ListenIP is not set, localhost will be used.
#       If port is not set, then ListenPort value will be used. In case ListenPort is not set, 10051 will be used.
#       This option can be overridden by address specified in frontend configuration.
#
# Mandatory: no
# Default:
# NodeAddress=localhost:10051

####### Browser monitoring #######

### Option: WebDriverURL
#       WebDriver interface HTTP[S] URL. For example http://localhost:4444 used with Selenium WebDriver standalone server.
#
# Mandatory: no
# Default:
# WebDriverURL=

### Option: StartBrowserPollers
#       Number of pre-forked instances of browser item pollers.
#
# Mandatory: no
# Range: 0-1000
# Default:
# StartBrowserPollers=1
# ### Option: FpingLocation
#       Location of fping.
#       Make sure that fping binary has root ownership and SUID flag set.
#
# Mandatory: no
# Default:
# FpingLocation=/usr/sbin/fping
FpingLocation=/usr/bin/fping
StartPingers=4
### Option: Fping6Location

#       Location of fping6.
#       Make sure that fping6 binary has root ownership and SUID flag set.
#       Make empty if your fping utility is capable to process IPv6 addresses.
#
# Mandatory: no
# Default:
# Fping6Location=/usr/sbin/fping6
Fping6Location=
