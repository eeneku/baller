# -*- coding: utf-8 -*-

class EntityManager(object):
    """ This class manages all entities in the game. """
    
    def __init__(self, *args, **kwargs):
        self.lowest_unassigned_entity_id = 1
        
        self.entities = []
        self.components = {}
        
    def get_component(self, entity, component):
        store = self.components.get(component.__name__)
        
        return_value = None
        
        if not store:
            print("No entities with component " + component.__name__)
        else:
            result = store.get(entity)
        
            if not result:
                print("Entity " + str(entity) + " does not posses component " + component.__name__)
            else:
                return_value = result
        
        return return_value
    
    def get_components(self, entity, components):
        store = []
        
        for component in components:
            store.append(self.get_component(entity, component))
            
        return store
    
    def get_all_components_of_type(self, component):
        return self.components.get(component.__name__).values()
    
    def get_all_components_of_types(self, components):
        
        store = {}
        # The method below is kinda poor. Should improve. 
        # When you have found the required components and added them to store,
        # you compare each keys length to this. If its the same,
        # then you have one found a group. Otherwise you havent.
        
        components_required = len(components)
        return_value = []
        
        for i in range(components_required):
            return_value.append([])
        
        for component in components:
            temp = self.components.get(component.__name__)
            if temp:
                for entity in temp:
                    store.setdefault(entity, []).append(temp[entity])
                
        for entity in store:
            if len(store[entity]) == components_required:
                for i in range(components_required):
                    return_value[i].append(store[entity][i])

        return tuple(return_value)

    def get_all_entities_possessing_component(self, component):
        store = self.components.get(component.__name__)
        
        return_value = []
        
        if store:
            return_value = store.keys()
            
        return return_value
    
    def add_component(self, entity, component):
        self.components.setdefault(component.__name__, {})[entity] = component()
    
    def add_components(self, entity, components):
        for component in components:
            self.components.setdefault(component.__name__, {})[entity] = component()
    
    def create_entity(self):
        new_id = self.lowest_unassigned_entity_id 
        self.entities.append(new_id)
        self.lowest_unassigned_entity_id += 1
        
        return new_id
    
    def kill_entity(self, entity):
        self.entities.remove(entity)