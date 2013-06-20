# -*- coding: utf-8 -*-

from engine import component

class Ball(component.Component):
    """ Ball component. """

    def __init__(self, *args, **kwargs):
        
        super(Ball, self).__init__(*kwargs, **kwargs)
        
        self.type = None
        self.attached = False
