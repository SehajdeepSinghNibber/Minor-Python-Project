# 📱 QR Code Generator (Python)

A simple Python project that generates a QR code from any URL and saves it as an image using the `qrcode` library.

---

## 🚀 Features

- Generate QR codes from any URL
- Saves QR code as PNG image
- Simple and beginner-friendly code
- Uses Python and Pillow

---

## 🛠️ Requirements

Make sure you have Python installed (3.7+ recommended).

Install the required library:

```bash
pip install qrcode[pil]
````

---

## 📂 Project Structure

```
Qr_code_generator/
│
├── qr_generator.py
├── QR_code_images/
│   └── my_qr_code.png
└── README.md
```

---

## ▶️ How to Run

1. Clone or download this repository
2. Open terminal in project folder
3. Run the script

```bash
python qr_generator.py
```

4. Enter the URL when prompted

```
Enter the URL: https://example.com
```

5. Your QR code will be saved in the `QR_code_images` folder

---

## 💻 Code

```python
import qrcode

url = input("Enter the URL: ").strip()
file_path="C:\\Users\\sehaj\\Desktop\\Minor Python Projects\\Qr_code_generator\\QR_code_images\\my_qr_code.png"

qr = qrcode.QRCode()
qr.add_data(url)

image = qr.make_image()
image.save(file_path)

print("QR code generated and saved successfully!")
```

---

## 🧠 How It Works

* Takes user input (URL)
* Creates QRCode object
* Converts data into QR image
* Saves image to specified path

---

## 🔧 Possible Improvements

* Add custom colors
* Add logo inside QR
* Create GUI using Tkinter
* Generate unique filenames automatically
* Error handling for invalid paths

---

## 📜 License

This project is open source and free to use.

---

## 👤 Author

Sehajdeep Singh

```