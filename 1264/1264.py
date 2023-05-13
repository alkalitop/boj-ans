while 1:
    s = input()
    if s == '#': break
    print(sum(list(map(lambda z: s.lower().count(z), ['a', 'e', 'i', 'o', 'u']))))
    
    
    
    
