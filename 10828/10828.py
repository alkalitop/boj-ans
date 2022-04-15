class stack:
    def __init__ (self):
        self.els = []    
    def push (self, el):
        self.els.insert(0, el)
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

import sys
input = sys.stdin.readline

stk = stack()

for i in range(int(input())):
    cmd = input().strip()
    if 'push' in cmd:
        stk.push(int(cmd.split()[1]))
    if cmd == 'pop':
        val = stk.pop()
        print(val if val != None else -1)
    if cmd == 'size':
        print(stk.size())
    if cmd == 'empty':
        print(1 if stk.is_empty() else 0)
    if cmd == 'top':
        val = stk.top()
        print(val if val != None else -1)
