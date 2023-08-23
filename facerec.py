import pygame
import pygame.camera
from os import path

pygame.camera.init()
camlist = pygame.camera.list_cameras()
print(camlist)

if camlist:
    cam = pygame.camera.Camera(camlist[0], (640,480))
    cam.start()
    image = cam.get_image()
    pygame.image.save(image, "pic.jpg")

else:
    print("No camera")

filepath = 'C:\Random\pic.jpg'
file = open(filepath,'r')