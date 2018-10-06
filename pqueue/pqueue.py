'''
Created on Sep 16, 2018

@author: Kris
'''

class pqueue(object):

    
    def __init__(self):
        '''
        Constructor
        '''
        self.pqueue = []
        
    def cmp_lt(self, x, y):
        return (x < y) if hasattr(x, '__lt__') else (not y <= x)
    
    def heappush(self, item):
        """Push item onto heap, maintaining the heap invariant."""
        self.pqueue.append(item)
        self._siftdown(0, len(self.pqueue)-1)
        
    def heappop(self):
        """Pop the smallest item off the heap, maintaining the heap invariant."""
        lastelt = self.pqueue.pop()    # raises appropriate IndexError if heap is empty
        if self.pqueue:
            returnitem = self.pqueue[0]
            self.pqueue[0] = lastelt
            self._siftup(0)
        else:
            returnitem = lastelt
        return returnitem
    
    def _siftdown(self, startpos, pos):
        newitem = self.pqueue[pos]

        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = self.pqueue[parentpos]
            if self.cmp_lt(newitem.current_distance, parent.current_distance):
                self.pqueue[pos] = parent
                pos = parentpos
                continue
            break
        self.pqueue[pos] = newitem
        
    def _siftup(self, pos):
        endpos = len(self.pqueue)
        startpos = pos
        newitem = self.pqueue[pos]
        # Bubble up the smaller child until hitting a leaf.
        childpos = 2*pos + 1    # leftmost child position
        while childpos < endpos:
            # Set childpos to index of smaller child.
            rightpos = childpos + 1
            if rightpos < endpos and not self.cmp_lt(self.pqueue[childpos].current_distance, self.pqueue[rightpos].current_distance):
                childpos = rightpos
            # Move the smaller child up.
            self.pqueue[pos] = self.pqueue[childpos]
            pos = childpos
            childpos = 2*pos + 1
        # The leaf at pos is empty now.  Put newitem there, and bubble it up
        # to its final resting place (by sifting its parents down).
        self.pqueue[pos] = newitem
        self._siftdown(startpos, pos)