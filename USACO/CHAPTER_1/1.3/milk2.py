"""
ID: a.bonvi96
LANG: PYTHON3
PROG: milk2
"""
import math
import copy
R = 'R'
B = 'B'


class RB_interval_node:
    def __init__(self, low, high, color = R, left=None, right=None, p=None, maximum = 0):
        self.interval = {'low':low,'high':high}
        self.color = color
        self.left = left
        self.right = right
        self.p = p
        self.maximum = maximum
    def __repr__(self):
        if self.interval['low'] == None:
            return 'NIL'
        else:
            return'Interval:{} , Color:{} Max:{} , Parent:{} , Left:{} , Right:{}'.format(self.interval,self.color,self.maximum,self.p.interval,self.left.interval,self.right.interval)



class RedBlack_Int_Tree:
    def __init__(self):
        self.nil = RB_interval_node(None,None,B,None,None,None,0)
        self.root = self.nil
        self.root.left = self.nil
        self.root.right = self.nil
        self.height = 1
        self.n_nodes = 0
    def __repr__(self):
        self._print()
        return '...if the tree maximum height is > 6 the representation may not be complete...'
    
    # What you'll use...
    
    def insert(self,interval):
        new_node = RB_interval_node(interval[0],interval[1],left=self.nil,right=self.nil,p=self.nil)
        self._RB_INSERT(new_node)
        self._update_maximum_bottom_top(new_node)
        self.n_nodes += 1
        self._update_height()
                                           
    def delete(self,interval):
        node = self._Get_Node(interval)
        if not node:
            print('Error: The specified key does not exist in the tree.',file = sys.stderr)
            return
        else:
            self._RB_Delete(node)
            self.n_nodes -= 1
            self._update_height()
    def interval_search(self,i,mode = 'overlap'):
        if mode == 'overlap': # IF PRESENT, RETURN A POINTER TO AN INTERVAL OVERLAPPING THE GIVEN INTERVAL, ELSE RETURN NONE.
            x = self.root
            while x != self.nil and self._isnt_overlapping(i,x):
                if x.left != self.nil and x.left.maximum >= i[0]:
                    x = x.left
                else:
                    x = x.right
            if x == self.nil:
                return None
            else:
                return x 
        
        elif mode == 'fully_contained': # IF PRESENT, RETURN A POINTER TO AN INTERVAL FULLY CONTAINED IN THE GIVEN INTERVAL, ELSE RETURN NONE
            x = self.root    
            while x != self.nil:
                if not self._isnt_overlapping(i,x):
                    if i[0] >= x.interval['low'] and i[1]<=x.interval['high']:
                        return x
                    elif x.left != self.nil and x.left.maximum >= i[0]:
                        x = x.left
                    else:
                        x = x.right
                elif x.left != self.nil and x.left.maximum >= i[0]:
                    x = x.left
                else:
                    x = x.right
            return None 
            
                                                        
    # Under the hood...
    
    def _update_maximum_bottom_top(self,new_node):
        if new_node == self.root:
            new_node.maximum = max([new_node.interval['high'], new_node.left.maximum, new_node.right.maximum])
            return
        new_node.maximum = max([new_node.interval['high'], new_node.left.maximum, new_node.right.maximum])
        self._update_maximum_bottom_top(new_node.p)
    
    def _isnt_overlapping(self,i,x):
        return not (i[0]<= x.interval['high'] and x.interval['low'] <=i[1])
                 
    def _print(self):
        temp_level = [self.root]
        i = 1
        while i <= self.height:
            temp = copy.deepcopy(temp_level)
            print(' '*int(math.pow(2,self.height-i)-1),end=' ')
            first = temp_level.pop(0)
            if not first.interval['low'] and first.interval['low'] != 0:
                print('*',end='')
            else:
                print(str(first.interval['low'])+'-'+str(first.interval['high']),end='')
            j=0
            while j < math.pow(2,self.height-1-(self.height-i))-1:
                print(' '*int(math.pow(2,self.height+1-i)-1),end='')
                x = temp_level.pop(0)
                if not x.interval['low']:
                    print('*',end='')
                else:
                    print(str(x.interval['low'])+'-'+str(x.interval['high']),end='')
                j+=1
            print(' '*int(math.pow(2,self.height-i)-1),end='')
            for node in temp:
                temp_level.append(node.left)
                temp_level.append(node.right)
            i+=1
            print('\n')
        return
    def _update_height(self):
        self.height = math.ceil(2*math.log(self.n_nodes + 1,2))
        if self.height > 6:
            self.height = 6 # is difficult to visualize trees with a max_height > 6
    def _Get_Node(self,interval):
        x = self.root
        while x.interval['low'] != interval[0]:
            if x == self.nil:
                return None
            if interval[0] > x.interval['low']:
                x = x.right
            elif interval[0] < x.interval['low']:
                x = x.left
        if x.interval['high'] != interval[1]:
            if x.right.interval['low'] == interval[0] and x.right.interval['high'] == interval[1]:
                return x.right
            else:
                m = self._check_leftmost(x.right,interval)
                return m
        return x
    def _check_leftmost(self,x,interval):
        x = x.left
        while x.interval['low'] == interval[0]:
            if x.interval['high'] == interval[1]:
                return x
            x = x.left
        return None
    def _Left_Rotate(self,x):
        if x == self.nil:    # Maybe...
            return
        y = x.right
        x.right = y.left
        if y.left is not self.nil:
            y.left.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y
        y.maximum = x.maximum
        x.maximum = max([x.interval['high'], x.left.maximum, x.right.maximum])
        
    def _Right_Rotate(self,x):
        if x == self.nil:   # Maybe...
            return
        y = x.left
        x.left = y.right
        if y.right is not self.nil:
            y.right.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y
        y.maximum = x.maximum
        x.maximum = max([x.interval['high'], x.left.maximum, x.right.maximum])
        
    
    def _RB_INSERT(self,z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.interval['low'] < x.interval['low']:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.nil:
            self.root = z
        elif z.interval['low'] < y.interval['low']:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = R
        self._RB_INSERT_FIXUP(z)

    def _RB_INSERT_FIXUP(self,z):
        while z.p.color == R:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == R:
                    z.p.color = B
                    y.color = B
                    z.p.p.color = R
                    z = z.p.p
                else:
                    if z == z.p.right:    
                        z = z.p
                        self._Left_Rotate(z)
                    z.p.color = B         
                    z.p.p.color = R
                    self._Right_Rotate(z.p.p)

            # Symmetrically...

            else:
                
                y = z.p.p.left
                if y.color == R:          
                    z.p.color = B
                    y.color = B
                    z.p.p.color = R
                    z = z.p.p
                else:
                    if z == z.p.left:     
                        z = z.p
                        self._Right_Rotate(z)
                    z.p.color = B         
                    z.p.p.color = R
                    self._Left_Rotate(z.p.p)
        self.root.color = B
    
    def _RB_Transplant(self,u,v):  
        if u.p == self.nil:         #1
            self.root = v           #2
        elif u == u.p.left:      #3
            u.p.left = v         #4
        else:                   
            u.p.right = v        #5
        v.p = u.p                #6

    def _Tree_Minimum(self,z):
        while z.left != self.nil:
            z = z.left
        return z

    def _RB_Delete(self,z):
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self._RB_Transplant(z,z.right)
        elif z.right == self.nil:
            x = z.left
            self._RB_Transplant(z,z.left)
        else:
            y = self._Tree_Minimum(z.right) ##
            y_original_color = y.color
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self._RB_Transplant(y,y.right)
                y.right = z.right
                y.right.p = y
            self._RB_Transplant(z,y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
                
        if y_original_color == B:
            self._RB_DELETE_FIXUP(x)
            
    def _RB_DELETE_FIXUP(self,x):
        while x!=self.root and x.color == B:
            if x == x.p.left:
                w = x.p.right
                if w.color == R:
                    w.color = B
                    x.p.color = R
                    self._Left_Rotate(x.p)
                    w = x.p.right
                if w.left.color == B and w.right.color == B:
                    w.color = R
                    x = x.p
                else:
                    if w.right.color == B:
                        w.left.color = B
                        w.color = R
                        self._Right_Rotate(w)
                        w = x.p.right
                    w.color = x.p.color
                    x.p.color = B
                    w.right.color = B
                    self._Left_Rotate(x.p)
                    x = self.root
        # Symmetrically...
            else:
                w = x.p.left
                if w.color == R:
                    w.color = B
                    x.p.color = R
                    self._Right_Rotate(x.p)
                    w = x.p.left
                if w.right.color == B and w.left.color == B:
                    w.color = R
                    x = x.p
                else:
                    if w.left.color == B:
                        w.right.color = B
                        w.color = R
                        self._Left_Rotate(w)
                        w = x.p.left
                    w.color = x.p.color
                    x.p.color = B
                    w.left.color = B
                    self._Right_Rotate(x.p)
                    x = self.root
        x.color = B


  
fin = open('milk2.in', 'r')
fout = open('milk2.out', 'w')
N = int(fin.readline().strip())
times = []
for _ in range(N):
	times.append(list(map(int,fin.readline().strip().split())))
times = sorted(times, key = lambda x : x[0])

t = RedBlack_Int_Tree()
for i in times:
	if t.interval_search(i,mode = 'fully_contained'):
		continue
	else:
	    x = t.interval_search(i)
	    if x:
	        t.insert([min(i[0],x.interval['low']),max(i[1],x.interval['high'])])
	        t.delete([x.interval['low'],x.interval['high']])
	    else:
	        t.insert(i)
working_intervals = []
q = [t.root]
while q:
    tmp = q.pop(0)
    working_intervals.append([tmp.interval['low'],tmp.interval['high']])
    if tmp.left != t.nil:
        q.append(tmp.left)
    if tmp.right != t.nil:
        q.append(tmp.right)
not_working_intervals = []
working_intervals = sorted(working_intervals,key = lambda x : x[0])
for i in range(len(working_intervals)-1):
    not_working_intervals.append(working_intervals[i+1][0]-working_intervals[i][1])
working_intervals = [el[1]-el[0] for el in working_intervals]

a = max(working_intervals)
b = 0
if not_working_intervals:
	b = max(not_working_intervals)




fout.write('{} {}\n'.format(a,b))
fout.close()