# -*- coding: utf-8 -*-

from engine import component

class BallSpawner(component.Component):
    """ Ball spawner component. Spawns the balls. """

    def __init__(self, *args, **kwargs):
        
        super(BallSpawner, self).__init__(*args, **kwargs)

        self.last_spawn = 0
        self.time_between_spawns = 0
        
        self.ball_images = {}