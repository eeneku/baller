# -*- coding: utf-8 -*-

from engine import component

class Ball(component.Component):
    """ Ball component. """

    def __init__(self, *args, **kwargs):
        
        super(Ball, self).__init__(*args, **kwargs)
        
        self.type = None
        self.attached = False
        self.distance_to_player = 0
        self.angle = 0
