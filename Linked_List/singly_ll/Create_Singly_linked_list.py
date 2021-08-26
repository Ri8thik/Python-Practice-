class Node:
        def __init__(self,data):
                self.data=data
                self.ref=None

class Slinkedlist:
        def __init__(self):
                self.head=None
                self.tail=None


        
singlelinkedlist=Slinkedlist()
node1=Node(1)
node2=Node(2)

singlelinkedlist.head=node1
singlelinkedlist.head.ref=node2
singlelinkedlist.tail=node2




























