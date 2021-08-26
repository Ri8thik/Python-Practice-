class Node:
        def __init__(self,data):
                self.data=data
                self.nref=None
                self.pref=None
                
class double_linked_list:
        def __init__(self):
                self.head=None
                self.tail=None
        
        def insert(self,data,location):
                new_node=Node(data)
                if self.head is None:
                        self.head=new_node
                        self.tail=new_node
                        new_node.nref=None
                        new_node.pref=None 
                else:
                        if location==0:
                                new_node.nref=self.head
                                new_node.pref=None
                                self.head.pref=new_node
                                self.head=new_node
                        elif location==-1:
                                new_node.nref=None
                                new_node.pref=self.tail
                                self.tail.nref=new_node
                                self.tail=new_node
                        else:
                                n=self.head
                                index=0
                                while index<location-1:
                                        index+=1
                                        n=n.nref
                                new_node.nref=n.nref
                                new_node.pref=n
                                new_node.nref.pref=new_node
                                n.nref=new_node

        def printll(self):
                if self.head is None:
                        print("Linked list is empty ...!")
                else:
                        n=self.head
                        while n is not None:
                                print(n.data , end=' ')
                                n=n.nref

        def reverse_triversal(self):
                if self.head is None:
                        print("Dll is empty ...!")
                else:
                        n=self.tail
                        while n is not None:
                                print(n.data,end=' ')
                                n=n.pref

        def search(self,value):
                if self.head is None:
                        print("Linked list is empty ")
                else:
                        n=self.head
                        while n is not None:
                                if n.data==value:
                                        return value
                                n=n.nref
                        return 'element is not found in ll'


                
dll=double_linked_list()

dll.insert(1,0)
dll.insert(0,0)
dll.insert(0,0)

dll.insert(3,-1)
dll.insert(88,3)

dll.printll()
print()
dll.reverse_triversal()



