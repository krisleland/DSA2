'''
Created on Sep 12, 2018

@author: Kris
'''

from Graphs.Vertex import Customer, Depot

class Graph(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.adjacency_list = {}
        self.node_list = {}
        
    def add_customer(self, address, demand, due_time):
        self.node_list[address] = Customer(address,demand, due_time)
        
    def add_edge(self, edge):
        if edge.end_vertex.address not in self.node_list[edge.start_vertex.address].neighbors.keys():
            self.node_list[edge.start_vertex.address].neighbors[edge.end_vertex.address] = float(edge.weight)
            
        #elif edge not in self.node_list[edge.start_vertex.address].neighbors[edge.end_vertex.address]:
        #    self.node_list[edge.start_vertex.address].neighbors[edge.end_vertex.address].append(edge)
            
        if edge.start_vertex.address not in self.node_list[edge.end_vertex.address].neighbors.keys():
            self.node_list[edge.end_vertex.address].neighbors[edge.start_vertex.address] = float(edge.weight)
            
        #elif edge not in self.node_list[edge.end_vertex.address].neighbors[edge.start_vertex.address]:
        #    self.node_list[edge.end_vertex.address].neighbors[edge.start_vertex.address].append(edge)
    def add_depot(self, address, capacity, number_trucks):
        self.node_list["HUB"] = Depot(address, capacity, number_trucks)
        
    def get_distance(self, start_vertex, end_vertex):
        return self.node_list[start_vertex.address].neighbors[end_vertex.address]