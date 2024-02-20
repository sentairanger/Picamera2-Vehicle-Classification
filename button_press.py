from gpiozero import Button
from button_app import *

# Define the buttons
button = Button(17)
button2 = Button(27)

# Capture the image and then process it to detect and classify the vehicle
while True:
    if button.is_pressed:
        capture()
    if button2.is_pressed:
        plt_show(convert_result(compiled_model_re, image_show(), resize_image(), box_car()))