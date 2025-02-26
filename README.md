
## 🔒 Steganography 
### Overview


A Python script that hides secret messages inside images using image steganography.

The message is encrypted within the blue color channel of an image, and only users with the correct passcode can decrypt it.



## 📌 Features

✅ Hide a secret message inside an image.

✅ Retrieve the hidden message using the correct passcode.

✅ Uses OpenCV (cv2) for image manipulation.

✅ Prevents unauthorized access to the hidden message.

✅ Ensures minimal image distortion by modifying only the blue channel.


## 📂 Project Structure

To deploy this project run

```bash
  📁 Image-Steganography
│── 📄 steganography.py      # Main Python script for encoding & decoding
│── 🖼️ mypic.jpg            # Original image (replace with your own)
│── 🖼️ encryptedImage.jpg   # Output image with hidden message
│── 📄 README.md            # Project documentation (this file)
```


## 🚀 Installation

### 1. Clone the Repository


```bash
git clone https://github.com/your-username/Image-Steganography.git
cd Image-Steganography

```

### 2. Install Dependencies
Ensure you have Python 3.x installed. Then install OpenCV:

```bash
pip install opencv-python numpy

```

## 🔧 For GUI Install Required Libraries
Before running the script, make sure you have all the required Python libraries installed:

```bash
pip install opencv-python numpy cryptography pillow
pip install opencv-python numpy cryptography pillow tkinter

```
    
## 🛠 Usage

### 1️⃣ Encoding a Message into an Image
Run the script and enter your secret message:


```bash
python steganography.py

```

• Enter your secret message.

• Set a passcode.

• The script will generate an encrypted image (encryptedImage.jpg).

### 2️⃣ Decoding the Message
Run the script again and enter the correct passcode:


```bash
python steganography.py

```

• If the passcode is correct, the hidden message will be revealed.
• If the passcode is wrong, access is denied.
## 📜 License



This project is open-source under the [MIT](https://choosealicense.com/licenses/mit/) License. Feel free to modify and improve it.
## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ankit-kumar-singh-081035320/)


