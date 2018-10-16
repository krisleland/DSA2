'''
Created on Sep 12, 2018

@author: Kris
'''

class Edge(object):
    '''
    classdocs
    '''


    def __init__(self, start_vertex, end_vertex, weight):
        '''
        Constructor
        '''
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.weight = weight
        