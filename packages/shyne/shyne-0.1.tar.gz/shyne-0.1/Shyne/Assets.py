import pygame
import os

path = os.path.dirname(__file__) + "/Assets/"

images = {"add": pygame.image.load(path + "Images/add.png")}


def init():
    global images
    for image in images.values():
        image.convert_alpha()
