import tkinter as tk
from tkinter import filedialog, messagebox
from steganography import encode_text_to_image, decode_text_from_image

def choose_image():
    file_path.set(filedialog.askopenfilename(filetypes=[("PNG files", "*.png")]))


def encode():
    img_path = file_path.get()
    message = text_box.get("1.0", tk.END).strip()
    if not img_path or not message:
        messagebox.showerror("Error", "Please select an image and enter a message.")
        return
    output = encode_text_to_image(img_path, message, "encoded_output.png")
    messagebox.showinfo("Success", f"Message encoded and saved to {output}")


def decode():
    img_path = file_path.get()
    if not img_path:
        messagebox.showerror("Error", "Please select an image to decode.")
        return
    message = decode_text_from_image(img_path)
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, message)

# GUI Layout
root = tk.Tk()
root.title("LSB Steganography Tool")

file_path = tk.StringVar()

tk.Label(root, text="Image File:").grid(row=0, column=0, sticky='e')
tk.Entry(root, textvariable=file_path, width=40).grid(row=0, column=1)
tk.Button(root, text="Browse", command=choose_image).grid(row=0, column=2)

tk.Label(root, text="Message:").grid(row=1, column=0, sticky='ne')
text_box = tk.Text(root, height=10, width=50)
text_box.grid(row=1, column=1, columnspan=2)

tk.Button(root, text="Encode", command=encode).grid(row=2, column=1, sticky='e', pady=10)
tk.Button(root, text="Decode", command=decode).grid(row=2, column=2, sticky='w')

root.mainloop()
