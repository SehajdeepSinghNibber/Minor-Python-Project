# pip insrall qrcode[pil]

import qrcode

url = input("Enter the URL: ").strip()
file_path="C:\\Users\\sehaj\\Desktop\\Minor Python Projects\\Qr_code_generator\\QR_code_images\\my_qr_code.png"

qr = qrcode.QRCode()
qr.add_data(url)

image = qr.make_image()
image.save(file_path)

print("QR code generated and saved successfully!")