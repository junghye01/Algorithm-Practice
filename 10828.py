import sys

class stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def empty(self):
        if len(self.items)==0:
            return 1
        else:
            return 0
    def pop(self):
        if len(self.items)==0:
            return -1
        else:
            return self.items.pop()
    def top(self):
        if len(self.items)==0:
            return -1
        else:
            return self.items[-1]
    def size(self):
        return len(self.items)

acc=stack()


N=int(sys.stdin.readline())
for i in range(N):
    word=sys.stdin.readline().split()
    order=word[0]
   
    if order=='push':
        acc.push(word[1])
    elif order=='top':
        print(acc.top())
    elif order=='size':
        print(acc.size())
    elif order=='pop':
        print(acc.pop())
    elif order=='empty':
        print(acc.empty())
    


