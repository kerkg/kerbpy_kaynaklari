import pygame
pygame.init()
screen=pygame.display.set_mode((800,400))
clock=pygame.time.Clock
pygame.display.set_caption("müzük programı")
pygame.mixer_music.load("müziğin.mp3")#giriş sarkışı dediğim çöp sizde olmadığı için adını yazmaya gerek duymadım ayrıca sen kendi müziğini koyabilirsin
pygame.mixer_music.play()
while True:
    screen.fill("orange")

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        pygame.display.update()
        clock.tick(40)
