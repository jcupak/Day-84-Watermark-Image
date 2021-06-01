# Day 84 Watermark Image
# 100 Days of Coding in Python
# 2021-05-31 John Cupak

import os

from tkinter import filedialog
from tkinter import *
from tkinter import ttk

from PIL import Image      # Load / save images
from PIL import ImageDraw  # 2D graphics for images
from PIL import ImageFont  # Write text on image

from datetime import date


def watermark(input_image_path, text):
    """Apply watermark text to input image and save as watermarked file to same folder"""

    print(f"input_image_path: '{input_image_path}'")           # Echo input
    directory_name = os.path.dirname(input_image_path)         # Get directory_name
    input_file = os.path.basename(input_image_path)            # Get file name with extension
    file_name, file_ext = input_file.split('.')                # Split input_file into file_name and file_ext
    output_file = file_name + "_watermarked" + '.' + file_ext  # Append _watermarked to output_file
    output_image_path = directory_name + '/' + output_file     # Append output_file to directory_name
    in_photo = Image.open(input_image_path)                    # Open image
    w, h = in_photo.size                                       # Get image width and height
    drawing = ImageDraw.Draw(in_photo)                         # make the image editable
    black = (3, 8, 12)                                         # RGB
    font = ImageFont.truetype("~/Library/Fonts/OpenSans-Italic.ttf", 64)
    copyright_text = "© " + text + ' ' + \
                     date.today().strftime("%Y-%m-%d") + " "   # Create watermark with text and date
    text_w, text_h = drawing.textsize(copyright_text, font)    # get watermark text width and height
    pos = w - text_w, (h - text_h) - 50                        # Specify where to place watermark text
    drawing.text(pos, copyright_text, fill=black, font=font)   # Add watermark to photo
    in_photo.save(output_image_path)                           # Save watermarked image

    print(f"output_image_path: '{output_image_path}' saved.")  # Feedback


if __name__ == '__main__':

    root = Tk()
    root.withdraw()
    root.resizable(width=800, height=400)
    Title = root.title("File Browser")
    label = ttk.Label(root, text="Select file to watermark", foreground="blue", font="Helvetica, 16")
    label.pack()

    # Get image filename to watermark
    full_path = filedialog.askopenfilename(
        initialdir="/",
        filetypes=(("JPEG File", "*.jpeg"), ("JPG Files", "*.jpg"), ("PNG File", "*.png")),
        title="Select a file.")

    # Watermark image with text
    watermark(full_path, "John J Cupak Jr")
