#후입선출의 스택구조 
class Stack():
    
    def __init__(self): #인스턴스가 생성될 때, 빈 리스트를 각 인스턴스 이름안에 넣는다.
        self.lst = []
    
    def empty(self): #셀프를 넣어야 하나?
        if self.lst == []:
            return True
        else:
            return False

    def top(self):
        if self.lst == []:
            return None
        else:
            return self.lst[-1]

    def pop(self):
        if self.lst == []:
            return None
        else:
            return self.lst.pop(len(self.lst)-1)

    def push(self, val):
        self.lst.append(val)
    
    def __repr__(self):
        return f'리스트는 현재{self.lst} 이렇게 존재합니다.'


#-------------------------

class Stack:
    def __init__(self): #data는 뭐지?
        self.data = []
    
    #스택이 비었다면 true, 그렇지 않다면 false 반환
    def empty(self):
        if self.data ==[]:
            return True
        return False

    #마지막 데이터 반환, 비었다면 none반환   
    def top(self):
        flag = self.empty()
        if flag == True:
            return None
        return self.data[-1]
        # return self.data[-1] if self.empty() is not True else None


       
        #마지막 데이터 반환, 해당 데이터 삭제  비었다면 none반환  
    def pop(self):
        flag = self.empty()
        if flag == True:
            return None
        else:
            return self.data.pop(len(self.data)-1)
    
    def push(self, val):
        self.data.append(val)
   
    def __repr__(self):
        return f'리스트는 현재{self.data} 이렇게 존재합니다.'


stack = Stack()
print(stack.empty())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.top())
print(stack)
stack.pop()
print(stack)

