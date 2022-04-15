class stack:
    def __init__ (self):
        self.els = []    
    def push (self, el):
        self.els.insert(0, el)
        return el
    def peek (self):
        if self.size() == 0:
            return None
        return self.els[0]
    def pop (self):
        value = self.top()
        if value != None:
            del self.els[0]
        return value        
    def size (self):
        return len(self.els)
    def empty (self):
        return self.size() == 0
