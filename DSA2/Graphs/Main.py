'''
Created on Sep 12, 2018

@author: Kris
'''
from Graphs.Graph import Graph
import csv
from Graphs.Edge import Edge
from Graphs.Package import create_package_list
from Algorithm.BranchBound import BnB
from Algorithm.Dijkstra import Dijkstra

def main():
    graph = Graph()
    graph.add_depot("HUB", 16, 3)
    
    with open('packagefile.txt') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                graph.add_customer(row[1], row[0], row[5])
    with open('distancetable.csv') as distance_file:
        distance_reader = csv.reader(distance_file)
        x = list(distance_reader)
        for i in range(1,len(x)):
            for j in range(0, i):
                graph.add_edge(Edge(graph.node_list[x[i][1]], graph.node_list[x[j][1]], x[i][j+2]))
    print("HEY")
    pack_list = create_package_list()
    x = Dijkstra(graph)
    short_graph = x.short_graph()
    #Make second graph short graph
    y = BnB(graph, graph, pack_list)
    y.run()
    print(y.best_leaf, y.best_leaf.current_distance)    
    
main()