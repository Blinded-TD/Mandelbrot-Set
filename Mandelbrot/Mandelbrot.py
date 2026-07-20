import numpy as np
import pygame as pg
from Vector_Class import Vector,complex_vec_multiply
import random 
#initalizing scene
rng = np.random.default_rng()
pg.init()
screen = pg.display.set_mode((640,360))
clock = pg.time.Clock()
running = True
dt,tt = 0,0
center = pg.Vector2(screen.get_width()/2,screen.get_height()/2)
#vector init
vec1_start = pg.Vector2(center.x,center.y)
vec1_end = pg.Vector2(center.x,center.y+50)
vec1 = Vector((center.x,center.y),(vec1_end.x,vec1_end.y),(200,0,100),10,10,20)
#Text setup
font = pg.font.Font(None,30)
clicked_vectors = []

# session
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill(color = "#00000000")
    
    #vector graphic
    vec1.start =pg.Vector2(center.x,center.y)
    vec1.end = pg.Vector2(vec1_end.x,vec1_end.y)
    vec1_angle = vec1.angle()
    #display stuff here
    floor = pg.draw.line(screen,"red",(0,center.y),(screen.get_width(),center.y) )
    vec1.draw(screen)
    #controls
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            clicked_pos = pg.Vector2(event.pos)
            clicked_vec = Vector((clicked_pos.x,clicked_pos.y),
                                 (30*np.cos(np.pi/4) + clicked_pos.x, 30*np.sin(np.pi/4) + clicked_pos.y),
                                 (255,0,0),5,7,8)
            clicked_vectors.append(clicked_vec)            
            init_start = pg.Vector2(clicked_vec.arrow_tip().x,clicked_vec.arrow_tip().y)
            for i in range(15):                
                vec_extesion = Vector((init_start.x,init_start.y),(30*np.cos(np.pi*i/10) + init_start.x, 30*np.sin(i*np.pi/10) + init_start.y),(255,0,0),5,7,8)
                init_start = pg.Vector2(vec_extesion.arrow_tip().x,vec_extesion.arrow_tip().y)
                clicked_vectors.append(vec_extesion)
    for vec in clicked_vectors:
        vec.draw(screen)
    ## RANDOM SHIT
    scaler = 10
    a = Vector((0*scaler,0*scaler),(0*scaler,1*scaler),(0,255,0),10,12,14)
    b = Vector((0*scaler,0*scaler),(2*scaler,-2*scaler),(0,0,255),10,12,14)
    c = complex_vec_multiply(a,b,(0,0))
    print(c.end[0],c.end[1])               
    clicked_vectors.append(c)
    
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
    text_surface = font.render(f"{tt:.02f}s" + f" {vec1_angle:.02f} deg" ,True,"blue")
    text_rect = text_surface.get_rect()
    text_rect.center = (screen.get_width()/2,screen.get_height()/4)
    screen.blit(text_surface,text_rect)

    #Time stuff
    dt = clock.tick(60)/1000
    tt += dt

    pg.display.flip()
pg.quit()
