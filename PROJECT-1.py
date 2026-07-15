print(f"Welcome to the Interactive Personal Data Collector !\n")

a=str(input("Please Enter Your Name :- "))
b=int(input("Please Enter Your Age :- "))
c=float(input("Please Enter Your Height in meters :- "))
d=int(input("Please Enter Your Favourite Number :- "))

print(f"\nThank you!, \nHere is the information we collected :- ")

print(f"\nName :- ",a)
print("Type :- ",type(a))
print("Memory Address :- ",id(a))
print("------------------------------------------------------------------------")

print(f"\nAge :- ",b)
print("Type :- ",type(b))
print("Memory Address :- ",id(b))
print("------------------------------------------------------------------------")

print(f"\nHeight :- ",c)
print("Type :- ",type(c))
print("Memory Address :- ",id(c))
print("------------------------------------------------------------------------")

print(f"\nFavourite Number :- ",d)
print("Type :- ",type(d))
print("Memory Address :- ",id(d))
print("------------------------------------------------------------------------")

print(f"\nYour birth year is approximately :- ",2026-b," ( Based on your age of ",b,")")
print("------------------------------------------------------------------------")

print(f"\nThank you for using the Personal Data Collector, \nGoodbye!")
