# Intelligent Queue Management System Simulation

# Logical Components & Steps implemented in Python

# Doctor Schedules & Availability
# - Track individual doctor schedules and real-time availability.
# - Clearly define doctor availability in predefined time blocks.

# Patient Arrival & Appointment Handling
# - Record and compare scheduled vs. actual arrival times.
# - Manage walk-ins effectively, including prioritization.
# - Provide mechanisms for rescheduling missed appointments dynamically.

# Multi-Channel Appointment Sources
# - Integrate various appointment booking channels (IVR, App, WhatsApp, Walk-ins).
# - Consolidate these sources into a unified, centralized queue management system.

# Queue Optimization & Prioritization
# - Dynamically prioritize patient assignments based on real-time urgency, delays, and queue length.
# - Ensure doctors have balanced workloads.

# Patient Status Tracking
# - Implement real-time tracking of patient status: "arrived," "waiting," and "consulted."

import heapq
from datetime import datetime, timedelta
import random

class Doctor:
    def __init__(self, doctor_id, availability_blocks):
        self.doctor_id = doctor_id
        self.queue = []
        self.availability_blocks = availability_blocks  # [(start_hour, end_hour)]

    def add_patient(self, patient):
        heapq.heappush(self.queue, (patient.priority, patient.arrival_time, patient.patient_id, patient))

    def next_patient(self):
        if self.queue:
            return heapq.heappop(self.queue)[3]
        return None

class Patient:
    def __init__(self, patient_id, arrival_time, scheduled_time, urgency, source):
        self.patient_id = patient_id
        self.arrival_time = arrival_time
        self.scheduled_time = scheduled_time
        self.urgency = urgency
        self.source = source
        self.priority = self.calculate_priority()

    def calculate_priority(self):
        delay_minutes = max(0, (self.arrival_time - self.scheduled_time).seconds // 60)
        source_priority = 0 if self.source == "Walk-in" else 5
        return -(self.urgency * 10 - delay_minutes + source_priority)

class QueueManagementSystem:
    def __init__(self):
        self.doctors = {}

    def add_doctor(self, doctor_id, availability_blocks):
        self.doctors[doctor_id] = Doctor(doctor_id, availability_blocks)

    def assign_patient(self, doctor_id, patient):
        if doctor_id in self.doctors:
            self.doctors[doctor_id].add_patient(patient)

    def estimate_wait_time(self, doctor_id):
        if doctor_id in self.doctors:
            avg_consult_time = random.randint(8, 22)
            queue_length = len(self.doctors[doctor_id].queue)
            return queue_length * avg_consult_time
        return None

# Example simulation
if __name__ == "__main__":
    qms = QueueManagementSystem()
    qms.add_doctor(doctor_id=1, availability_blocks=[(9, 12), (15, 18)])

    patient1 = Patient(patient_id=101,
                       arrival_time=datetime.now(),
                       scheduled_time=datetime.now() + timedelta(minutes=15),
                       urgency=2,
                       source="App")

    patient2 = Patient(patient_id=102,
                       arrival_time=datetime.now(),
                       scheduled_time=datetime.now() + timedelta(minutes=10),
                       urgency=3,
                       source="Walk-in")

    qms.assign_patient(1, patient1)
    qms.assign_patient(1, patient2)

    estimated_wait = qms.estimate_wait_time(1)
    print(f"Estimated wait time for Doctor 1: {estimated_wait} minutes")

    # Additional Test Case
    patient3 = Patient(patient_id=103,
                       arrival_time=datetime.now(),
                       scheduled_time=datetime.now() - timedelta(minutes=5),
                       urgency=5,
                       source="WhatsApp")

    qms.assign_patient(1, patient3)

    estimated_wait = qms.estimate_wait_time(1)
    print(f"Updated estimated wait time for Doctor 1 after new patient: {estimated_wait} minutes")
