import numpy as np
import pygame as pg

#initalizing scene
pg.init()
screen = pg.display.set_mode((640,360))
clock = pg.time.Clock()
running = True
dt,tt = 0,0
center = pg.Vector2(screen.get_width()/2,screen.get_height()/2)
#vector init
vec_start = pg.Vector2(center,center)
vec_end = pg.Vector2(center.x,center.y+50)
vec1_angle = 0
vec1_slope = 0
k = 5
r=5
#Orthogonal Vector
#Text setup
font = pg.font.Font(None,30)

# session
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill(color = "#00000000")
    

    #vector graphic
    vec1_dif = vec_end - vec_start
    vec1_angle = np.arctan2(vec1_dif.y,vec1_dif.x)
    orthog_angle = vec1_angle - np.pi/2
    arrow_point_1 = pg.Vector2(vec_end.x,vec_end.y) - pg.Vector2(k*np.cos(orthog_angle),k*np.sin(orthog_angle))
    arrow_point_2 = pg.Vector2(vec_end.x,vec_end.y) + pg.Vector2(k*np.cos(orthog_angle),k*np.sin(orthog_angle))
    arrow_point_3 = pg.Vector2(vec_end.x,vec_end.y) + pg.Vector2(r*np.cos(vec1_angle),r*np.sin(vec1_angle))

    #display stuff here
    vec1 = pg.draw.line(screen,"blue",
                        vec_start,
                        vec_end,3)
    arrow_head = pg.draw.polygon(screen, "blue",
                                 ((arrow_point_1),
                                  (arrow_point_2),
                                  (arrow_point_3)))
    floor = pg.draw.line(screen,"red",(0,center.y),(screen.get_width(),center.y) )
    
    
    
    
    #controls
    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
        vec_end.x -= 50 * dt
    if keys[pg.K_d]:
        vec_end.x += 50 * dt
    if keys[pg.K_w]:
        vec_end.y -= 50 * dt
    if keys[pg.K_s]:
        vec_end.y += 50 * dt
    
    
    #Rendering Timer
    text_surface = font.render(f"{tt:.02f}s" + f"{vec1_angle:.02f} deg",True,"blue")
    text_rect = text_surface.get_rect()
    text_rect.center = (screen.get_width()/2,screen.get_height()/4)
    screen.blit(text_surface,text_rect)

    #Time stuff
    dt = clock.tick(60)/1000
    tt += dt

    pg.display.flip()
pg.quit()

