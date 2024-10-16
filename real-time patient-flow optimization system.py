import random
import time
from queue import Queue
import threading

# Simulating patient data
class Patient:
    def __init__(self, patient_id, severity):
        self.patient_id = patient_id
        self.severity = severity  # Severity levels: 1 (low), 2 (moderate), 3 (high)
        self.time_admitted = time.time()
        self.resources_needed = random.randint(1, 3)  # Resources required (e.g., 1 bed, 2 equipment, etc.)

class Hospital:
    def __init__(self, num_beds, num_doctors, num_equipment):
        self.num_beds = num_beds
        self.num_doctors = num_doctors
        self.num_equipment = num_equipment
        self.patients_queue = Queue()  # Queue to hold incoming patients
        self.patients_in_hospital = []

    def admit_patient(self, patient):
        if self.check_availability(patient):
            print(f"Admitting Patient {patient.patient_id} with severity {patient.severity}.")
            self.allocate_resources(patient)
            self.patients_in_hospital.append(patient)
        else:
            print(f"Patient {patient.patient_id} with severity {patient.severity} added to waitlist.")
            self.patients_queue.put(patient)

    def discharge_patient(self, patient):
        print(f"Discharging Patient {patient.patient_id}.")
        self.release_resources(patient)
        self.patients_in_hospital.remove(patient)

    def allocate_resources(self, patient):
        # Allocate hospital resources (e.g., bed, doctor, equipment)
        self.num_beds -= 1
        self.num_doctors -= 1
        self.num_equipment -= patient.resources_needed
        print(f"Allocated resources for Patient {patient.patient_id}. Beds left: {self.num_beds}, Doctors available: {self.num_doctors}")

    def release_resources(self, patient):
        # Release resources after patient discharge
        self.num_beds += 1
        self.num_doctors += 1
        self.num_equipment += patient.resources_needed
        print(f"Released resources for Patient {patient.patient_id}. Beds left: {self.num_beds}, Doctors available: {self.num_doctors}")

    def check_availability(self, patient):
        # Check if resources are available
        return self.num_beds > 0 and self.num_doctors > 0 and self.num_equipment >= patient.resources_needed

    def manage_waiting_list(self):
        # Check if resources are available and admit waiting patients
        while not self.patients_queue.empty() and self.check_availability(self.patients_queue.queue[0]):
            patient = self.patients_queue.get()
            self.admit_patient(patient)

    def simulate_discharge(self):
        # Randomly discharge patients after a certain time (for simulation purposes)
        if len(self.patients_in_hospital) > 0:
            patient = random.choice(self.patients_in_hospital)
            self.discharge_patient(patient)
            self.manage_waiting_list()

def simulate_patient_arrival(hospital):
    patient_id = 1
    while True:
        # Simulating the arrival of patients at random intervals
        severity = random.choice([1, 2, 3])
        patient = Patient(patient_id, severity)
        hospital.admit_patient(patient)
        patient_id += 1
        time.sleep(random.randint(2, 5))  # Patients arrive every 2-5 seconds

def simulate_discharge(hospital):
    while True:
        # Randomly discharging patients every 10 seconds
        time.sleep(10)
        hospital.simulate_discharge()

# Simulation parameters (for a small hospital)
num_beds = 5
num_doctors = 3
num_equipment = 10

hospital = Hospital(num_beds, num_doctors, num_equipment)

# Start simulating patient arrivals and discharges using threads
arrival_thread = threading.Thread(target=simulate_patient_arrival, args=(hospital,))
discharge_thread = threading.Thread(target=simulate_discharge, args=(hospital,))

arrival_thread.start()
discharge_thread.start()

arrival_thread.join()
discharge_thread.join()
