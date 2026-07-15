import numpy as np
import pygame as pg

# Initializing scene
pg.init()
screen = pg.display.set_mode((640, 360))
clock = pg.time.Clock()
running = True
dt, tt = 0, 0
center = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Vector init
vec_start = pg.Vector2(center)
vec_end = pg.Vector2(center.x, center.y + 50)
k = 15  # Arrow head half-width
r = 10   # Arrow length offset

# Text setup
font = pg.font.Font(None, 30)

# Session
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(color=(0, 0, 0)) # Fixed invalid color string

    # Vector Math
    vec_diff = vec_end - vec_start
    vec1_angle = np.arctan2(vec_diff.y, vec_diff.x)
    
    # Orthogonal angle (90 degrees / pi/2 radians)
    orthog_angle = vec1_angle - np.pi / 2 

    # Display stuff here
    pg.draw.line(screen, "blue", vec_start, vec_end, 3)

    # Arrow Head points
    arrow_p1 = vec_end + pg.Vector2(np.cos(orthog_angle), np.sin(orthog_angle)) * k
    arrow_p2 = vec_end - pg.Vector2(np.cos(orthog_angle), np.sin(orthog_angle)) * k
    arrow_p3 = vec_end + pg.Vector2(np.cos(vec1_angle), np.sin(vec1_angle)) * r
    
    pg.draw.polygon(screen, "yellow", (arrow_p1, arrow_p2, arrow_p3), 3)

    # Floor
    pg.draw.line(screen, "red", (0, center.y), (screen.get_width(), center.y))

    # Controls
    keys = pg.key.get_pressed()
    speed = 200 # Pixels per second
    if keys[pg.K_a]:
        vec_end.x -= speed * dt
    if keys[pg.K_d]:
        vec_end.x += speed * dt
    if keys[pg.K_w]:
        vec_end.y -= speed * dt
    if keys[pg.K_s]:
        vec_end.y += speed * dt

    # Rendering Timer
    angle_deg = np.degrees(vec1_angle)
    text_surface = font.render(f"{tt:.02f}s {angle_deg:.02f} deg", True, "blue")
    text_rect = text_surface.get_rect()
    text_rect.center = (screen.get_width() / 2, screen.get_height() / 4)
    screen.blit(text_surface, text_rect)

    # Time stuff
    dt = clock.tick(60) / 1000
    tt += dt
    pg.display.flip()

pg.quit()