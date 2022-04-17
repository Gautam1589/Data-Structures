#BST Construction

class Treenode:
    def __init__(self,data,left,right):
        self.data=data
        self.left=left
        self.right=right

class BST:
    def __init__(self,arr):
        self.arr=arr
        
    def construct(self,low,high):
        if low>high:
            return None

        mid=(low+high)//2
        left_=self.construct(low,mid-1)
        right_=self.construct(mid+1,high)

        newnode=Treenode(self.arr[mid],left_,right_)

        return newnode

    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

    def preorder(self,root):
        if root==None:
            return
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self,root):
        if root==None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)

    def find_min(self,root):
        if root==None:
            return -1
        if root.left is not None:
            return self.find_min(root.left)
        else:
            return root.data

    def find_max(self,root):
        if root==None:
            return -1
        if root.right is not None:
            return self.find_max(root.right)
        else:
            return root.data

    def search(self,root,key):
        if root==None:
            return "Not found"
        if key>root.data:
            return self.search(root.right,key)
        elif key<root.data:
            return self.search(root.left,key)
        else:
            return "Found"

    def insert(self,root,val):
        if root==None:
            return Treenode(val,None,None)

        if val>root.data:
            root.right=self.insert(root.right,val)
        if val<root.data:
            root.left=self.insert(root.left,val)
            
        return root

    def deleteNode(self,root,key):
        if root==None:
            return None
        
        if key>root.data:
            root.right=self.deleteNode(root.right,key)
        elif key<root.data:
            root.left=self.deleteNode(root.left,key)
        else:
            if root.left and root.right:
                left_max=self.find_max(root.left)
                root.data=left_max
                root.left=self.deleteNode(root.left,left_max)
                return root
            elif root.left:
                return root.left
            elif root.right:
                return root.right
            else:
                return None
        
        return root
        

arr=list(map(int,input().split()))
tree=BST(arr)

root=tree.construct(0,len(arr)-1)  #Construct Binary Search Tree with Inorder array

print("Preorder")
tree.preorder(root)  #Preorder Traversal

print("Inorder")
tree.inorder(root)  #Inorder Traversal

print("Postorder")
tree.postorder(root)  #Postorder Traversal

print("Max element",tree.find_max(root))  #Find Maximum element in Binary Search Tree

print("Min element",tree.find_min(root))  #Find Minimum element in Binary Search Tree

key=int(input())
print(tree.search(root,key))  #Search a key in BST

val=int(input())
root=tree.insert(root,val)  #Insert a node/element into BST
print("Inorder")
tree.inorder(root)

val=int(input())
root=tree.deleteNode(root,val)  #Dlete a node/element from BST
print("Inorder")
tree.inorder(root)