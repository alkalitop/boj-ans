class stack:
    def __init__ (self):
        self.els = []    
    def push (el):
        self.els.append(el)
        return el
    def top ():
        if self.size() == 0:
            return None
        return self.els[0]
    def pop ():
        value = self.top()
        if value != None:
            del self.els[0]
        return value        
    def size ():
        return len(self.els)
    def is_empty ():
        return self.size() == 0
