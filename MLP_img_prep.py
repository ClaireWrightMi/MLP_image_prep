"""
Author: Claire Wright
Date: 2024-06-03

This module is used to grid images and export them as a PDF for the Mountain Legacy Project
"""

import os
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageOps

def addLines(img):
    """Add grid lines to image"""

    w, h = img.size

    v_lines = [int(round(w/4)), int(round(3*w/4)), int(round(w/2))] # get vertical line positions
    pos_list = [((v_lines[0], 0), (v_lines[0], h)), ((v_lines[1], 0), (v_lines[1], h)), ((v_lines[2], 0), (v_lines[2], h)), ((0,int(round(h/2))), (w,int(round(h/2))))] # list of coordinates for drawing lines 
    thickness = int(round(max(h,w)/500))

    draw = ImageDraw.Draw(img)
    for pos in pos_list:
        draw.line(pos, fill=(255, 255, 255), width=thickness)

    diag_pos = [((v_lines[0],0), (v_lines[1],h)),((v_lines[0],h), (v_lines[1],0))]
    for pos in diag_pos:
        draw.line(pos, fill=(255, 255, 255), width=int(round(thickness/2)))

    if h > w:
        gridded_img=img.transpose(Image.ROTATE_90) # flip if portrait image
    else:
        gridded_img =img

    return gridded_img

def gridImages(img_dir):
    """Adds grid to images from folder"""

    gridded_imgs = []
    for img_pth in os.listdir(img_dir):
        # check if the image ends with png or jpg or jpeg
        if (img_pth.endswith(".png") or img_pth.endswith(".jpg") or img_pth.endswith(".jpeg") or img_pth.endswith(".tif") or img_pth.endswith(".tiff")):
            img_pth = os.path.join(img_dir, img_pth)
            img = Image.open(img_pth).convert('RGB')
            gridded_img = addLines(img)
            gridded_imgs.append(gridded_img)
    
    return(gridded_imgs)

def padImages(gridded_imgs):
    """Pads images to letter size at 300 DPI"""
    
    padded_imgs = []
    for img in gridded_imgs:
        resize = (3300-320,2550-640)
        resize_img = ImageOps.contain(img, resize)
        w, h = resize_img.size
        background = Image.new("RGB", (3300,2550), "White")
        background.paste(resize_img, (int(round((3300-w)/2)), int(round((2550-h)/2))))

        padded_imgs.append(background)

    return padded_imgs

def labelImages(img_dir, padded_imgs, survey):
    """Adds label to images"""

    img_names = []
    for img_pth in os.listdir(img_dir):
        # check if the image ends with png or jpg or jpeg
        if (img_pth.endswith(".png") or img_pth.endswith(".jpg") or img_pth.endswith(".jpeg") or img_pth.endswith(".tif") or img_pth.endswith(".tiff")):
            name = os.path.splitext(os.path.basename(img_pth))[0]
            img_names.append(name)

    labelled_imgs = []
    for img, name in zip(padded_imgs, img_names):
        label = survey + " " + name
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("OpenSans_Regular.ttf",60)

        w, h = img.size
        _, _, w_t, h_t = draw.textbbox((0, 0), label, font)
        draw.text(((w-w_t)/2, h-160-h_t/2), label, (0,0,0), font)

        labelled_imgs.append(img)
    
    return labelled_imgs

def main():
    """Gets user input images and names, grids images, and exports to named PDF"""

    surveyor = input("Enter surveyor name: ") 
    year = input("Enter survey year: ")
    station = input("Enter station name: ")

    label = surveyor + " " + year + " " + station

    img_dir = filedialog.askdirectory(title="Select folder of images")
    gridded_imgs = gridImages(img_dir)
    padded_imgs = padImages(gridded_imgs)
    labelled_imgs = labelImages(img_dir, padded_imgs, label)


    save_dir = filedialog.askdirectory(title="Select save location")
    filename = label + ".pdf"
    filename = filename.replace(" ", "_")
    save_path = os.path.join(save_dir, filename)
    labelled_imgs[0].save(save_path, save_all=True, append_images=labelled_imgs[1:])

main()





