# -*- coding: utf-8 -*-

from pyglet import gl

from engine import system

from components import Render
from components import Transform

class RenderSystem(system.System):
    """ Render system. Draws an image on the screen. """
    
    def __init__(self, entity_manager=None, *args, **kwargs):
        super(RenderSystem, self).__init__(*args, **kwargs)
        
        self.entity_manager = entity_manager
    
    def on_draw(self):
        rendr_components, trans_components = self.entity_manager.get_all_components_of_types([Render, Transform])
        
        for render, trans in zip(rendr_components, trans_components):
            gl.glPushMatrix()
            gl.glTranslatef(trans.x, trans.y, 0.0)
            gl.glRotatef(trans.rotation, 0, 0, 1)
            gl.glScalef(trans.scale, trans.scale, 1.0)
            render.image.blit(0, 0)
            gl.glPopMatrix()
    
    
    