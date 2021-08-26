class Node:
        def __init__(self,data):
                self.data=data
                self.nref=None
                self.pref=None
class doblly_ll:
        def __init__(self):
                self.head=None
                self.tail=None
                
        def insertion(self,data,location):
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
                                neW_node.pref=self.tail
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
                                
        def triverse(self):
                if self.head is None:
                        print("Linked list is empyt ..!")
                else:
                        n=self.head
                        while n is not None:
                                print(n.data,end=" ")
                                n=n.nref
                                
        def reverse_triverse(self):
                if self.head is None:
                        print("Linked list is empyt ..!")
                else:
                        n=self.tail
                        while n is not None:
                                print(n.data,end=" ")
                                n=n.pref

        def search(self,value):
                if self.head is None:
                        print("Linked list is empyt ..!")
                else:
                        n=self.head
                        while n is not None:
                                if n.data==value:
                                        return value
                                n=n.nref
                                
                        return " element is not found "
                
        def deletion(self,location):
                if self.head is None:
                        print("LL is empty ..!")
                else:
                        if location==0:
                                if self.head ==self.tail:
                                        self.head=None
                                        self.tail=None
                                else:
                                        self.head =self.head.nref
                                        self.head.pref=None
                        elif location==-1:
                                if self.head==self.tail:
                                        self.head=None
                                        self.tail=None
                                else:
                                        self.tail=self.tail.pref
                                        self.tail.nref=None
                        else:
                                n=self.head
                                index=0
                                while index<location-1:
                                        n=n.nref
                                        index+=1
                                n.nref=n.nref.nref
                                n.nref.pref=n
        def complete_ll_delet(self):
                if self.head is None:
                        print("LL is already empty ..!")
                else:
                        n=self.head
                        while n is not None:
                                n.pref=None
                                n=n.nref
                        self.head=None
                        self.tail=None
        
                                
                                
                                        
                        
                                
                









                                
                                
                                
                
