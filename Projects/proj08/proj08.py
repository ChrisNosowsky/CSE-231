###########################################################
#  Computer Project 08
#  Created by: Chris Nosowsky
#
#    Pollution Data
#     Prompts to open a file. In this case, pollution_small.csv. Reads it.
#     Prompts for what state and year
#     Runs through what user requests and displays it in a nice chart
#     Plots data if the user wants too.
#     Keeps asking for years to find until user wants to stop(quit)
###########################################################

#import csv
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
            
def read_file(fp):
    '''
    Reads through all the records and displays in this format: {State: [city,date,NO2mean,O3Mean,SO2Mean,COMean]}
    '''
    fp.readline()
    all_records = {}
    all_values = []
    MI_records = []
    ME_records = []
    MI_records_final = []
    ME_records_final = []
    DUPLICATES = []
    for line in fp:
        
        all_values = line.strip().split(",")
        if '\"' in line:
            if all_values[30] == '' or all_values[15]== '' or all_values[25] == '' or all_values[20] =='':
                continue
            else:
                ME_records.append([all_values[9],all_values[10],float(all_values[12]),float(all_values[17])*1000,float(all_values[22]),float(all_values[27])*1000])
        elif all_values[28] == '' or all_values[13]== '' or all_values[23] == '' or all_values[18] =='':
            continue
        else:
            MI_records.append([all_values[7],all_values[8],float(all_values[10]),float(all_values[15])*1000,float(all_values[20]),float(all_values[25])*1000])   

    for i in range(len(MI_records)-1):
        t = i+1
        if MI_records[i][1] not in DUPLICATES and (MI_records[i][0] == MI_records[t][0] and MI_records[i][1] == MI_records[t][1]):
            MI_records_final.append(MI_records[i])
            DUPLICATES.append(MI_records[i][1])
        elif MI_records[i][1] in DUPLICATES and (MI_records[i][0] == MI_records[t][0] and MI_records[i][1] == MI_records[t][1]):
            continue   
        else:
            MI_records_final.append(MI_records[i])
       #####Last Test####     
        if (t==len(MI_records)-1) and MI_records[t][1] not in DUPLICATES:
            MI_records_final.append(MI_records[t])
    for i in range(len(ME_records)-1):
        t = i+1
        if ME_records[i][1] not in DUPLICATES and (ME_records[i][0] == ME_records[t][0] and ME_records[i][1] == ME_records[t][1]):
            ME_records_final.append(ME_records[i])
            DUPLICATES.append(ME_records[i][1])
        elif ME_records[i][1] in DUPLICATES and (ME_records[i][0] == ME_records[t][0] and ME_records[i][1] == ME_records[t][1]):
            continue   
        else:
            ME_records_final.append(ME_records[i])
        if (t==len(ME_records)-1) and ME_records[t][1] not in DUPLICATES:
            ME_records_final.append(ME_records[t])
    all_records.update({"Michigan":MI_records_final})
    all_records.update({"Maine":ME_records_final})
    return all_records
        

def total_years(D, state):
    '''
    Prints total years and the pollution accumulated that year in total for the state the user wants to search for
    '''
    NO2 = 0
    O3 = 0
    SO2 = 0
    CO2 = 0
    if state.lower() == "michigan":
        max_val = 0
        min_val = 100000000
        total = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        for l in D["Michigan"]:
            for k in range(17):
                NO2 = 0
                O3 = 0
                SO2 = 0
                CO2 = 0
                year = 2000+k
                year_str = str(year)
                if year_str in l[1]:
                    NO2 += float(l[2])
                    O3 += float(l[3])
                    SO2 += float(l[4])
                    CO2 += float(l[5])
                    total[0+k][0] += NO2
                    total[0+k][1] += O3
                    total[0+k][2] += SO2
                    total[0+k][3] += CO2
            
        for i in range(len(total)):
            for t in range(len(total[0])):
                if total[i][t] > max_val:
                    max_val = total[i][t]
                elif total[i][t] < min_val:
                    min_val = total[i][t]
                else:
                    continue
    if state.lower() == "maine":
        max_val = 0
        min_val = 100000000
        total = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        for l in D["Maine"]:
            for k in range(17):
                NO2 = 0
                O3 = 0
                SO2 = 0
                CO2 = 0
                year = 2000+k
                year_str = str(year)
                if year_str in l[1]:
                    NO2 += float(l[2])
                    O3 += float(l[3])
                    SO2 += float(l[4])
                    CO2 += float(l[5])
                    total[0+k][0] += NO2
                    total[0+k][1] += O3
                    total[0+k][2] += SO2
                    total[0+k][3] += CO2
            
        for i in range(len(total)):
            for t in range(len(total[0])):
                if total[i][t] > max_val:
                    max_val = total[i][t]
                elif total[i][t] < min_val:
                    min_val = total[i][t]
                else:
                    continue    
    total = (total, max_val, min_val)    
    return total
            

def cities(D, state, year):
    city_dict = {}
    year_str = str(year)
    NO2 = 0
    O3 = 0
    SO2 = 0
    CO2 = 0
    i = 0
    if state.lower() == "michigan":
        for l in D["Michigan"]:
            if year_str in l[1]:
                NO2 += float(l[2])
                O3 += float(l[3])
                SO2 += float(l[4])
                CO2 += float(l[5])
                key = l[0]
                if key in city_dict or i == 0:
                    city_dict.update({l[0]:[NO2,O3,SO2,CO2]})
                elif key in city_dict and i > 0:
                    city_dict.update({l[0]:[NO2,O3,SO2,CO2]})
                else:
                    NO2 = 0
                    O3 = 0
                    SO2 = 0
                    CO2 = 0 
                    NO2 += float(l[2])
                    O3 += float(l[3])
                    SO2 += float(l[4])
                    CO2 += float(l[5])
                    city_dict.update({l[0]:[NO2,O3,SO2,CO2]})
                i+=1
    return city_dict    

def months(D,state,year):
    '''
    Calculates top pollution months of the desired year
    '''
    year_str = str(year)
    NO2_avgs_month = [0,0,0,0,0,0,0,0,0,0,0,0]
    O3_avgs_month = [0,0,0,0,0,0,0,0,0,0,0,0]
    SO2_avgs_month = [0,0,0,0,0,0,0,0,0,0,0,0]
    CO_avgs_month = [0,0,0,0,0,0,0,0,0,0,0,0]
    NO2_top5 = []
    O3_top5 = []
    SO2_top5 = []
    CO_top5 = []
    full_list = []
    if state.lower() == "michigan":
        for l in D["Michigan"]:
            month, day, year1 = l[1].split("/")
            if year_str == year1:
                for k in range(12):
                    
                    if k == 0:
                        continue
                    elif str(k) == month:
                        NO2_avgs_month[k-1]+=float(l[2])
                        O3_avgs_month[k-1]+=float(l[3])
                        SO2_avgs_month[k-1]+=float(l[4])
                        CO_avgs_month[k-1]+=float(l[5])
        NO2_avgs_month_so = sorted(NO2_avgs_month, reverse =True)
        O3_avgs_month_so = sorted(O3_avgs_month,reverse =True)
        SO2_avgs_month_so = sorted(SO2_avgs_month,reverse =True)
        CO_avgs_month_so = sorted(CO_avgs_month,reverse =True)
        for i in range(5):
            NO2_top5.append(NO2_avgs_month_so[i])
            O3_top5.append(O3_avgs_month_so[i])
            SO2_top5.append(SO2_avgs_month_so[i])
            CO_top5.append(CO_avgs_month_so[i])
        full_list = (NO2_top5, O3_top5,SO2_top5,CO_top5)
    return full_list
            
def display(totals_list,maxval,minval,D_cities,top_months):
    '''
    Displays all values in a nice chart
    '''
    print("\nMax and Min pollution")
    print("\n{:>10s}{:>10s}".format("Minval","Maxval"))
    print("{:>10.2f}{:>10.2f}".format(minval,maxval))
    i = 0
    year = 0
    print("\nPollution totals by year")
    print("\n{:<6s}{:>8s} {:>8s} {:>8s} {:>10s}".format("Year","NO2","O3","SO2","CO"))
    for t in totals_list[0]:
        if totals_list[0][i][0] == 0.00:
            break
        else:
            year = 2000 + i
            print("{:<6d}{:>8.2f} {:>8.2f} {:>8.2f} {:>10.2f}".format(year,totals_list[0][i][0],totals_list[0][i][1],totals_list[0][i][2],totals_list[0][i][3]))
            i+=1
    print("\nPollution by city")
    print("\n{:<16s}{:>8s} {:>8s} {:>8s} {:>8s}".format("City","NO2","O3","SO2","CO"))
    for key, value in D_cities.items():
        print("{:<16s}{:>8.2f} {:>8.2f} {:>8.2f} {:>8.2f}".format(key,value[0],value[1],value[2],value[3]))
        
    print("\nTop Months")
    print("\n{:>8s} {:>8s} {:>8s} {:>8s}".format("NO2","O3","SO2","CO"))
    for i in range(5):
        print("{:>8.2f} {:>8.2f} {:>8.2f} {:>8.2f}".format(top_months[0][i],top_months[1][i],top_months[2][i],top_months[3][i]))
        
def plot_years(totals_list,maxval,minval):
    no2 = []
    so2 = []
    o3 = []
    co = []
    years = []

    for i in range(2000,2017):
        years.append(i)

    for i in totals_list:
        no2.append(i[0])
        o3.append(i[1])
        so2.append(i[2])
        co.append(i[3])

    fig, ax = pylab.subplots()
    pylab.ylabel('Average Concentration')
    pylab.xlabel('Year')
    pylab.title('Total Average Pollution Per Year')
    ax.plot(years,no2, 'ro')
    ax.plot(years,o3, 'bo')
    ax.plot(years,so2, 'go')
    ax.plot(years,co, 'yo')
    ax.plot(years,no2, 'ro', label='NO2')
    ax.plot(years,o3, 'bo', label='O3')
    ax.plot(years,so2, 'go', label='SO2')
    ax.plot(years,co, 'yo', label='CO')


    ax.legend(loc='upper right', shadow=True, fontsize='small')

    pylab.show()

def main():
    fp = open_file()
    data = read_file(fp)
    t = 0
    p = 0
    years = ""
    city = ""
    month = ""
    a = True
    while t == 0 or p == 0 or a == True:
        t = 0
        p = 0
        state = input("Enter a state ('quit' to quit): ")
        if state.lower() == "quit":
            a = False
            break
        for d in data:
            if state.lower() == d.lower():
                t = 1
                years = total_years(data, state)
            else:
                continue
        if t == 0:
            print("Invalid state.")
        else:
            year = input("Enter a year ('quit' to quit): ")
            if year.lower() == "quit":
                a = False
                break
            else:
                p = 1
                year_int = int(year)
                city = cities(data,state,year_int)
                month = months(data,state,year_int)
                display(years,years[1],years[2],city,month)
                ask = input("Do you want to plot (yes/no)? ")
                if ask.lower() == "yes":
                    plot_years(years,years[1],years[2])
                else:
                    continue
  
if __name__ == "__main__":
    main()          
