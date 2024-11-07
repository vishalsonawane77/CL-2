import RPi.GPIO as gp
import time
import yagmail  # Be sure to install yagmail library before running (to install yagmail, run this command -> `pip install yagmail`)
sensor_pin = 18

gp.setmode(gp.BCM)
gp.setup(sensor_pin,gp.IN)
pwd = ' ' # Enter your app password here

# To get app password, you need to turn on 2 step verification on your google account, then follow these steps to get your app password
# Step 1:
#   - Go to google.com
# Step 2:
#   - Click on your profile photo in top right corner, then click "manage your google account"
# Step 3:
#   - Type in the search bar "App password", then click on "App password"
# Step 4:
#   - You will be prompted with a Text box, Enter "mail" then hit Enter, You will get your 16 password, that's your `pwd`

yag = yagmail.SMTP('yourEmailId@gmail.com',pwd)

while 1:
    if gp.input(sensor_pin)==1:
        yag.send(to='receiverEmailId@gmail.com',subject='Motion detected!',contents='Attention! Motion is detected around the sensor')
        print('Motion detected!')
    time.sleep(2)