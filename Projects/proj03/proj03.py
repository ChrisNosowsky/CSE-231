###########################################################
#  Computer Project #3
#  Created by: Chris Nosowsky
#
#    Currency Conversion
#     Prompt for inputs (org. currency + convert currency)
#     Prompts for how much you want to convert
#     Checks to see if there is a non-integer
#     If integer, goes to url and converts the currency into the desired currency
#     Prints conversion then asks if user wants to do another conversion. If not, exit code.
###########################################################

import urllib.request

org_str = input("What is the original currency? ").upper() #Original Currency Input
conv_str = input("What currency do you want to convert to? ").upper() #New Currency Input
amt_str = input("How much do you want to convert (int)? ") #Amount wished to convert
test = amt_str.find(".") #Searches for a decimal. Checks to see if float
cont_exit = "yes" #placeholder until user wants to leave loop
while cont_exit.lower() == "yes":
    if test < 0 and amt_str.isdigit(): #If no decimal found(-1) and string is a digit, execute
        amt_int = int(amt_str) 
        url = "https://finance.google.com/finance/converter?a={}&from={}&to={}".format(amt_int,org_str,conv_str)
        response = urllib.request.urlopen(url)
        result = str(response.read())
        index = result.find("span") #Finds the span tag in the HTMl code, where our converted currency is nested
        indexnew = index + 15 #Index at span + 15 = where the desired conversion value starts
        lastindex = result.find("</span>") #Find the end of the span tag
        value_str = result[indexnew:lastindex] #Slices the result and takes only the value and currency acronymn
        amount_str, currency_str = value_str.split(" ") #Splits the code whereever there is a whitespace
        amount_float = float(amount_str) #Converts the first split(our converted value) into float
        print(amt_int,org_str,"is",round(amount_float,2),currency_str) #Prints original value, original currency, new value, new currency
        ask_str = input("Do you want to convert another currency? ") #Prompts if user wants to convert again
        if ask_str.lower() == "no": #If user says no, then it stops the loop from executing
            cont_exit = "no"
        else: #If user wants to continue, then we ask the same thing again
            org_str = input("What is the original currency? ").upper()
            conv_str = input("What currency do you want to convert to? ").upper()
            amt_str = input("How much do you want to convert (int)? ")
            test = amt_str.find(".")
            continue
    else: #This executes if non-integer is entered
        print("The value you input must be an integer. Please try again.")
        amt_str = input("How much do you want to convert (int)? ")
        test = amt_str.find(".")
