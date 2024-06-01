#!/usr/bin/env python3

# --*-- --*--
# Adapted from 'Create an Animated GIF of the Weather Radar in Australia' by Roland Thompson
# https://medium.com/@rolanditaru/create-an-animated-gif-of-the-weather-radar-in-australia-37446a0f4de0
# --*-- --*--

import io
import ftplib
from PIL import Image
import time

print("")
radar_id = input("Enter the radar ID: ")
print("")

start = time.time()
print(f"{"{:.2f}".format(round((start - start), 2))} | Starting...")

frames = []

ftp = ftplib.FTP('ftp.bom.gov.au')
ftp.login()
ftp.cwd('anon/gen/radar_transparencies/')

print(f"{"{:.2f}".format(round((time.time() - start), 2))} | Connected to the FTP server")

# Get the legend image
file_obj = io.BytesIO()

ftp.retrbinary('RETR ' + f'IDR.legend.0.png', file_obj.write)
base_image = Image.open(file_obj).convert('RGBA')
    
print(f"{"{:.2f}".format(round((time.time() - start), 2))} | Added legend to the background")

# Get the background and topography images
for layer in ['background', 'topography']:
    file_obj = io.BytesIO()

    ftp.retrbinary('RETR ' + f'{radar_id}.{layer}.png', file_obj.write)
    image = Image.open(file_obj).convert('RGBA')
    base_image.paste(image, (0,0), image)
    
    print(f"{"{:.2f}".format(round((time.time() - start), 2))} | Added {layer} to the background")

ftp.quit()


# Connect to the rader FTP server
ftp = ftplib.FTP('ftp.bom.gov.au')
ftp.login()
ftp.cwd('anon/gen/radar/')

# Get the last 5 radar images
files = [file for file in ftp.nlst() if file.startswith(radar_id) and file.endswith('.png')][-5:]

# Loop over the files and append the image data into our image list
for file in files:
    file_obj = io.BytesIO()

    try:
        ftp.retrbinary('RETR ' + file, file_obj.write)
        image = Image.open(file_obj).convert('RGBA')
        frame = base_image.copy()
        frame.paste(image, (0,0),image)
        frames.append(frame)
        print(f"{"{:.2f}".format(round((time.time() - start), 2))} | Added {file} to the frames list")
    except Exception as e:
        print(f'Error: {e}')

print(f"{"{:.2f}".format(round((time.time() - start), 2))} | All images loaded!")

ftp.quit()


# Overlay range and location over the frames
ftp = ftplib.FTP('ftp.bom.gov.au')
ftp.login()
ftp.cwd('anon/gen/radar_transparencies/')

for i, frame in enumerate(frames):
    for layer in ['range', 'locations']:
        file_obj = io.BytesIO()
        ftp.retrbinary('RETR ' + f'{radar_id}.{layer}.png', file_obj.write)
        range_image = Image.open(file_obj).convert('RGBA')
        frame.paste(range_image, (0,0), range_image)
        frames[i] = frame
        print(f"{"{:.2f}".format(round((time.time() - start), 2))} | Added {layer} to frame {i}")

# Save the frames as a gif
print(f"{"{:.2f}".format(round((time.time() - start), 2))} | Creating the gif...")
frames[0].save('radar.gif', save_all=True, append_images=frames[1:], duration=500, loop=0)

# Alert the user that the gif has been created
print(f"{"{:.2f}".format(round((time.time() - start), 2))} | Done!")
print("")