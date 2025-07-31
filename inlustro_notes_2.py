# # 1. Encapsulation - smart thermostat

# class SmartThermostat:
#     def __init__(self):
#         self.__current_temp = 22
#         self.__target_temp = 22

#     def set_target_temp(self, temp):
#         if 10 <= temp <= 30:
#             self.__target_temp = temp
#             self.__control_temp()
#         else:
#             print("Temperature out of range.")

#     def get_current_temp(self):
#         return self.__current_temp

#     def __control_temp(self):
#         if self.__current_temp < self.__target_temp:
#             print("Heater is ON")
#         elif self.__current_temp > self.__target_temp:
#             print("Cooler is ON")
#         else:
#             print("Temperature is favourable")

# thermostat = SmartThermostat()
# thermostat.set_target_temp(25)

# # 2. Abstraction - Travel booking site

# class MyTravelApp:
#     def search_flights(self, source, destination):
#         print(f"Searching flights from {source} to {destination}...")

#     def book_ticket(self, flight_id):
#         print(f"Booking ticket for flight ID: {flight_id}")

# app = MyTravelApp()
# app.search_flights("Kozhikode", "Dubai")
# app.book_ticket("KZH786")

# # 3. Inheritance - Hospital management system

# class Staff:
#     def __init__(self, name, staff_id, department):
#         self.name = name
#         self.staff_id = staff_id
#         self.department = department

# class Doctor(Staff):
#     def diagnose(self):
#         print(f"Dr. {self.name} is diagnosing patients.")

# class Nurse(Staff):
#     def assist_surgery(self):
#         print(f"Nurse {self.name} is assisting.")

# class Receptionist(Staff):
#     def schedule_appointments(self):
#         print(f"{self.name} is scheduling appointments.")

# doc = Doctor("Dilshad", 567, "Cardiology")
# nurse = Nurse("Alby", 568, "Surgery")
# receptionist = Receptionist("Charlie", 103, "Front Desk")

# doc.diagnose()
# nurse.assist_surgery()
# receptionist.schedule_appointments()

# # 4. Polymorphism - Notification system

# class Notification:
#     def send(self):
#         pass

# class EmailNotification(Notification):
#     def send(self):
#         print("Sending Email")

# class SMSNotification(Notification):
#     def send(self):
#         print("Sending SMS")

# class PushNotification(Notification):
#     def send(self):
#         print("Sending Push")

# notifications = [EmailNotification(), SMSNotification(), PushNotification()]
# for n in notifications:
#     n.send()

# # AGAIN ---------------------------------------------------------------------------------------

# # 1. Encapsulation - Smart thermostat system

# class SmartThermostat:
#     def __init__(self, current_temp, target_temp):
#         self.__currentTemp = current_temp
#         self.__targetTemp = target_temp
#     def setter(self, new_target):
#         if 15 < new_target < 30:
#             self.__targetTemp = new_target
#         else:
#             print('target temperature out of range -(15 < temp < 30)')
#     def getter(self):
#         return self.__targetTemp

# st1 = SmartThermostat(33, 20)
# print(f'Target temp: {st1.getter()}')
# st1.setter(25)
# print(f'Target temp: {st1.getter()}')

# # ------------------------------------------------------------------------------------------------------ #

# # Thread: smallest unit of execution in an operating system, not a program by itself, but runs within a program.
# # allow programs to execute sequential actions or many actions concurrently.

# # 2 modules: 1. thread module -> used for low-level threading       2. threading module ->

# from threading import Thread
# def my_func():
#     print(f'The thread name is Thread 1')
# def my_func1():
#     print('Hi hi hi')
# t1 = Thread(target = my_func1)
# t2 = Thread(target = my_func)
# t1.start()
# t1.join()
# t2.start()

# from threading import Thread
# def my_func(name):
#     print(f'The name is {name}')
# t1 = Thread(target=my_func, args=('Godson',)).start()
# t2 = Thread(target=my_func, args=('Razi',)).start()

# import threading, time
# def download():
#     print('Downloading...')
#     time.sleep(2)
#     print('Done!')
# threading.Thread(target=download).start()

# # print the thread name
# from threading import Thread
# import threading
# def show_name():
#     print("Running in", threading.current_thread())
# threading.Thread(target=show_name).start()

# import threading
# messages = []
# def say_hello(num):
#     messages.append(f'Hello from Thread-{num}')
# n = 5
# threads = []
# for i in range(1, n + 1):
#     t = threading.Thread(target=say_hello, args=(i, ))
#     t.start()
#     threads.append(t)
# for t in threads:
#     t.join()
# print(messages)

# from threading import Thread
# count = 0
# def increase():
#     global count
#     for i in range(1000):
#         count += 1
# threads = []
# for i in range(5):
#     t = Thread(target=increase)
#     t.start()
#     threads.append(t)
#     for t in threads:
#         t.join()

# print('Final counter value', count)
