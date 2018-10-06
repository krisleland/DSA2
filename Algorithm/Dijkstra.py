'''
Created on Sep 30, 2018

@author: Kris
'''

from pqueue.pqueue import pqueue
from Graphs.Graph import Graph
from Graphs.Edge import Edge

class Dijkstra(object):
    '''
    classdocs
    '''


    def __init__(self, graph):
        '''
        Constructor
        '''
        self.graph = graph
        self.pq = pqueue()
        
        
    def run(self, vertex):
        for vert in self.graph.node_list.values():
            if vert == vertex:
                vert.current_distance = 0
                vert.prior_node = vertex
            else:
                vert.current_distance = 1000
                vert.prior_node = None
            self.pq.heappush(vert)   
        while self.pq.pqueue:
            vert = self.pq.heappop()
            for neighbor in self.graph.node_list[vert.address].neighbors:
                if neighbor == vert.address:
                    continue
                neighbor_vertex = self.graph.node_list[neighbor]
                neighbor_weight = self.graph.node_list[vert.address].neighbors[neighbor]
                if vert.current_distance + neighbor_weight < neighbor_vertex.current_distance:
                    if neighbor_vertex in self.pq.pqueue:
                        self.pq.pqueue.remove(neighbor_vertex)
                        neighbor_vertex.current_distance = vert.current_distance + neighbor_weight
                        neighbor_vertex.prior_node = vert
                    else:
                        neighbor_vertex.current_distance = vert.current_distance + neighbor_weight
                        neighbor_vertex.prior_node = vert
                    self.pq.heappush(neighbor_vertex)
                
    def short_graph(self):
        min_span_graph = Graph()
        for vert in self.graph.node_list.values():
            if vert.address == 'HUB':
                min_span_graph.add_depot(vert.address, vert.capacity, vert.number_trucks)
            else:
                min_span_graph.add_customer(vert.address, vert.demand, vert.due_time)
        
        for source_vertex in self.graph.node_list.values():
            self.run(source_vertex)
            for end_vertex in self.graph.node_list.values():
                if source_vertex == end_vertex:
                    continue
                if end_vertex.prior_node == source_vertex:
                    min_span_graph.add_edge(Edge(source_vertex, end_vertex, end_vertex.current_distance))
                    self.graph.node_list[source_vertex.address].neighbors[end_vertex.address] = end_vertex.current_distance
        return min_span_graph