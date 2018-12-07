###########################################################
#  Computer Project #5
#  Created by: Chris Nosowsky
#
#    Country Happiness Scores
#     Opens a file
#     Prompts for country or region search
#     Prompts for a specific keyword
#     Searches and prints results
###########################################################


def open_file(): #opens a file for reading
    file = False
    while file == False:
        try: #tests to see if it exists
            prompt = input("Input a file name: ")
            ofile = open(prompt, "r")
        except FileNotFoundError: #if file is not found
            print("Unable to open the file. Please try again.")
            continue
        file = True
    return ofile
    
def read_data(fp, input_str, search_str):
    hap_avg = []
    if input_str == "1": #if user inputted 1 for search by country
        total = 0
        for line in fp:
            count, reg, hap, ec, fam, hth, free, trst, gen = line.split(",")
            if count == "Country":
                print("{:24s}{:<32s}{:<17s}".format(count,reg,hap))
                print("-"*71) #To make it look pretty
            if hap != "Happiness Score":
                hap_flt = float(hap)
            if search_str in count.lower(): #If found in country category
                total+=1
                final = display_line(count, reg, hap_flt)
                print(final)
                hap_avg.append(hap_flt)
    else: #if user inputted 2 for search by region
        total = 0
        for line in fp:
            count, reg, hap, ec, fam, hth, free, trst, gen = line.split(",")
            if count == "Country":
                print("{:24s}{:<32s}{:<17s}".format(count,reg,hap))
                print("-"*71)
            if hap != "Happiness Score":
                hap_flt = float(hap)
            if search_str in reg.lower(): #If found in region category
                total+=1
                final = display_line(count, reg, hap_flt)
                print(final)
                hap_avg.append(hap_flt)
    hap_avg_sum = sum(hap_avg)/total
    print("-"*71)
    print("Average Happiness Score {:>36.2f}".format(hap_avg_sum))
        
def display_line(country_name, region_name, happiness_score):
    return "{:24s}{:<32s}{:<17.2f}".format(country_name, region_name, happiness_score)

def main():
    the_file = open_file()
    test = False
    num_input = input("Input 1 to search in country names, 2 to search in regions: ")
    while test == False: #Loop to test if correct number entered
        if num_input == "1" or  num_input == "2":
            test = True
        else:
            print("Invalid choice, please try again!")
            num_input = input("Input 1 to search in country names, 2 to search in regions: ")
    search_str = input("What do you want to search for? ")
    read_data(the_file,num_input,search_str)

if __name__ == '__main__':
   main()
