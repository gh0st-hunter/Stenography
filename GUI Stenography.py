import cv2
import os
import numpy as np
from tkinter import Tk, filedialog, Label, Button, Entry, messagebox
from cryptography.fernet import Fernet
from PIL import Image, ImageTk

def generate_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_message(message, key):
    cipher = Fernet(key)
    return cipher.encrypt(message.encode()).decode()

def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_message.encode()).decode()

def select_image():
    global img, image_path
    image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    
    if not image_path:
        return
    
    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Could not open image.")
        return
    
    pil_img = Image.open(image_path)
    pil_img.thumbnail((200, 200))
    img_tk = ImageTk.PhotoImage(pil_img)
    image_label.config(image=img_tk)
    image_label.image = img_tk

def encode_message():
    global img, image_path
    if img is None:
        messagebox.showerror("Error", "Please select an image first.")
        return
    
    msg = msg_entry.get()
    password = password_entry.get()

    if not msg or not password:
        messagebox.showerror("Error", "Please enter a message and passcode.")
        return
    
    height, width, _ = img.shape
    key = load_key()
    msg_encrypted = encrypt_message(msg, key)
    msg_encoded = [ord(char) for char in msg_encrypted]

    if len(msg_encoded) >= (height * width):
        messagebox.showerror("Error", "Message too long for image size!")
        return

    img[0, 0, 0] = len(msg_encoded) // 255
    img[0, 0, 1] = len(msg_encoded) % 255

    index = 0
    for row in range(height):
        for col in range(1, width):  
            if index < len(msg_encoded):
                img[row, col, 0] = msg_encoded[index]  
                index += 1
            else:
                break

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        cv2.imwrite(save_path, img)
        messagebox.showinfo("Success", "Message hidden successfully!")

def decode_message():
    global img, image_path
    if img is None:
        messagebox.showerror("Error", "Please select an image first.")
        return

    entered_passcode = password_entry.get()
    if not entered_passcode:
        messagebox.showerror("Error", "Please enter the passcode to decrypt.")
        return

    height, width, _ = img.shape
    key = load_key()

    message_length = (img[0, 0, 0] * 255) + img[0, 0, 1]
    decrypted_msg = ""
    index = 0

    for row in range(height):
        for col in range(1, width):
            if index < message_length:
                decrypted_msg += chr(img[row, col, 0])  
                index += 1
            else:
                break

    try:
        decrypted_msg = decrypt_message(decrypted_msg, key)
        messagebox.showinfo("Decrypted Message", decrypted_msg)
    except:
        messagebox.showerror("Error", "Incorrect passcode or corrupted image!")

generate_key()
root = Tk()
root.title("Image Steganography Tool")
root.geometry("400x500")

Label(root, text="Image Steganography", font=("Arial", 16, "bold")).pack(pady=10)

Button(root, text="Select Image", command=select_image).pack(pady=5)
image_label = Label(root)
image_label.pack()

Label(root, text="Enter Secret Message:").pack(pady=5)
msg_entry = Entry(root, width=40)
msg_entry.pack()

Label(root, text="Enter Passcode:").pack(pady=5)
password_entry = Entry(root, width=40, show="*")
password_entry.pack()

Button(root, text="Encode Message", command=encode_message, bg="lightblue").pack(pady=10)
Button(root, text="Decode Message", command=decode_message, bg="lightgreen").pack(pady=5)

root.mainloop()

