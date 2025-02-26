import cv2
import os
import numpy as np

image_path = "mypic.jpg"  # Replace with the correct image path
img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found! Make sure the file exists.")
    exit()

height, width, _ = img.shape

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

msg_encoded = [ord(char) for char in msg]

if len(msg_encoded) >= (height * width):
    print("Error: Message is too long for the image size!")
    exit()

img[0, 0, 0] = len(msg_encoded)

index = 0
for row in range(height):
    for col in range(1, width):  
        if index < len(msg_encoded):
            img[row, col, 0] = msg_encoded[index] 
            index += 1
        else:
            break

cv2.imwrite("encryptedImage.jpg", img)
print("Message successfully hidden in 'encryptedImage.jpg'")

os.system("start encryptedImage.jpg")

decryption_password = input("Enter passcode for decryption: ")

if decryption_password == password:
    print("Correct password. Decrypting...")

    message_length = img[0, 0, 0]

    decrypted_msg = ""
    index = 0

    for row in range(height):
        for col in range(1, width):
            if index < message_length:
                decrypted_msg += chr(img[row, col, 0]) 
                index += 1
            else:
                break

    print("Decryption successful! Message:", decrypted_msg)

else:
    print("ERROR: Incorrect password. Access denied.")
