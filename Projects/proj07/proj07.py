###########################################################
#  Computer Project 07
#  Created by: Chris Nosowsky
#
#    Medicaid Spending
#     Prompts to open a file. In this case, medicaid_spending.csv. Reads it.
#     Creates a tuple of data that includes: year, medication name, total spending covered, prescriptions, etc.
#     Uses that data and displays it in a nice chart for easy reading.
#     Plots data if the user wants too.
#     Keeps asking for mediaid data by year until user wants to terminate.
###########################################################




from operator import itemgetter
import pylab

def open_file():
    '''
    Opens file for reading. If file is not found, it throws an error. Returns the file pointer.
    '''
    while True:
        try:
            ask = input("Input a file name: ")
            fp = open(ask, "r")
            break #If file is opened, then we break out of this
        except FileNotFoundError: #If file not found
            print("Unable to open the file. Please try again.")
    return fp

def read_data(fp):
    '''
    Takes in filepointer and skips first line. All other lines are data that will be extracted and put into a list of tuples that contain data.
    returns this list sorted by name and year.
    '''
    fp.readline() #Read over first line
    medic_data = []
    tup_data = []
    avg_presc = 0
    avg_unit = 0
    for line in fp:
        medic_data = line.strip().split(",") #Gets rid of whitespace and the commas that seperate each category
        if medic_data[3] != "n/a": #If the value is avaliable to us
            avg_unit = float(medic_data[3])/int(medic_data[5])
            avg_presc = float(medic_data[3])/int(medic_data[4])
            tup_data.append((int(medic_data[0]),medic_data[1],float(medic_data[3]),int(medic_data[4]),int(medic_data[5]),avg_presc,avg_unit))
    return sorted(tup_data, key=itemgetter(0,1)) #Sorts by year and by brand alphabetically A-Z

def top_ten_list(column, year_list):
    '''
    Takes the top ten of whatever column the user requests. Returns the top 10 of this column, along with the medication brands.
    '''
    num = column -1 #Subtract 1 to deal with index
    so_yr = sorted(year_list, key=itemgetter(num), reverse=True) #Takes the year_list and sorts by the requested column, reversed(largest to smallest)
    i = 0
    list1 = []
    list2 = []
    for medication in so_yr:
        if i < 10: #Increments through i until it reaches 10, then stops to return the top 10.
            list1.append(so_yr[i][1])
            list2.append(so_yr[i][num])
            i+=1
            
    return list1, list2
        
    
def get_year_list(year, data):
    '''
    Takes in a year and the data from read_data function and creates a list of tuples for that specified year only. Returns the list of tuples.
    '''
    year_tup = []
    i = 0
    for medication in data:
        if data[i][0] == year: #This searches in the year list and in the tuple elements in the list, and checks to see if the year matches the year we want to return
            year_tup.append((data[i]))
            i += 1
        else:
            i += 1
    return year_tup
def display_table(year, year_list):
    '''
    Formats the year list from get_year_list and puts it in a easily readable chart.
    '''
    so_yr = sorted(year_list, key=itemgetter(0)) #Sorts by brand name, A-Z
    print("{:^80s}".format("Drug spending by Medicaid in " + str(year)))
    print("{:<35s}{:>15s}{:>20s}{:>15s}".format("Medication","Prescriptions","Prescription Cost","Total"))
    for medication in so_yr:
        print("{:<35s}{:>15,d}{:>20,.2f}{:>15,.2f}".format(medication[1],medication[3],medication[5],medication[2]/1000))

def plot_top_ten(x, y, title, xlabel, ylabel):
    '''
        This function plots the top 10 values from a list of medications.
        This function is provided to the students.
        
        Input:
            x (list) -> labels for the x-axis
            y (list) -> values for the y-axis
            title (string) -> Plot title
            xlabel (string) -> Label title for the x-axis
            ylabel (string) -> Label title for the y-axis
    '''
    pos = range(10)
    pylab.bar(pos, y)
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    pylab.xticks(pos,x, rotation='90')
    pylab.show()
    

def main():
    fp = open_file()
    print("Medicaid drug spending 2011 - 2015")
    data = read_data(fp) 
    test = True
    while test == True: #This will keep looping unless the user wants to terminate(q)
        test2 = True
        t = 0
        year1 = input("Enter a year to process ('q' to terminate): ")
        if year1.lower() != "q":
            while test2 == True: #This keeps looping until a valid year is entered
                try:
                    year = int(year1)
                    test2 = False
                except ValueError:
                    print("Invalid Year. Try Again!")
                    year1 = input("Enter a year to process ('q' to terminate): ")
            i = 0
            for medication in data:
                if data[i][0] == year: #If year is found in data
                    year_list = get_year_list(year,data)
                    t10_list_meds = top_ten_list(4,year_list)
                    t10_list_covered = top_ten_list(3,year_list)
                    display_table(year, year_list)
                    plot = input("Do you want to plot the top 10 values (yes/no)? ")
                    if plot.lower() == "yes": #If the user wants to plot
                        plot_top_ten(t10_list_meds[0],t10_list_meds[1],"Top 10 Medications prescribed in " + str(year),"Medication Name","Prescriptions" )
                        plot_top_ten(t10_list_covered[0],t10_list_covered[1],"Top 10 Medicaid Covered Medications in " + str(year),"Medication Name","Amount" )
                    t = 1
                    break #Breaks out of for loop so we don't keep looping if same year is found.
                else:
                    i += 1
            if t == 0: #This will only run if we can't find the year.
                print("Invalid Year. Try Again!")
        else:
            test = False

    pass
        
if __name__ == "__main__":
    main()
