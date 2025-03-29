# Intelligent Queue Management System Simulation (Assessment #2)

## Problem Breakdown
- **Doctor Schedules & Availability:**  
  Tracks doctor availability in predefined time blocks, managing real-time schedules effectively.

- **Patient Arrival & Appointment Handling:**  
  Handles scheduled, walk-in, and missed appointments dynamically, prioritizing urgent cases effectively.

- **Multi-Channel Appointment Sources:**  
  Centralizes bookings from various channels (IVR, App, WhatsApp, Walk-ins) into one unified system.

- **Queue Optimization & Prioritization:**  
  Dynamically assigns patients based on urgency, arrival time, and doctor availability, balancing workloads.

- **Patient Status Tracking:**  
  Clearly tracks patient states (Arrived, Waiting, Consulted) in real-time.

## Required Information for Intelligent Queuing
- Doctor availability schedules and consultation durations.
- Real-time patient arrival data and historical appointment trends.
- Booking data from different channels (App, IVR, WhatsApp).
- Specific doctor preferences for handling walk-ins and appointment types.

## Measuring System Effectiveness
- **Average Wait Time Reduction:** Measures improvements by comparing before-and-after average wait times.
- **Queue Efficiency Score:** Evaluates the number of patients each doctor effectively consults per shift.
- **Patient Satisfaction Surveys:** Regularly collects feedback via SMS/App notifications.
- **No-show and Walk-in Handling:** Monitors effectiveness at managing unexpected arrivals and missed appointments.

## Patient Communication Strategy
- **Real-time Notifications:** Sends patients SMS/App updates about their estimated wait times.
- **Automated Rescheduling:** Offers alternate appointment times automatically if waits exceed thresholds.
- **Check-in Confirmation:** Alerts patients through automatic notifications when their doctor is ready.

## Implementation
- See [`queue_system_simulation.py`](queue_system_simulation.py) for the Python simulation demonstrating patient prioritization and queue management.

### Note:
- The simulation currently uses randomized consultation durations to reflect realistic scenarios. Modify these durations if predictable wait-time demonstrations are desired.
