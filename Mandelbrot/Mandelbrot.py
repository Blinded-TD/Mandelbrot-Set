import numpy as np
import pygame as pg

#initalizing scene
pg.init()
screen = pg.display.set_mode((640,360))
clock = pg.time.Clock()
running = True
dt = 0
td = f"{dt:.2f}"
circ_pos = pg.Vector2(screen.get_height()/2,screen.get_width()/2)

#Text setup
font = pg.font.Font(None,30)
text_surface = font.render(td,True,"blue")
text_rect = text_surface.get_rect()
text_rect.center = (screen.get_height()/4,screen.get_width()/2)
screen.blit(text_surface,text_rect)
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill(color = "#00000000")
    
    #display stuff here
    pg.draw.circle(screen,"blue", (320,180), 20)
    td = f"{dt:.2f}"
    text_surface = font.render(td,True,"blue")


    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        circ_pos.y -= 20 * dt
    if keys[pg.K_s]:
        circ_pos.y += 20 * dt
    if keys[pg.K_a]:
        circ_pos.x -= 20 * dt
    if keys[pg.K_d]:
        circ_pos.x += 20 * dt
    
    pg.display.flip()
    dt = clock.tick(60)/1000
pg.quit()

