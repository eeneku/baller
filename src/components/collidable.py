# -*- coding: utf-8 -*-

from engine import component

class Collidable(component.Component):
    """ Collidable component. """

    def __init__(self, *args, **kwargs):
        
        super(Collidable, self).__init__(*kwargs, **kwargs)

        self.collided = False