class Node:
        def __init__(self,data):
                self.data=data
                self.ref=None

class Sll:
        def __init__(self):
                self.head=None
                self.tail=None

        def insert_data(self,data,location):
                new_node=Node(data)
                if self.head is None:
                        self.head =new_node
                        self.tail=new_node
                else:
                        if location ==0:
                                new_node.ref=self.head
                                self.head=new_node
                        elif location==-1:
                                new_node.ref=None
                                self.tail.ref=new_node
                                self.tail=new_node
                        else:
                                n=self.head
                                index=0
                                while index<location-1:
                                        n=n.ref
                                        index+=1
                                        
                                new_node.ref=n.ref
                                n.ref=new_node
                                
        def print__ll(self):
                if self.head is None:
                        print("Linked List is empty ...!")
                else:
                        n=self.head
                        while n is not None:
                                print(n.data,end=' ')
                                n=n.ref

        def searchSll(self,value):
                if self.head is None:
                        return "LL is empty ...!"
                else:
                        n=self.head
                        while n is not None:
                                if n.data==value:
                                        return n.data
                                n=n.ref
                        return "data is not present in ll"

        def reverse(self):
                n=self.head
                prev=None
                while n is not None:
                        value=n.ref
                        n.ref=prev
                        prev=n
                        n=value
                self.head=prev

        def middle(self):
                n=self.head
                p=self.head
                while (p is not None and p.ref is not None):
                        p=p.ref.ref
                        n=n.ref
                print(n.data)
                        

ll=Sll()
ll.insert_data(1,0)
ll.insert_data(9,0)
ll.insert_data(8,0)
ll.insert_data(7,0)
ll.insert_data(2,-1)
ll.insert_data(3,-1)
ll.insert_data(1,0)
ll.insert_data(5,3)
ll.insert_data(467,1)

ll.print__ll()


print()
ll.middle()
                        
                                
