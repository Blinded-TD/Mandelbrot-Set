import numpy as np
import pygame as pg
from Vector_Class import Vector,real_to_pg,pg_to_real, Complex_number, complex_multiplication, complex_addition, complex_absolute_value,normalizing_func
#initalizing scene
pg.init()
screen = pg.display.set_mode((640,640))
clock = pg.time.Clock()
running = True

#Creating alternitive cordinate system
origin = pg.Vector2(screen.get_width()/2,screen.get_height()/2)

#image setup
Mandelbrot_Equation_Image = pg.image.load("Mandelbrot Horseshoe Eq.png").convert_alpha()

#numbers of steps
iterations = 20

#initalizing stored vectors
stored_vectors = []

#creating color matrix
color_matrix = np.zeros((screen.get_height()+1,screen.get_width()+1))
for i in range(screen.get_height()+1):
    for j in range(screen.get_width()+1):
        y,x = (i/(screen.get_height())*4 - 2,j/(screen.get_width())*4 - 2) #converting to real cords
        C = Complex_number(x,y)
        Z = Complex_number(0,0)
        for r in range(iterations): #calculating value of sequence 
            Z = complex_addition(complex_multiplication(Z,Z),C)
        color_value = normalizing_func(complex_absolute_value(Z))
        color_matrix[i][j] = color_value

# session
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill(color = "#F3F3F3FF")
    
    #creating Mandelbrot image
    for i in range(screen.get_height() + 1):
        for j in range(screen.get_width() + 1):
            screen.set_at((j,i),(0,0,color_matrix[i][j]))
 
    #Rendering Equation Image 
    screen.blit(Mandelbrot_Equation_Image,(origin.x - 50, origin.y -200))

    #detecting click
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            stored_vectors = []
            clicked_vec_Pg = Vector((origin.x,origin.y),(event.pos[0],event.pos[1]),(0,0,0),2,2,3)
            clicked_vec_R = pg_to_real(clicked_vec_Pg,screen) #turning clicked cords into Real cords
            stored_vectors.append(real_to_pg(clicked_vec_R,screen))
            next_vec_R = clicked_vec_R
            Z = Complex_number(0,0)
            C = Complex_number(event.pos[0]/(screen.get_width())*4 - 2,event.pos[1]/(screen.get_width())*4 - 2)
            Mandelbrot_Results = []
            for i in range(iterations):
                Z = complex_addition(complex_multiplication(Z,Z), C)
                Mandelbrot_Results.append(Z)
            init_vector_R = pg.Vector2(0,0)
            for i in range(iterations): #creating visual vectors  
                next_vec_R = Vector((init_vector_R.x,init_vector_R.y),(Mandelbrot_Results[i].real,Mandelbrot_Results[i].img),(round(255-i*(255/iterations - 1)),0,0),2,2,3)
                init_vector_R = pg.Vector2(next_vec_R.end)
                stored_vectors.append(real_to_pg((next_vec_R),screen))
    #drawing stored vectors 
    for vec in stored_vectors:
        vec.draw(screen)
    pg.display.flip()
pg.quit()
