import numpy as np
import pygame as pg
from Vector_Class import Vector

#initalizing scene
pg.init()
screen = pg.display.set_mode((2*640,2*360))
clock = pg.time.Clock()
running = True
dt,tt = 0,0
center = pg.Vector2(screen.get_width()/2,screen.get_height()/2)
#vector init
vec1_start = pg.Vector2(center.x,center.y)
vec1_end = pg.Vector2(center.x,center.y+50)
vec1 = Vector((center.x,center.y),(vec1_end.x,vec1_end.y),(200,0,100),10,10,20)
vec2_start = pg.Vector2(vec1.arrow_tip().x,vec1.arrow_tip().y)
vec2_end = pg.Vector2(50,50)
vec2 = Vector(vec2_start,vec2_end,(256,256,256),vec1.line_width/2,5,10)
#Text setup
font = pg.font.Font(None,30)


# session
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill(color = "#00000000")
    
    #vector graphic
    vec1 = Vector((center.x,center.y),(vec1_end.x,vec1_end.y),(200,0,100),10,10,20)
    vec2_start = pg.Vector2(vec1.arrow_tip().x,vec1.arrow_tip().y)
    vec2 = Vector(vec2_start,vec2_end,(255,255,255),5,5,10)
    vec1_angle = vec1.angle()
    vec2_angle = vec2.angle()
    #display stuff here
    floor = pg.draw.line(screen,"red",(0,center.y),(screen.get_width(),center.y) )
    vec1.draw(screen)
    vec2.draw(screen)
    #controls
    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
        vec1_end.x -= 50 * dt
    if keys[pg.K_d]:
        vec1_end.x += 50 * dt
    if keys[pg.K_w]:
        vec1_end.y -= 50 * dt
    if keys[pg.K_s]:
        vec1_end.y += 50 * dt
    
    
    #Rendering Timer
    text_surface = font.render(f"{tt:.02f}s" + f" {vec1_angle:.02f} deg" + f" {vec2_angle:.02f} deg",True,"blue")
    text_rect = text_surface.get_rect()
    text_rect.center = (screen.get_width()/2,screen.get_height()/4)
    screen.blit(text_surface,text_rect)

    #Time stuff
    dt = clock.tick(60)/1000
    tt += dt

    pg.display.flip()
pg.quit()
