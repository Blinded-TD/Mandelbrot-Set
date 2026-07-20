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
def complex_vec_multiply(a,b,start: tuple):
    return Vector((start[0],start[1]),(a.end[0]*b.end[0] - a.end[1]*b.end[1],a.end[0]*b.end[1]+b.end[0]*a.end[1]),(0,255,0),10,12,14)

