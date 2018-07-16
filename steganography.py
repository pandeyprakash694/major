from stegano import lsb

secret = lsb.hide("Lenna.png", "Hello World")

secret.save("Lenna-secret.png")

clear_message = lsb.reveal("Lenna-secret.png")

print(clear_message)