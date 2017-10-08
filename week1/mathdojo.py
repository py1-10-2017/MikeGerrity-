class MathDojo(object): 
    def __init__(self, value): 
        self.value = 0

    def add(self, *nums):
        for i in range(len(nums)):
            x = nums[i]
            self.value = self.value + x
        return self

    def sub(self, *nums):
        for i in range(len(nums)):
            x = nums[i]
            self.value = self.value - x     
        return self
    
    def result(self): 
        print "The result is " + str(self.value)
        return self



md1 = MathDojo(0) 
md1.add([1],3,4).add([3,5,7,8], [2,4.3,1.25]).sub(2,[2,3],[1.1,2.3]).result()
