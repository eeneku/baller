# -*- coding: utf-8 -*-

from engine import component

class BallSpawner(component.Component):
    """ Ball spawner component. Spawns the balls. """

    def __init__(self, *args, **kwargs):
        
        super(BallSpawner, self).__init__(*kwargs, **kwargs)
