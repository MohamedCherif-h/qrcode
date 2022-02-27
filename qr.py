#Modules

import qrcode 
import os 


#asking for the link
link = "https://youtu.be/xvFZjo5PgG0"

#making the qr code
img = qrcode.make(link)

#saving the qr code as PNG extension 
img.save("qr.png" , "PNG")





