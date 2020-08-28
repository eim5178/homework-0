def main(): 
  celsius_temperature = float(input("Enter temperature in celsius: "))
  temperature = (celsius_temperature  * 9/5) + 32 
  print(str(celsius_temperature) + "\N{degree sign} in Celsius is equivalent to " + str(temperature) + "\N{degree sign} Fahrenheit." )
main()