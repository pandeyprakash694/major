from stegano import lsb
import desdeff
from PIL import Image,  ImageFont, ImageDraw
import textwrap

def decode_image(text_to_write,file_location="Decode_templete.png"):
    img = Image.open(file_location)

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('FreeMono.ttf',24)
    #font = ImageFont.load_default().font
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((0,0),text_to_write,(0,0,0),font=font)
    img.save('Decoded_image.jpg')

def main():

    print("Deff Hellman Code \n")
    #Deff Hellman ko code

    #KeyGeneration from Deff.py Level line_no=95
    print("Bob's shared secret:")
    print(desdeff.kBob)

    print("Alice's shared secret (should be equal to Bob's)")
    print(desdeff.kAlice)

    #KeyGeneration from Deff.py Level TWO line_no=120
    print("192-bit Session Key:")
    print(desdeff.sessionKey)

    #Initialization Vector Generation from Deff.py Level THREE line_no=135
    #  AES uses a 16-byte IV:
    print("Initialization Vector:")
    print(desdeff.iv)
    print("\n")


    
    var = "This is the test data"
    encStr= desdeff.crypt.encryptStringENC(var)
    print("Encrypted Text in Image:")
    print(encStr)
    print("\n")

    path=input('Enter Image Location : ')
    secret = lsb.hide(path, encStr)

    secret.save("Lenna-secret.png")

    to_decode_text = lsb.reveal("Lenna-secret.png")
    print("Decrypted Text from Image:")
    print(to_decode_text)

    decoded_text=desdeff.crypt.decryptStringENC(to_decode_text)



    print("Original Text is:")
    print(decoded_text)

    decode_image(decoded_text)






main()

