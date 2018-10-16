'''
Created on Sep 12, 2018

@author: Kris
'''


class Vertex(object):

    def __init__(self, address):
        self.address = address
        self.neighbors = {}
        self.current_distance = 1000
        self.prior_node = None

class Customer(Vertex):
    
    def __init__(self, address, demand, due_time):
        super().__init__(address)
        self.demand = demand
        self.due_time = due_time
        
class Depot(Vertex):
    
    def __init__(self, address, capacity, number_trucks):
        super().__init__(address)
        self.capacity = capacity
        self.number_trucks = number_trucks
        self.current_distance = 0
        self.prior_node = 'source'