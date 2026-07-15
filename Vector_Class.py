import numpy as np
import pygame as pg

class Vector:
    def __init__ (self,start,end):
        self.start = start
        self.end = end

    def return_start(self):
        return self.start, self.end

vec1 = Vector((0,1),(2,3))
print(vec1.return_start())