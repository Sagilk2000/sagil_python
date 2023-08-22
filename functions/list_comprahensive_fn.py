"""
[expression,loop,codition]
"""
matrix=[[j for j in range(3)]for i in range(3)]
print(matrix)

matrix=[[j for j in range(3)for i in range(3)]]
print(matrix)

"""
reverse a string
"""
string='python'
str=[string[i] for i in range(len(string)-1,-1,-1)]
print(''.join(str))

s='ligas'
name=[s[i] for i in range(len(s)-1,-1,-1)]
print(''.join(name))


p='nakkop'
# pname=[p[i] for i in range(len(p)-1,-1,-1)]
# print(''.join(pname))

def revp(revr):
    revs=''
    for i in revr:
        revs=i+revs
    print(revs)
revr='nakkop'
revp(revr)

