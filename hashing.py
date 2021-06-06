class HashTable():

    def __init__(self):
        self.max_length = 10
        self.length = 0
        self.table = [None] * self.max_length
        self.op=[0]*self.max_length

    def __len__(self):
        return self.length
    
    def find(self, key):
        hv=key%self.max_length
        for j in range(self.max_length):
            temp=(hv+j)%self.max_length
            if(self.table[temp]==key):
                return temp
            if(self.table[temp]==None and self.op[temp]!=-1):
                return -1
    
    def insert(self,key):
        hv=key%self.max_length
        for j in range(self.max_length):
            temp=(hv+j)%self.max_length
            if(self.table[temp]==key):
                break
            if(self.table[temp]==None):
                self.table[temp]=key
                self.op[temp]=1
                self.length+=1
                break
            
        if self.length/self.max_length>0.75:
            if self.table.count(None)==0:
                self.resize()
            
    def delete(self,key):
        temp=self.find(key)
        if(temp!=-1):
            self.length-=1
            self.op[temp]=-1
            self.table[temp]=None
            
    def resize(self):
        self.table=self.table+[None]*(self.max_length//2)
        self.op=self.op+[0]*(self.max_length//2)
        self.max_length+=self.max_length//2
        
    def __repr__(self):
        return str(self.table)
                
        
ht=HashTable()
for i in [22,48,112,77,82,62,22,108,22]:
    ht.insert(i)
print(ht.max_length)
print(len(ht))
print(ht)
print(ht.op)
print(ht.table)
print(ht.find(22))
print(ht.find(83))
ht.delete(112)
print(ht)
ht.delete(55)
print(ht)
ht.delete(112)
print(ht)
ht.delete(82)
print(ht)
print(ht.op)
ht.insert(76)
print(ht)
print(ht.op)
print(ht.max_length)
ht.insert(86)
print(ht)
print(ht.op)
ht.insert(96)
print(ht)
print(ht.op)
print(ht.max_length)
