class Node:
        def __init__(self,data):
                self.data=data
                self.ref=None
class sll:
        def __init__(self):
                self.head=None
                self.tail=None

        def insertt(self,data,location):
                new_node=Node(data)
                if self.head is None:
                        self.head=new_node
                        self.tail=new_node
                else:
                        if location ==0:
                                new_node.ref=self.head
                                self.head=new_node
                        elif location == -1:
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

        def delete(self,location):
                if self.head is None:
                        print("LL is empty you can't delete the data ...!")
                else:
                        if location==0:
                                if self.head==self.tail:
                                        self.head=None
                                        self.tail=None
                                else:
                                        self.head=self.head.ref
                        elif location==-1:
                                if self.head==self.tail:
                                        self.head=None
                                        self.tail=None
                                else:
                                        n=self.head
                                        while n is not None:
                                                if n.ref ==self.tail:
                                                        break
                                                n=n.ref
                                        n.ref=None
                                        self.tail=n
                        else:
                                n=self.head
                                index=0
                                while index<location-1:
                                        n=n.ref
                                        index+=1
                                n.ref=n.ref.ref

                                
        def print_ll(self):
                if self.head is None:
                        print("Linked list is empty ..!")
                else:
                        n=self.head
                        while n is not None:
                                print(n.data,end=' ')
                                n=n.ref

ll=sll()
ll.insertt(2,0)
ll.insertt(1,0)
ll.insertt(9,0)
ll.insertt(8,-1)
ll.insertt(2,-1)
ll.insertt(88,2)
ll.delete(3)
ll.print_ll()
                                        
                                
                        
                
