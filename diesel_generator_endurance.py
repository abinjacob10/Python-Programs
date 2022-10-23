"""Program calclulates remaining fuel Endurance = (Current fuel)/(Current Fuel consumption per minute) 
Program is written to highlight how erroneous input values could be handled in Python. """ 

#print(__doc__)



def func1(f: float ,fc: float)-> float:
#inside try block, first check if any of the entered numbers are negative, if negative, raise the exception and ask to enter positive numbers. Else, proceed to calculate the Endurance.
    try:
      if f < 0 or fc < 0:
        raise Exception("Please enter positive number")
      else:
        endurance=f/fc 
#handle error generated due to dividing by 0
    except ZeroDivisionError:
      print("Fuel consumption per minute is now 0")
#if no error seen from the inputs and calculation(f/fc), then return the endurance with 1 floating point value.
    else:
      return float("{:.1f}".format(endurance))
#  finally:
#    print("Good Day!!")



#Enter fuel and fuel consumption
#This try block checks if only numbers are entered not strings or other characters
try:
  f=float(input("Enter current available fuel in litre in decimal point:"))
  fc=float(input("Enter current fuel Consumption in litre per minute in decimal point:"))
  endur=func1(f,fc)
  #If returned value is not None(i.e. else from the function is, continue to print the endurance to user.
  if endur !=None:
    print("Remaining fuel endurance = {} minutes,".format(endur))
  #Else Show a message saying, 
  else:
    print("Current fuel = {:.1f} litre, endurance will depend on the consumption ".format(f))
  print("~~~~~Green Day!!~~~~~~")
#Catch the error when user enters non-numbers
except ValueError:
  print("Please enter numbers only!!")

