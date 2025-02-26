# Stenography

🔒 Image-Based Steganography with OpenCV
A Python script that hides secret messages inside images using image steganography.
The message is encrypted within the blue color channel of an image, and only users with the correct passcode can decrypt it.

📌 Features
✅ Hide a secret message inside an image.
✅ Retrieve the hidden message using the correct passcode.
✅ Uses OpenCV (cv2) for image manipulation.
✅ Prevents unauthorized access to the hidden message.
✅ Ensures minimal image distortion by modifying only the blue channel.

📂 Project Structure

📁 Image-Steganography
│── 📄 steganography.py      # Main Python script for encoding & decoding
│── 🖼️ mypic.jpg            # Original image (replace with your own)
│── 🖼️ encryptedImage.jpg   # Output image with hidden message
│── 📄 README.md            # Project documentation (this file)

🚀 Installation
1. Clone the Repository
git clone https://github.com/your-username/Image-Steganography.git
cd Image-Steganography

2. Install Dependencies
Ensure you have Python 3.x installed. Then install OpenCV:

pip install opencv-python numpy

🛠 Usage
1️⃣ Encoding a Message into an Image
Run the script and enter your secret message:
python steganography.py

Enter your secret message.
Set a passcode.
The script will generate an encrypted image (encryptedImage.jpg).

2️⃣ Decoding the Message
Run the script again and enter the correct passcode:
python steganography.py

If the passcode is correct, the hidden message will be revealed.
If the passcode is wrong, access is denied.
💡 How It Works
1️⃣ Encoding Process:

The script reads the image and converts the secret message to ASCII values.
The message is stored in the blue color channel of each pixel.
The first pixel (0,0) stores the message length to ensure safe retrieval.
The modified image is saved as encryptedImage.jpg.
2️⃣ Decoding Process:

The script reads the modified image and extracts the message using the stored message length.
If the user enters the correct passcode, the message is revealed.

🔐 Security Considerations
This method is not highly secure for large-scale cryptography.
For added security, consider AES encryption before embedding the message.
LSB-based steganography can be used to make the message less detectable.

📝 To-Do List
 Add LSB-based encoding for better security.
 Implement AES encryption before hiding the message.
 Create a GUI version using Tkinter or PyQt.
📜 License
This project is open-source under the MIT License. Feel free to modify and improve it.

🤝 Contributing
Contributions are welcome! If you’d like to improve the project, follow these steps:
Fork the repository.
Create a new branch.
Commit your changes.
Push to your fork and submit a Pull Request.
