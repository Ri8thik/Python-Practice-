class Node:
        def __init__(self,data):
                self.data=data
                self.nref=None
                self.pref=None
class Sdll:
        def __init__(self):
                self.head =None
                self.tail=None

        def creation(self,data):
                new_node=Node(data)
                new_node.nref=new_node
                new_node.pref=new_node
                self.head=new_node
                self.tail=new_node

        def insertion(sel,data,location):
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
                                self.tail.nref=new_node
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
                        print("Linked list is empty..!")
                else:
                        n=self.head
                        while n is not None:
                                print(n.data,end=" ")
                                if n==self.tail:
                                        break
                                n=n.nref
        def reverse_triverse(self):
                if self.head is None:
                        print("Linked list is empty..!")
                else:
                        n=self.tail
                        while n is not None:
                                print(n.data,end=" ")
                                if n==self.head:
                                        break
                                n=n.pref
        def search(self,value):
                if self.head is None:
                        print("Linked list is empty..!")
                else:
                        n=self.head
                        while n is not None:
                                if n.data==value:
                                        return value
                                if n==self.tail:
                                        break
                                n=n.nref
                        return "Value not found ...!"

        def deletion(self,location):
                if self.head is None:
                        print("Linked list is empty ...!")
                else:
                        if location==0:
                                if self.head ==self.tail:
                                        self.head.nref=None
                                        self.head.pref=None
                                        self.head=None
                                        self.pref=None
                                else:
                                        self.head=self.head.nref
                                        self.head.pref=self.tail
                                        self.tail.nref=self.head
                        elif location==-1:
                                if self.head ==self.tail:
                                        self.head.nref=None
                                        self.head.pref=None
                                        self.head=None
                                        self.pref=None
                                else:
                                        self.tail=self.tail.pref
                                        self.tail.nref=self.head
                                        self.head.pref=self.tail
                        else:
                                n=self.head
                                index=0
                                while index<location-1:
                                        index+=1
                                        n=n.nref
                                n.nref=n.nref.nref
                                n.nref.pref=n
                                        
                                        


        
                        
                        
