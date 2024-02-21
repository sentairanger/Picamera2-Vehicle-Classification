# Picamera2-Vehicle-Classification
This project uses two buttons; one to capture an image of a vehicle and another to classify and detect the car in the image. This project also uses OpenVINO for vehicle detection.

## Getting Started

To get started, first you'll need a Camera module, but you can also use a USB webcam. Make sure to alter the code if you use a webcam. You can use any kind of mount and if you plan to test this yourself be sure to have a good power supply and make sure that you are connected to a network. Next, follow this [tutorial](https://gist.github.com/sentairanger/caf11a2432ceebd715c6b33c224f4960) to get OpenVINO installed. Also be sure to have an NCS2 in hand. You'll also need to add two buttons; one on GPIO 17 and another on GPIO 27. You can use any kind of button you want, such as a PC front panel switch or even solder one if you want. After everything is set up, you can run this code remotely through SSH or if you choose to use VNC. Run the code with `python3 button_press.py`. Press the first button to capture an image. Press the second one to classify and detect. You should get the color of the vehicle and type. Note that there could be some inaccuracies based on the color and type so be sure there is enough light in the image. 

Note: the data directory is empty except for a text file that tells you to add your images there.
