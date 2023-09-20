input()
ss = input().split()

input()
ns = input().split()

input()
mg = input().split()

input()
st = input()

for v in ss:
    if not v in mg:
        st = st.replace(v, ' ')

for v in ns:
    if not v in mg:
        st = st.replace(v, ' ')
        
for s in st.split():
    print(s)
