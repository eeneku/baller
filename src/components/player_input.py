# -*- coding: utf-8 -*-

from engine import component

class PlayerInput(component.Component):
    """ Player input component."""

    def __init__(self, *args, **kwargs):
        
        super(PlayerInput, self).__init__(*kwargs, **kwargs)
        
        self.turn_left = None
        self.turn_right = None
        self.explode = None
        