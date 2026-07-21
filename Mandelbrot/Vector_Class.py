import numpy as np
import pygame as pg
class Vector:
    def __init__ (self,start: tuple,end: tuple,color: tuple,line_width: float,arrow_width: float,arrow_height: float):
        self.start = pg.Vector2(start)
        self.end = pg.Vector2(end)
        self.color = color
        self.line_width = line_width
        self.arrow_width = arrow_width
        self.arrow_height = arrow_height
    
    def difference(self):
        return self.end - self.start
   
    def legnth(self):
        return (self.difference()).length()

    def angle(self):
        return np.arctan2(self.difference().y,self.difference().x)

    def arrow_tip(self):
        return pg.Vector2((self.end.x + self.arrow_height*np.cos(self.angle())),(self.end.y + self.arrow_height*np.sin(self.angle())))

    def draw(self,display):
        #points for arrow's polygon
        angle_perp = self.angle() - np.pi/2
        arrow_point_1 = pg.Vector2((self.end.x - self.arrow_width*np.cos(angle_perp)),(self.end.y - self.arrow_width*np.sin(angle_perp)))
        arrow_point_2 = pg.Vector2((self.end.x + self.arrow_width*np.cos(angle_perp)),(self.end.y + self.arrow_width*np.sin(angle_perp)))
        arrow_point_3 = pg.Vector2((self.end.x + self.arrow_height*np.cos(self.angle())),(self.end.y + self.arrow_height*np.sin(self.angle())))

        vector_line = pg.draw.line(display,self.color,self.start,self.end,self.line_width)
        vector_arrow = pg.draw.polygon(display,self.color,((arrow_point_1),(arrow_point_2),(arrow_point_3)))

def complex_vec_multiply(vec1,vec2,start: tuple):
    return Vector((start[0],start[1]),(vec1.end[0]*vec2.end[0] - vec1.end[1]*vec2.end[1],vec1.end[0]*vec2.end[1]+vec2.end[0]*vec1.end[1]),(0,255,0),10,12,14)

def real_to_pg(vec_R,display):
    vec_R.start = pg.Vector2(display.get_width()/2 + vec_R.start.x *display.get_width()/4,display.get_height()/2 + vec_R.start.y*display.get_height()/4)
    vec_R.end = pg.Vector2(display.get_width()/2 + vec_R.end.x *display.get_width()/4,display.get_height()/2 + vec_R.end.y*display.get_height()/4)
    vec_Pg = vec_R
    return vec_Pg

def pg_to_real(vec_pg,display):
    vec_pg.start = pg.Vector2(((vec_pg.start.x)/(display.get_width())*4) - 2, ((vec_pg.start.y)/(display.get_height())*4) - 2)
    vec_pg.end = pg.Vector2(((vec_pg.end.x)/(display.get_width())*4) - 2, ((vec_pg.end.y)/(display.get_height())*4) - 2)
    vec_R = vec_pg
    return vec_R 
class Complex_number:
    def __init__(self, real: float, img: float):
        self.real = real
        self.img = img

def complex_multiplication(num1: Complex_number , num2: Complex_number):
    return Complex_number(num1.real * num2.real - num1.img * num2.img , num1.real * num2.img + num2.real * num1.img )

def complex_addition(num1: Complex_number, num2: Complex_number):
    return Complex_number(num1.real + num2.real, num1.img + num2.img)

def complex_absolute_value(num: Complex_number):
    return np.sqrt((min(abs(num.real), 100)**2) + (min(abs(num.img), 100)**2))

def normalizing_func(num: float):
    if np.isnan(num) or np.isinf(num):
        return 0
    return round(255 - 162*np.arctan(2.5 * num))

