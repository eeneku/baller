# -*- coding: utf-8 -*-

from engine import component

class Transform(component.Component):
    """ Transform component."""

    def __init__(self, *args, **kwargs):
        
        super(Transform, self).__init__(*args, **kwargs)
        
        self.x = 0
        self.y = 0
        self.rotation = 0
        self.scale = 1
        self.anchor_x = 0
        self.anchor_y = 0
        