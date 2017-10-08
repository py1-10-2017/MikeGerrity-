class MathDojo(object): 
    def __init__(self, value): 
        self.value = 0

    def add(self, *nums):
        for i in nums:
            if type(i) == list:
                for k in i:
                    self.value += k
            if type(i) == int: 
                self.value += i
            if type(i) == tuple: 
                for l in i:
                    self.value += l
        return self

    def sub(self, *nums):
        for i in nums:
            if type(i) == list:
                for k in i:
                    self.value -= k
            if type(i) == int: 
                self.value -= i
            if type(i) == tuple: 
                for l in i:
                    self.value -= l
        return self
    
    def result(self): 
        print "The result is " + str(self.value)
        return self



md1 = MathDojo(0) 
md1.add([1],3,4).add([3,5,7,8], [2,4.3,1.25]).sub(2,[2,3],[1.1,2.3]).result()
