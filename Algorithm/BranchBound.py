from pqueue.pqueue import pqueue
from Leaf.Leaf import Leaf
from Graphs.Graph import Graph

class BnB(object):
    def __init__(self, graph, short_graph):
        self.min_cost = 40
        self.pqueue = pqueue()
        self.graph = graph
        self.short_graph = short_graph
        self.current_best = 1000
        
    def run(self):
        self.pqueue.heappush(Leaf(self.short_graph.node_list["HUB"], None, self.graph, self.short_graph))
        while self.pqueue.pqueue:
            prune_leaf = self.pqueue.pqueue.pop()
            if self.pruned(prune_leaf) == True:
                continue
            
            for neighbor in prune_leaf.vertex.neighbors:
                if neighbor == "HUB":
                    self.addLeaf(Leaf(self.short_graph.node_list[neighbor], prune_leaf, self.graph, self.short_graph))
                else:
                    if self.short_graph.node_list[neighbor] in prune_leaf.serviced_nodes:
                        continue
                    if prune_leaf.capacity == 0:
                        continue
                    self.addLeaf(Leaf(self.short_graph.node_list[neighbor], prune_leaf, self.graph, self.short_graph))
        return self.pqueue
    
    def addLeaf(self, leaf):
        #add leaf.address == 'HUB'
        if (leaf.vertex.address != 'HUB' and leaf.number_customers == 26 and leaf.current_distance + leaf.calc_lower_bound() < self.current_best
            or leaf.vertex.address == 'HUB' and leaf.number_customers == 26 and leaf.current_distance < self.current_best):
            if leaf.vertex.address != 'HUB':
                leaf.current_distance += leaf.calc_lower_bound()
            self.best_leaf = leaf
            self.current_best = leaf.current_distance
            print(self.current_best)
        
        if self.pruned(leaf) == False:
            self.pqueue.heappush(leaf)
        
    def pruned(self, leaf):
        #if leaf.current_distance >= self.current_best:
            #return True
        #if leaf.current_distance + leaf.calc_lower_bound() >= self.current_best:
            #return True
        if leaf.calc_lower_all_cust() + leaf.current_distance >= self.current_best:
            return True
        return False