# -*- coding: utf-8 -*-

from pyglet import gl

from engine import system

from components import render
from components import transform

class RenderSystem(system.System):
    """ Render system. Draws an image on the screen. """
    
    def __init__(self, entity_manager=None, *args, **kwargs):
        super(RenderSystem, self).__init__(*args, **kwargs)
        
        self.entity_manager = entity_manager
    
    def on_draw(self):
        store = self.entity_manager.get_all_components_of_type(render.Render)

        if store:
            for entity, component in store.iteritems():
                transform_component = self.entity_manager.get_component(entity, transform.Transform)

                if transform_component:
                    #gl.glLoadIdentity()
                    gl.glPushMatrix()
                    #gl.glTranslatef(transform_component.x, transform_component.y, 0.0)
                    gl.glRotatef(transform_component.rotation, 0, 0, 1)
                    gl.glScalef(transform_component.scale, transform_component.scale, 1.0)
                    component.image.blit(transform_component.x, transform_component.y)
                    gl.glPopMatrix()
    
    
    