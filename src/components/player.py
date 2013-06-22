# -*- coding: utf-8 -*-

from engine import component

class Player(component.Component):
    """ Player component."""

    def __init__(self, *args, **kwargs):
        
        super(Player, self).__init__(*args, **kwargs)
        
        self.keys = {"turn_left": None,
                     "turn_right": None,
                     "explode": None}
        
        self.rotation_speed = 128
        
        