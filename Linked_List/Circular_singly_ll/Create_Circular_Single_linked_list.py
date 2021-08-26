class Node:
        def __init__(self,data):
                self.data=data
                self.ref=None
class circular:
        def __init__(self):
                self.head=None
                self.tail=None

        def circular_ll(self,data):
                new_node=Node(data)
                new_node.ref=new_node
                self.head=new_node
                self.tail=new_node


        def insert_ll(self,data,location):
                new_node=Node(data)
                if self.head is None:
                        new_node.ref=new_node
                        self.head=new_node
                        self.tail=new_node
                else:
                        if location==0:
                                new_node.ref=self.head
                                self.head=new_node
                                self.tail.ref=new_node
                        elif location==-1:
                                new_node.ref=self.head
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
                                
                
        def print_ll(self):
                if self.head is None:
                        print("Linked list is empty...!")
                else:
                        n=self.head
                        while n is not None:
                                print(n.data,end=' ')
                                n=n.ref
                                if n ==self.head:
                                        break
                                
ll=circular()
##ll.circular_ll(2)
ll.insert_ll(1,0)
ll.insert_ll(9,-1)
ll.insert_ll(88,0)
ll.insert_ll(89,-1)
ll.insert_ll(66,2)
ll.print_ll()
