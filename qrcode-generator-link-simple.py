import qrcode

url = input("Coloque a URL: ").strip()
file_path = "qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("Seu QR Code foi gerado!")

#https://www.youtube.com/watch?v=pJdTyvufOdg