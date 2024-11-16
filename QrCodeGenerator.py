import qrcode

while True:
    x = input("input link you want to convirt : ")
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=2,
    )
    qr.add_data(x)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#000", back_color="#fff")
    img.save(r'C:\Users\Nour`s PC\Desktop\qr.png')
    print('QR saved to Desktop succefully ! \n')