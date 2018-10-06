from Graphs.Graph import Graph
class Leaf(object):
    
    def __init__(self, vertex, parent, graph, short_graph):
        self.vertex = vertex
        self.parent = parent
        self.graph = graph
        self.short_graph = short_graph
        self.capacity = 16
        self.current_distance = self.calc_current_distance()
        self.calc_serviced_nodes()
        
        
    def truck_used(self):
        if self.parent == None:
            used = 0
        elif self.parent.vertex.address == "HUB" and self.capacity == 0:
            used = self.parent.truck_used() + 1
        else:
            used = self.parent.truck_used()
        self.truck = used
        
    def calc_current_distance(self):
        if self.parent == None:
            return 0
        else:
            return self.parent.current_distance + self.graph.node_list[self.parent.vertex.address].neighbors[self.vertex.address]

    def calc_serviced_nodes(self):
        if self.parent == None:
            self.number_customers = 0
            self.serviced_nodes = []
        else:
            self.serviced_nodes = self.parent.serviced_nodes.copy()
            self.number_customers = self.parent.number_customers
            
            if self.vertex.address != "HUB":
                self.number_customers += 1
                self.serviced_nodes.append(self.vertex)
    
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