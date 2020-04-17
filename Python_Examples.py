
# # Try, Except, Finally

# try:
#     print(x)
# except:
#     print("Error Occured")
# finally:
#     c = 2+3
#     print(c)

# #Value Validation

# def age(value):
#     assert value>0 , "please give"
#     print(value)
# inp = int(input("Enter no:"))
# age(inp)


# #Exception Info

# import sys

# a = [5,8,"d",9,7,0,4]

# for i in a:
#     try:
#         c = 2/i
#         print(c)
#     except:
#         print("Error",sys.exc_info()[0],"occured")


# # Exception 
# class Error(Exception):
#     pass
# class TooSmallError(Error):
#     pass
# class TooLargeError(Error):
#     pass
# num =10
# while True:
#     try:
#         ch = int(input("Number:"))
#         if ch < 10:
#             raise TooSmallError
#         elif ch > 10:
#             raise TooLargeError
#         break
#     except TooSmallError:
#         print("Entered small no")
#     except TooLargeError:
#         print("Entered large no")
# print("Entered actual value")    

# #Read Write

# f = open("/home/ennovasys/Jai/python/t.txt", "r+")
# # f.write("Entered Data")
# length = len(f.readlines())
# # str = f.read(5)
# # print(str)
# print(length)
# f.close()  

# #Class, Obj , fucnc 

# class Ex:
#     a = 10
#     b = 21
#     c = "sa"
#     d = 90
#     def add(self,x,y):
#         c = x+y+self.d
#         return c
        
# obj = Ex()
# print(obj.c)
# ans = obj.add(10,5)
# print(ans)

# # Constructor 

# class demo:
#     print("constructor:".upper())
#     def __init__(self,name,age):
#         self.age = age
#         self.name = name 
#     def display(self):
#         print("Name is :",self.name)
#         print("Age is :",self.age)
# obj = demo("Jai",23)
# obj.display()


# #Inheritance

# class Father:
#     f_name = "this.father"
#     f_age = 55
# class son(Father):
#     s_name = "this.son"
#     s_age = 23

# obj = son()

# print("The Fathers name is :", obj.f_name,",", obj.f_age)
# print("The son name is :", obj.s_name,",", obj.s_age)

# #Multi Threading & Naming

# import threading
# import time

# def thread1(x,st):

#     for i in range (x): 
#         time.sleep(st)
#         print(threading.current_thread().getName())
#         print("Thread 1 Started \n")

# def thread2(x1,st1):

#     for i in range (x1):
#         time.sleep(st1)
#         print(threading.current_thread().getName())
#         print("Thread 2 Started \n")

# t1 = threading.Thread(target = thread1, args = (5,1))
# t1.setName("Thread #1")
# t2 = threading.Thread(target = thread2, args = (3,1))
# t2.setName("Thread #2")
# t1.start()
# t2.start()


# #Thread checking (Alive or Dead)
# import threading
# import time

# def thread(i):
#     time.sleep(i)
#     return
# t1 = threading.Thread(target = thread, args = (60,), name = "Thread 1")
# t1.start()
# t2 =  threading.Thread(target = thread, args = (2,), name = "Thread 2")
# t2.start()

# for x in range(5): # To check thread for every 5 secs
#     time.sleep(x)
#     print("[",time.ctime(),t1.name,t1.is_alive(),"]")    
#     print("[",time.ctime(),t2.name,t2.is_alive(),"]")

# # Daemon Threading
  
# import threading
# import time
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

# def thread1():   
#     print("Thread 1 Started \n")
#     time.sleep(2)
#     print("Theread 1 Ended")
 
# def thread2():
#     print("Thread 2 Started")
#     print("Thread 2 Ended")
    
# t1 = threading.Thread(target = thread1, daemon = 'true')
# t1.start()
# t2 = threading.Thread(target = thread2)
# t2.start()
# t1.join() # To Get Deamon thread end point
# t2.join()
 

# Timer Threading

# import threading
# import time

# def demo():
#     print("Timer Started")
# t = threading.Timer(3,demo)
# t.start()
# time.sleep(2)  # Cancels the theread if thread not started before 2 seconds
# t.cancel() 
import sys
import time
class ex:
    def __init__(self, text, hour, min, sec):
        self.text = text
        self.hour = hour
        self.min = min
        self.sec = sec


    def l(self): 
        print("op :", self.text)
    # def __init__(self, text):
    #    self.text = text

    # def getvalue(self):
    #     return self.text
    def check(self):
        
        c= ":"
        while self.hour > -1:
            while self.min > -1:
                while self.sec > 0:
                    self.sec=self.sec-1
                    time.sleep(1)
                    sec1 = ('%02.f' % self.sec)  # format
                    min1 = ('%02.f' % self.min)
                    hour1 = ('%02.f' % self.hour)
                    sys.stdout.write('\r' + str(hour1) + c + str(min1) + c + str(sec1))
                    if str(hour1) == "00" and  str(min1) == "00" and str(sec1) == "07":
                        playsound.playsound('test.mp3', True)

                        print("Time up")

                self.min=self.min-1
                self.sec=60
            self.hour=self.hour-1
            self.min=59

        print('Countdown Complete.')
        
