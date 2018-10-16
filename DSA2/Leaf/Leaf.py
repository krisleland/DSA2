from Graphs.Graph import Graph
class Leaf(object):
    
    def __init__(self, vertex, parent, graph, short_graph):
        self.vertex = vertex
        self.parent = parent
        self.graph = graph
        self.short_graph = short_graph
        self.capacity = 16
        self.calc_serviced_nodes()
        self.current_distance = self.calc_current_distance()
        self.truck_used()
        self.calc_dist_at_hub()
        
        
        
        
    def truck_used(self):
        if self.parent == None:
            self.truck = 1
            self.truck_dist = 0
        elif self.vertex.address == "HUB" and self.parent.truck == 1 and self.number_customers >= 10:
            self.truck = 2
            self.truck_dist = 0
        else:
            self.truck = self.parent.truck
            
    def calc_dist_at_hub(self):
        if self.vertex.address == 'HUB':
            self.dist_at_hub = self.current_distance
        else:
            self.dist_at_hub = self.parent.dist_at_hub   
        
    def calc_current_distance(self):
        if self.parent == None:
            self.truck_dist = 0
            return 0

        else:
            self.truck_dist = self.parent.truck_dist + self.graph.node_list[self.parent.vertex.address].neighbors[self.vertex.address]
            return self.parent.current_distance + self.graph.node_list[self.parent.vertex.address].neighbors[self.vertex.address]
            

    def calc_serviced_nodes(self):
        if self.parent == None:
            self.number_customers = 0
            self.serviced_nodes = []
        else:
            self.serviced_nodes = self.parent.serviced_nodes.copy()
            self.number_customers = self.parent.number_customers
            self.capacity = self.parent.capacity
            
            if self.vertex.address != "HUB":
                self.capacity -= 1
                self.number_customers += 1
                self.serviced_nodes.append(self.vertex)
            else:
                self.capacity = 16
    
    def calc_lower_bound(self):
        if self.vertex.address == "HUB":
            return 0
        else:
            return Graph.get_distance(self.graph, self.graph.node_list[self.vertex.address], self.graph.node_list['HUB'])
        
    def get_min_edge(self, vertex):
        weight = 1000
        for i in self.short_graph.node_list[vertex].neighbors:
            if self.short_graph.node_list[i] not in self.serviced_nodes:
                edge_weight = self.graph.node_list[i].neighbors[vertex]
                if edge_weight < weight:
                    weight = edge_weight
        return weight
    
    def calc_lower_all_cust(self):
        total = 0
        return_cost = 1000
        for vertex in self.short_graph.node_list.keys():
            if vertex == 'HUB':
                continue
            if self.short_graph.node_list[vertex] not in self.serviced_nodes:
                total += self.get_min_edge(vertex)
                if self.graph.node_list['HUB'].neighbors[vertex] < return_cost:
                    return_cost = self.graph.node_list['HUB'].neighbors[vertex]
                
        return total