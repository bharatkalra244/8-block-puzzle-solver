import copy
import queue
import time
import heapq


Q = queue.SimpleQueue()
begin = time.time()
Q = queue.SimpleQueue()
visited = []
children=[]
path_length=0


class blockstate:
    def __init__(self,parent,lst,xy):
        self.parent=parent
        self.lst=lst
        self.xy=xy

    def __eq__(self, other):
        return (self.cost(end)==other.cost(end))

    def __ne__(self, other):
        return (self.cost(end)!=other.cost(end))

    def __lt__(self, other):
        return (self.cost(end)<other.cost(end))

    def __le__(self, other):
        return (self.cost(end)<=other.cost(end))

    def __gt__(self, other):
        return (self.cost(end)>other.cost(end))

    def __ge__(self, other):
        return (self.cost(end)>=other.cost(end))
    
    def equal(self,other):
        if(self.lst==other.lst):
            return(1)
        else:
            return(0)

    def print_list(self):
        global path_length
        path_length+=1
        for i in self.lst:
            print(i)

    def print_all(self):
        if(self.parent is None):
            return
        self.parent.print_all()
        self.print_list()

        print("---------------")
    
    def cost(self,other):
        count = int(0)
        for i in range(3):
            for j in range(3):
                if (self.lst[i][j]!=other.lst[i][j]):
                    count+=1
        return(count)

initial1 = [[2,0,3],[1,8,4],[7,6,5]] #(0,1)
initial2 = [[2,8,3],[1,4,5],[7,6,0]] #(2,2)
initial3 = [[2,8,3],[0,1,5],[7,4,6]] #(1,0)
initial4 = [[8,1,3],[2,5,6],[0,7,4]] #(2,0)
initial5 = [[8,1,3],[5,0,6],[2,7,4]] #(1,1)
goal = [[1,2,3],[8,0,4],[7,6,5]]
end = blockstate(None,goal,(1,1))

# IF YOU WANT TO CHECK OTHER INITIAL STATES
start = blockstate(None,initial2,(2,2))  # CHANGE INITIAL LIST HERE AND ALSO THE POSITION OF ZERO

Q.put(start)


def up(bs):
    x,y=bs.xy
    newlst = copy.deepcopy(bs.lst)
    if(x>0):
        newlst[x][y]=newlst[x-1][y]
        newlst[x-1][y]=0
    newstate = blockstate(bs,newlst,(x-1,y))
    if(newstate.lst not in visited):
        children.append(newstate)

def right(bs):
    x,y=bs.xy
    newlst = copy.deepcopy(bs.lst)
    if(y<2):
        newlst[x][y]=newlst[x][y+1]
        newlst[x][y+1]=0
    newstate = blockstate(bs,newlst,(x,y+1))
    if(newstate.lst not in visited):
        children.append(newstate)

def down(bs):
    x,y=bs.xy
    newlst = copy.deepcopy(bs.lst)
    if(x<2):
        newlst[x][y]=newlst[x+1][y]
        newlst[x+1][y]=0
    newstate = blockstate(bs,newlst,(x+1,y))
    if(newstate.lst not in visited):
        children.append(newstate)

def left(bs):
    x,y=bs.xy
    newlst = copy.deepcopy(bs.lst)
    if(y>0):
        newlst[x][y]=newlst[x][y-1]
        newlst[x][y-1]=0
    newstate = blockstate(bs,newlst,(x,y-1))
    if(newstate.lst not in visited):
        children.append(newstate)

def move(bs):
        children.clear()
        temp=blockstate(None,initial2,(2,2)) # CHANGE INITIAL LIST HERE AND ALSO THE POSITION OF ZERO
        y,x=bs.xy
        if(x==0):
            right(bs)
        elif(x==1):
            right(bs)
            left(bs)
        elif(x==2):
            left(bs)
        if(y==0):
            down(bs)
        elif(y==1):
            up(bs)
            down(bs)
        elif(y==2):
            up(bs)
        for i in children:
            if i<temp:
                temp=i
        Q.put(temp)



start.print_list()
print("------------")

def solve_bfs(initial,goal):
    while(not Q.empty()):
        curr = Q.get()
        if(curr.lst not in visited):
            visited.append(curr.lst)
            if(curr.equal(goal)):
                curr.print_all()
                break
            else:
                move(curr)
        if(Q.empty()):
            print("NO RESULT")
            global path_length
            path_length=0

solve_bfs(start,end)
print("PATH LENGTH : ",path_length)
end = time.time()
print(end-begin)