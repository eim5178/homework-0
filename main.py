def main(): 
  celsius_temperature = float(input("Enter the temperature in celsius: "))
  temperature = (celsius_temperature  * 9/5) + 32 
  print(celsius_temperature, "\N{degree sign} in celsius is equivalent to" , temperature, "\N{degree sign}  Fahrenheit." )
main()