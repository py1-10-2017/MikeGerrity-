class Call(object): 
    def __init__(self, id, name, ptn, call_time, call_reason):
        self.id = id
        self.name = name
        self.ptn = ptn
        self.call_time = call_time
        self.call_reason = call_reason

    def displayinfo(self): 
        info = {
            "Call ID: ": self.id,
            "Name: ": self.name,
            "Phone Number: ": self.ptn,
            "Call Time: ": self.call_time,
            "Reason for Call: ": self.call_reason
        }
        return info

class Center(object): 
    def __init__(self):
        self.calls = []
        self.que = 0
    
    def incoming(self, id, name, ptn, call_time, call_reason):
        call = Call(id, name, ptn, call_time, call_reason)
        self.calls.append(call)
        return self.calls

    # def delete_call(self): 
    #     self.calls.pop[0]

    def call_info(self):
        for call in self.calls:
            info = call.displayinfo()
            call_key = info.keys()
            call_info = info.values()
            print call_key[4], call_info[4]
            print call_key[2], call_info[2]    

        call_count = 0

        for call in self.calls:
            call_count += 1
        print "Currently, there are {} calls in que".format(call_count)

callcenter = Center()
callcenter.incoming(1, "Bill", "443-555-1212", "20:30", "Tech Support")
callcenter.incoming(2, "Willy", "570-288-1212", "20:40", "Payment")
callcenter.incoming(3, "Francis", "717-333-1212", "20:50", "Collections")
#callcenter.delete_call()
callcenter.call_info()
    
    
    