class Node:
        def __init__(self,data):
                self.data=data
                self.nref=None
                self.pref=None
                
class C_doubly_ll:
        
        def __init__(self):
                self.head=None
                self.tail=None

        def create(self,data):
                new_node=Node(data)
                new_node.nref=new_node
                new_node.pref=new_node
                self.head=new_node
                self.tail=new_node

        def insertion(self,data,location):
                new_node=Node(data)
                if self.head is None:
                        new_node.nref=new_node
                        new_node.pref=new_node
                        self.head=new_node
                        self.tail=new_node
                else:
                        if location==0:
                                new_node.nref=self.head
                                new_node.pref=self.tail
                                self.head.pref=new_node
                                self.head=new_node
                                self.tail.ref=new_node
                        elif location==-1:
                                new_node.nref=self.head
                                new_node.pref=self.tail
                                self.tail.nref=new_node
                                self.head.pref=new_node
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

        def triverse(self):
                if self.head is None:
                        print("LL is empty ...!")
                else:
                        n=self.head
                        while n is not None:
                                print(n.data,end=" ")
                                
                                if n is self.tail :
                                        break
                                n=n.nref

        def reverse_triversal(self):
                if self.head is None:
                        print("LL is empty ...!")
                else:
                        n=self.tail
                        while n is not None:
                                print(n.data,end=" ")
                                if n == self.head:
                                        break
                                n=n.pref

        def search_element(self,value):
                if self.head is None:
                        print("Linked list is empty ")
                else:
                        n=self.head
                        while n is not None:
                                if n.data==value:
                                        return value
                                if n==self.tail:
                                        break
                                n=n.nref
                        return "element is not found "
                                                
Dll=C_doubly_ll()

Dll.insertion(1,0)
Dll.insertion(0,0)
Dll.insertion(90,-1)
Dll.insertion(91,-1)
Dll.insertion(92,-1)
Dll.insertion(93,-1)
Dll.insertion(2,2)

Dll.triverse()
print()
Dll.reverse_triversal()
print()
print(Dll.search_element(92))                      
