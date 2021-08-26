class Node:
        def __init__(self,data):
                self.data=data
                self.ref=None

class circular_ll:
        def __init__(self):
                self.head=None
                self.tail=None
                
        def circular(self,data):
                new_node=Node(data)
                new_node.ref=new_node
                self.head=new_node
                self.tail=new_node
                

        def insert_ll(self,data,location):
                new_node=Node(data)
                if self.head is None:
                        new_node.ref=new_node
                        self.head =new_node
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
                                        index+=1
                                        n=n.ref
                                new_node.ref=n.ref
                                n.ref=new_node

        def print_ll(self):
                if self.head is None:
                        print("Liked list is empty ...!")
                else:
                        n=self.head
                        while n is not None:
                                print(n.data,end=" ")
                                n=n.ref
                                if n==self.head:
                                        break
        def find_data(self,value):
                if self.head is None:
                        print("LL is empty ....!")
                else:
                        n=self.head
                        while n is not None:
                                if n.data ==value:
                                        return value
                                n=n.ref
                                if n==self.head:
                                        break
                        return "Data is not present in the list "



        def delet(self,location):
                if self.head is None:
                        print("ll is empty ")
                else:
                        if location==0:
                                if self.head=self.tail:
                                        self.head.ref=None
                                        self.head=None
                                        self.tail=None
                                else:
                                        self.head=self.head.ref
                                        self.tail.ref=self.head
                        elif location==-1:
                                if self.head=self.tail:
                                        self.head.ref=None
                                        self.head=None
                                        self.tail=None
                                else:
                                        n=self.head
                                        while n is not None:
                                                if n.ref==self.tail:
                                                        break
                                                n=n.ref
                                        n.ref=self.head
                                        self.tail=n
                        else:
                                n=self.head
                                index=0
                                while index<location-1:
                                        index+=1
                                        n=n.ref
                                n.ref=n.ref.ref

                                
                                        
                                        
                                
                                        
                                























                















                                
                                
                                        
                                
                                
                        
