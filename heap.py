# helper functions

class EmptyHeapException(Exception):
    ''' Exception for when a heap is empty.'''
    pass

def left(index):
    '''Return index's left child index.
    '''
    return index * 2 + 1


def right(index):
    '''Return index's left child index.
    '''
    return index * 2 + 2
    
    
def parent(index):
    '''Return index's parent index.'''
    
    return (index - 1) // 2


class MinHeap:
    
    def __init__(self, L=None):
        '''Create a new MinHeap.
        This method is complete.'''
        
        if not L:        
            self._data = []
        else:
            self._data = L
            self._min_heapify()

        
    def __len__(self):
        '''Return the length of the MinHeap.
        This method is complete.'''
        
        return len(self._data)
    

    def __str__(self):
        '''Return a string representation of the heap.
        This method is complete.'''
        
        return str(self._data)
    
    
    def insert(self, v):
        '''Insert v in self. Maintain heap property.'''
        
        self._data.append(v)
        self._percolate_up()
    
    
    def extract_min(self):
        '''Remove minimal value in self. Restore heap property.
        Raise EmptyHeapException if heap is empty.'''
        
        if self._data == []:
            raise EmptyHeapException()
        
        self._data[len(self._data) -1], self._data[0] = self._data[0], self._data[len(self._data) -1]
        
        min = self._data.pop()
        
        self._percolate_down(0)
        
        return min
    
    
    def _percolate_up(self):
        '''Restore heap property of self after 
        adding new item'''
        
        end_index = len(self._data) -1
        parent_index = parent(end_index)
        
        while self._data[end_index] < self._data[parent_index] and parent_index >= 0:
            self._data[end_index], self._data[parent_index] = self._data[parent_index], self._data[end_index]
            end_index = parent_index
            parent_index = parent(end_index)
    
    
    def _percolate_down(self, i):
        ''' Restore heap property of subtree 
        rooted at index i.
        '''
        
        # while larger than at least one child
        # swap with smaller child and repeat    
        left_i = left(i)
        right_i = right(i)
        final_i = len(self._data) - 1
        
        while left_i <= final_i or right_i <= final_i:
            if left_i <= final_i and right_i <= final_i:
                if self._data[i] > self._data[left(i)] or self._data[i] > self._data[right(i)]:
                    if self._data[left(i)] < self._data[right(i)]:
                        self._data[i], self._data[left(i)] = self._data[left(i)], self._data[i]
                        i = left(i)
                        left_i = left(i)
                        right_i = right(i)
                    else:
                        self._data[i], self._data[right(i)] = self._data[right(i)], self._data[i]
                        i = right(i)
                        left_i = left(i)
                        right_i = right(i)
                else:
                    return
                    
            elif left_i <= final_i:
                if self._data[i] > self._data[left(i)]:
                    self._data[i], self._data[left(i)] = self._data[left(i)], self._data[i]
                    i = left(i)
                    left_i = left(i)
                    right_i = right(i)
            
            elif right_i <= final_i:
                if self._data[i] > self._data[right(i)]:
                    self._data[i], self._data[right(i)] = self._data[right(i)], self._data[i]
                    i = right(i)
                    left_i = left(i)
                    right_i = right(i)
    
    
    def _min_heapify(self):
        '''Turn unordered list into min-heap.'''
        
        # for each node in the first half of the list
        # percolate down
        pass
    