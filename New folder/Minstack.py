class MinStack(object):

    def __init__(self):
        """
        data structure .
        """
        self.stack = []
        self.minimum = None  
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) == 0:
            self.stack.append(x)
            self.minimum = x
        else:
            if x >= self.minimum:
                self.stack.append(x)
            else:
                self.stack.append(2*x - self.minimum)
                self.minimum = x
                
    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) == 0:
            raise IndexError
            
        if self.stack[-1] < self.minimum: # Using this as flag for setting next minimum
            val = self.minimum
            self.minimum = 2*self.minimum - self.stack[-1]
            self.stack.pop()
            return val
        return self.stack.pop()
        
    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            raise IndexError
        
        if self.stack[-1] < self.minimum:
            if self.stack[-1] < 0:
                return self.minimum
            else:
                return 2*self.minimum - self.stack[-1]
        return self.stack[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return -1
        return self.minimum

'''
push:O(1)
getMin:O(1)
pop:O(1)

'''
heap=MinStack()
heap.push(1)
heap.push(2)
heap.push(10)
heap.push(-10)
print("min ->"+str(heap.getMin()))
print("poped ->"+str(heap.pop()))
print("min ->" + str(heap.getMin()))






