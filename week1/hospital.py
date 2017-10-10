class Patient(object): 
    PA_COUNT = 0
    def __init__(self, name, allergies):
        self.name = name
        self.alergies = allergies
        self.bed_num = None
        self.id = Patient.PA_COUNT
        Patient.PA_COUNT += 1
    
class Hospital(object):
    def __init__(self, name, cap):
        self.name = name
        self.cap = cap
        self.patients = []
        self.beds = self.bed_count()
    
    def bed_count(self):
        beds = []
        for i in range(0, self.cap):
            beds.append({
                "bed_id": i,
                "Available": True
            })
        return beds
    
    def admit(self, patient):
        if len(self.patients) <= self.cap:
            self.patients.append(patient)
            for i in range(0, len(self.beds)):
                if self.beds[i]["Available"]:
                    patient.bed_num = self.beds[i]["bed_id"]
                    self.beds[i]["Available"] = False
                    break
            print "Patient #{} admitted to bed #{}".format(patient.id, patient.bed_num)
        else:
            print "Hospital is full"

    def discharge(self, patientid):
        for patient in self.patients:
            if patient.id == patientid:
                for bed in self.beds:
                    if bed["bed_id"] == patient.bed_num:
                        bed["Available"] = True
                        break
                self.patients.remove(patient)
                print "Patient #{} sucessfully discharged.  Bed #{} now available".format(patient.id, patient.bed_num)


h1 = Hospital("Upper Chesapeak", 20)
pa1 = Patient("Bill", "Peanut")
pa2 = Patient("Brad", "eggs")
pa3 = Patient("Wendy", "lactose")

h1.bed_count()
h1.admit(pa1)
h1.admit(pa2)
h1.admit(pa3)

h1.discharge(0)
