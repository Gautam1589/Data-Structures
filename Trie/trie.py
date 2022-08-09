class trie_node:
    def __init__(self):
        self.arr=[None]*26
        self.flag=False

class trie:
    def __init__(self,root):
        self.root=root
        
if __name__=='__main__':
    s=['cap','cat','coco','country','count']
    trie(s)