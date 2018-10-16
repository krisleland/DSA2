Get from pqueue.pqueue import pqueue
from Leaf.Leaf import Leaf
from Graphs.Graph import Graph

class BnB(object):
    def __init__(self, graph, short_graph, pack_list):
        self.min_cost = 40
        self.pqueue = pqueue()
        self.pack_list = pack_list
        self.graph = graph
        self.short_graph = short_graph
        self.current_best = 1000
        self.dist_so_far = -100
        self.cust_so_far = 0
        self.doubles = {}
        
    def run(self):
        self.pqueue.heappush(Leaf(self.short_graph.node_list["HUB"], None, self.graph, self.short_graph))
        while self.pqueue.pqueue:
            prune_leaf = self.pqueue.heappop()
            print(prune_leaf.capacity, prune_leaf.number_customers,prune_leaf.truck, prune_leaf.current_distance, prune_leaf.truck_dist, prune_leaf.vertex.address)
            '''
            if self.pruned(prune_leaf) == True:
                continue
            '''
            if "HUB" not in prune_leaf.vertex.neighbors and prune_leaf.vertex.address != 'HUB':
                self.addLeaf(Leaf(self.short_graph.node_list['HUB'], prune_leaf, self.graph, self.short_graph))
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
        if leaf.vertex.address == 'HUB' and leaf.number_customers == 26 and leaf.current_distance < self.current_best:
            self.best_leaf = leaf
            self.current_best = leaf.current_distance
            print(self.current_best)
        if self.pruned(leaf) == False:
            self.doubles[(leaf.vertex.address, tuple(set(leaf.serviced_nodes)), leaf.number_customers)] = leaf.current_distance
            self.pqueue.heappush(leaf)            
        
    def pruned(self, leaf):
        for package in self.pack_list:
            if package.address == leaf.vertex.address:
                if leaf.dist_at_hub < package.arrival or leaf.truck_dist > package.due:
                    return True
                if package.truck != leaf.truck and package.truck != None:
                    return True
            if leaf.truck == 3 and package.truck == 2 and self.short_graph.node_list[package.address] not in leaf.serviced_nodes:
                return True
            if leaf.truck >= 2 and leaf.truck_dist > package.due and self.short_graph.node_list[package.address] not in leaf.serviced_nodes:
                return True
            if package.partners != None and leaf.vertex.address == package.address:
                for partner in self.pack_list:
                    if partner.ID in package.partners:
                        if partner not in leaf.partners:
                            if leaf.dist_at_hub < partner.arrival or leaf.truck_dist > partner.due:
                                return True
                            if partner.truck != leaf.truck and partner.truck != None:
                                return True
        if leaf.truck > 3:
            return True
        
        if leaf.truck == 3 and leaf.number_customers < 10:
            return True
        if (leaf.vertex.address, tuple(set(leaf.serviced_nodes)), leaf.number_customers) in self.doubles.keys():
            if leaf.current_distance >= self.doubles[(leaf.vertex.address, tuple(set(leaf.serviced_nodes)), leaf.number_customers)]:
                return True
        #if self.cust_so_far - 5 >= leaf.number_customers:
            #return True
        #if leaf.current_distance >= self.current_best:
            #return True
        #if leaf.current_distance + leaf.calc_lower_bound() >= self.current_best:
            #return True
        if leaf.calc_lower_all_cust() + leaf.current_distance >= self.current_best:
            return True
        return False
    
    
    
    
    
    