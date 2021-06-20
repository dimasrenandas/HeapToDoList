
class MinHeap():
    def __init__(self):
        self.heap = []

        #Untuk menandai maximum size yang pernah aku capai
        self.maxsize = int(0)

        #Untuk menandai real time size
        self.size = int(0)

    def isroot(self,index):
        if index == 0:
            return True
        return False
    
    def isleaf(self,index):
        if index >= self.size//2 and index <= self.size:
            return True
        return False

    def getparent(self, index):
        if self.isroot(index):
            return None
        return (index-1)//2

    def getleftchild(self,index):
        if self.isleaf(index):
            return None
        return (index*2)+1

    def getrightchild(self,index):
        if self.isleaf(index):
            return None
        elif (index*2)+2 >= self.size:
                return None
        return (index*2)+2

    def swap(self,src,dest):
        self.heap[src], self.heap[dest] = self.heap[dest], self.heap[src]

    def heapifyup(self):
        cur = self.size-1
        if self.size>1:
            while(self.heap[self.getparent(cur)] > self.heap[cur]):
                self.swap(cur,self.getparent(cur))
                cur = self.getparent(cur)
                if self.getparent(cur) == None:
                    break

    def heapifydown(self):
        cur = 0
        if self.size == 2:
            if self.getrightchild(cur) != None:
                if self.heap[self.getleftchild(cur)] < self.heap[self.getrightchild(cur)]:
                    self.swap(cur,self.getleftchild(cur))
                    cur = self.getleftchild(cur)
                else:
                    self.swap(cur,self.getrightchild(cur))
                    cur = self.getrightchild(cur)
            else:
                if self.heap[self.getleftchild(cur)] < self.heap[cur]:
                    self.swap(cur,self.getleftchild(cur))
        elif self.size>=3:
            while(self.heap[cur] > self.heap[self.getleftchild(cur)] or self.heap[cur] > self.heap[self.getrightchild(cur)]):
                if self.heap[self.getleftchild(cur)] < self.heap[self.getrightchild(cur)]:
                    self.swap(cur,self.getleftchild(cur))
                    cur = self.getleftchild(cur)
                else:
                    self.swap(cur,self.getrightchild(cur))
                    cur = self.getrightchild(cur)
                if self.getleftchild(cur) == None or self.getrightchild(cur) == None:
                    break
    
    def add(self,data,strtask):
        self.size+=1
        if self.size > self.maxsize:
            self.heap.append((data,strtask))
            self.maxsize+=1
        else:
            self.heap[self.size-1] = data
        self.heapifyup()

    def remove(self):
        self.heap[0] = self.heap[self.size-1]
        self.size-=1
        self.heapifydown()

    def display(self):
        if self.size == 0:
            print("Heap is empty")
        elif self.size == 1:
            print("Parent: " + str(self.heap[self.size-1]) + ", Left Child: None, Right Child: None")
        else:
            for i in range(0,(self.size//2)):
                result = "Parent: " + str(self.heap[i])
                if self.getleftchild(i)!=None:
                    result = result + ", Left Child: " + str(self.heap[self.getleftchild(i)])
                else:
                    result = result + ", Left Child: None"
                if self.getrightchild(i)!=None:
                    result = result+ ", Right Child: " + str(self.heap[self.getrightchild(i)])
                else:
                    result = result + ", Right Child: None" 
                print(result + ".")

    def peek(self):
        if self.size>0:
            return self.heap[0]
        return None
    def diskata(self):
        tempp=self
        for ele in self.heap:
            hasil = str(tempp.peek())
            hasil = ''.join(i for i in hasil if not i.isdigit())
            hasil=hasil[3:].replace(')','')
            print (tempp.peek(),hasil)
            tempp.remove()
    def displayori(self):
        print(self.heap)







def AddData(objn,prio,kata):
    objn.add(prio,kata)

def DisplayMenu():
    print("1.Add Task\n2.Edit Task\n3.Delete Task\n4.Display Task\n5.Pop Task\n6.Import Task")



mnheap = MinHeap()

menu = True

option = 0

while menu == True:
    DisplayMenu()
    print("Choose : ")
    option = int(input())

    if option == 1:
        print("hi1")
        AddData(mnheap,10,"hi")
        AddData(mnheap,2,"hi2")
        AddData(mnheap,8,"hi3")
        AddData(mnheap,9,"hi4")
        AddData(mnheap,3,"hi5")
        AddData(mnheap,4,"hi6")
        AddData(mnheap,1,"hi7")
    elif option == 2:
        print("hi2")
        mnheap.diskata()
    elif option == 3:
        print("hi3")
    elif option == 4:
        print("hi4")
        mnheap.displayori()
    elif option == 5:
        print("hi5")
    elif option == 6:
        print("hi6")
    elif option == 7:
        print("hi7")
        menu=False






