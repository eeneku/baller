# -*- coding: utf-8 -*-

class Component(object):
    """ This is the father class for all different components. """
    
    def __init__(self, owner=None, *args, **kwargs):
        self.owner = owner