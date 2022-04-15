class stack:
    def __init__ (self):
        self.els = []    
    def push (self, el):
        self.els.append(el)
        return el
    def top (self):
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
    def is_empty (self):
        return self.size() == 0