# create a class PatientRecord to store patient's information
class PatientRecord:
    # initialize the class with patient's information
    def __init__(self, name, age, date_of_latest_admission, medical_history):
        self.name = name
        self.age = age
        self.date_of_latest_admission = date_of_latest_admission

    # method to get all the information of the patient
    def get_all_info(self):
        return f"Name: {self.name}\nAge: {self.age}\nDate of latest admission: {self.date_of_latest_admission}\nMedical history: {self.medical_history}"

# test the class   
patient1 = PatientRecord("Jack", '33', "2025-04-08", "Hypertension, asthma, COVID-19")
print(patient1.get_all_info())