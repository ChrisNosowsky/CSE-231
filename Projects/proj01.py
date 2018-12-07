###########################################################
#  Computer Project #1
#  Created by: Chris Nosowsky
#
#    Arithmetic
#     Prompt for input
#     Print user's input
#     Converts user input into different units
#     Prints conversions rounded to three places
###########################################################

in_str = input("Input rods: ")                                #Prompts for user input
in_float = float(in_str)                                      #Converts input to float
print("You input", in_float, "rods.")                         #Prints user input in float

print("\nConversions")

in_meters = in_float*5.0292                                   #Converting from rods to meters
print("Meters:",round(in_meters,3))                           #Prints meters

in_feet = in_float*5.0292/0.3048                              #Converting from rods to feet
print("Feet:",round(in_feet,3))                               #Prints feet

in_miles = in_float*5.0292/1609.34                            #Converting from rods to miles
print("Miles:",round(in_miles,3))                             #Prints miles

in_furlongs = in_float/40                                     #Converting from rods to furlongs
print("Furlongs:", round(in_furlongs,3))                      #Prints furlongs

in_minutes = in_miles/3.1*60                                  #Converting from furlongs to minutes
print("Minutes to walk",in_float,"rods:",round(in_minutes,3)) #Prints minutes to walk
