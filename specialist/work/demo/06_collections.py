# 06 collections

l = ['bread', 'milk', 'cheese']
print(l)
l.append('butter')
print(l)
print(l[3])
#x = l.pop(3)
x = l.pop()
print(x)
l.insert(0, x)
print(l)
#l1 = l.copy()
l1 = l[:]

for item in l:
    print(item)
    
print(' - '.join(l))
#sss = 'a b c'.split(' ')
sss = list('abc')
print(sss)

t = ('Steve Austin', 'Undertaker', 'HHH')
print(t[0])

#d = {'bread': 1, 'milk': '2 l.', 'cheese': '1 pack'}
d = {'bread': 1,
     'milk': '2 l.',
     'cheese': '1 pack'
    }
print(d['milk'])
d['butter'] = 1
del d['cheese']
print(len(d))
print(d)
print('cheese' in d)
d.get('cheese', '...')

for i in d:
    print(i)
for k, v in d.items():
    print(k, v)  
for i in d.keys():
    print(i)
for i in d.values():
    print(i)

for c in 'abc':
    print(c)
print('hello'[0])
print('hello'[-1])
print('hello'[1:3])
print('hello'[1:])
print('hello'[:4])
print('hello'[:])
print('hello'*5)

ll = [1, 2, 3, 4, 5]
print(all(ll))
print(any(ll))
print(sum(ll))
print(max(ll))
print(min(ll))

lll = [1, 4, 11, 5, 44, 2, 4, 11]
ss = set(lll)
print(ss)
lll = list(ss)# demo/collections.py

# list generator
lg = [i*10 for i in range(1, 10) if i%2 == 0]
# equal to
for i in range(1, 10):
    if i%2 == 0:
        l.append(i*10)
    
