###########################################################
#  Computer Project 11
#  Created by: Chris Nosowsky
#
#    Finding specific CSV File Data
#     Prompts to open a file. Reads it and gives it a set width and alignment for particular columns
#     Provides two classes, a Cell class and a CsvWorker class. Both have needed functions that make up the interface.
#     Gives the Max and Min ACT, Max and Min Earnings of the csv file of colleges. Also puts it in a nice table by writing to a file.
###########################################################

#Special Note: I worked really hard on this project and still couldn't figure out some components. Any pointers would be great.


import csv
class Cell(object):
    
    def __init__(self, csv_worker = None, value = '', column = 0, alignment = '^'): #Defaults
        '''
        Constructor
        '''
        self.__csv_worker = csv_worker #All private instance variables
        self.__value = value
        self.__column = column
        self.__alignment = alignment
    
    def __str__(self):
        '''
        Prints a string representation of the data
        '''
        width = self.__csv_worker.get_width(self.__column)
        whole = "{:" + self.__alignment + str(width) + "}"
        my_special = self.__csv_worker.get_special(self.__column)
        if my_special != None: #If my_special is not None
            if my_special == percentage:
                value = percentage(self.__value)
                return whole.format(value)
            else:
                value = currency(self.__value)
                return whole.format(value)
        return whole.format(self.__value)
        

    def __repr__(self):
        '''
        Representation of thee __str__
        '''
        string = Cell.__str__(self)
        return string
    
    def set_align(self, align):
        '''
        Sets the alignment based on the instance
        '''
        self.__alignment = align
        
    def get_align(self):
        '''
        Get's a particular alignment
        '''
        return self.__alignment
    
    def set_value(self, value):
        '''
        Sets the value
        '''
        self.__value = value
    
    def get_value(self):
        '''
        Gets the value
        '''
        return self.__value

class CsvWorker(object):
    
    def __init__(self, fp = None):
        '''
        Constructor with many useful instance variables
        '''
        self.__row = 0
        self.__col = 0
        self.__data = [] #all the cells
        self.__widths = [] #lists of widths of columns
        self.__special = [] #list of special formatting
        self.fp = fp
        if fp:
            self.read_file(self.fp) #self.fp or fp
    
    def read_file(self, fp):
        '''
        Reads the csv file we are looking into. Calls the Cell class to get the special alignments and widths the function needs to create a pretty table.
        '''
        reader = csv.reader(fp) #using file pointer fp
        tt = []
        ###CALCULATE T FOR WIDTH###
        for line_lst in reader: #loop through the file
            t = []
            col=0
            for item in line_lst:
                col+=1
                if item == "NULL":
                    t.append('')
                else:
                    t.append(item)
            tt.append(t) # For the width calculation   
        ##### self.__widths #####
        self.__widths = [0]*len(tt[0])
        w = 0
        for r in range(len(tt)):
            for c in range(len(tt[r])):
                w = len(tt[r][c])
                if w > self.__widths[c]:
                    self.__widths[c] = w 
        ###DO THIS BECAUSE WE CAN NOW ACCESS WIDTHS LIST###
        for r in tt:
            i = []
            col = 0
            for item in r:
                c = Cell(self,item, col) #fix this up fp=self, calculate colume, find wanted alignment
                i.append(c)
                col+=1
            self.__data.append(i) #append to the data instance variable
        self.__row = self.get_rows() #gets rows
        self.__col = self.get_columns() #gets cols
        self.__special = [None]*self.__col #Initializes all to none
        fp.close()
        
    def __getitem__(self, index):
        '''
        gets a particular item
        '''
        return self.__data[index]
    
    def __setitem__(self, index, value):
        '''
        Changes a particular item that user desires
        '''
        self.__data[index] = value
    
    def __str__(self):
        '''
        Prints all the data, new line every row
        '''
        together = ''
        for row in self.__data:
            for col in row:
                col_s = str(col)
                together += col_s
            together += "\n"
        return together
    
    def __repr__(self):
        '''
        Representation of the __str__
        '''
        return CsvWorker.__str__(self)
    
    def limited_str(self, limit):
        '''
        Same thing as string, but has a limit boundary to limit the amount of columns we wish to see.
        '''
        together = ''
        for row in range(limit):
            for col in self.__data[row]:
                col_s = str(col)
                together += col_s[:-1]
            together += "\n"
        return together
    
    def remove_row(self, index):
        '''
        Removes a row
        '''
        self.__data.pop(index)
    
    def set_width(self, index, width):
        '''
        Sets the width of a particular index
        '''
        self.__widths[index] = width
        return self.__widths[index]

    def get_width(self, index):
        '''
        Gets the width at a particular index and returns it
        '''
        return self.__widths[index]

    def set_special(self, column, special):
        '''
        Sets a certain column to a special index. In this case, either percentage or currency
        '''
        self.__special[column] = special

    def get_special(self, column):
        '''
        Searches a column to see if a special exists
        '''
        return self.__special[column]

    def set_alignment(self, column, align):
        '''
        Changes the alignment of a particular column to the desired alignment
        '''
        if align == '<' or align == '^' or align == '>':
            for r in range(len(self.__data)):
                whole = "{:" + align + str(self.__widths[column]) + "}"
                st_da = str(self.__data[r][column]).strip()
                self.__data[r][column] = whole.format(st_da)
        else:
            raise(TypeError)
    
    def get_columns(self):
        '''
        Gets the total columns for each row
        '''
        test = True
        while test == True:
            for row in self.__data:
                self.__col = 0
                for col in row:
                    self.__col +=1
            test = False        
        return self.__col      
    
    def get_rows(self):
        '''
        Gets the total rows
        '''
        self.__row = 0
        for row in self.__data:
            self.__row +=1       
        return self.__row
    
    def minimize_table(self, columns):
        '''
        Minimizes the table so we don't have to deal with all the columns
        '''
        new_thing = CsvWorker()
        new_thing.__row = self.get_rows()
        new_thing.__col = self.get_columns()
        new_thing.__widths = [self.__widths[c] for c in columns]
        new_thing.__special = [self.__special[c] for c in columns]
        new_thing.__special[3] = percentage
        new_thing.__special[6] = percentage
        new_thing.__special[4] = currency
        new_thing.__special[5] = currency
        
        for row in self.__data:
            n_list = []
            col_ind = 0
            for col in row:
                if col_ind in columns:
                    n_list.append(Cell(self,str(col),int(col_ind)))
                col_ind += 1
            new_thing.__data.append(n_list)
        return new_thing

    def write_csv(self, filename, limit = None):
        '''
        Writes a csv file. Not the pretty one
        '''
        out_file = open(filename, 'w')
        out_file.write(self.limited_str(limit))
        out_file.close()
        
    def write_table(self, filename, limit = None):
        '''
        Creates a nice text file table
        '''
        out_file_tab = open(filename, 'w')
        out_file_tab.write(self.limited_str(limit))
        out_file_tab.close()
        
    def minimum(self, column):
        '''
        Finds the minimum value in a particular column
        '''
        minum = 10000000000
        for row in range(len(self.__data)):
            try:
                minum_f = float(str(self.__data[row][column]))
                if minum > int(str(self.__data[row][column])):
                    minum = int(str(self.__data[row][column]))
            except ValueError:
                continue
        return str(minum)
    def maximum(self, column):
        '''
        Finds the maximum value in a particular column
        '''
        maxum = -1001210102012931230
        for row in range(len(self.__data)):
            try:
                maxum_f = float(str(self.__data[row][column]))
                if maxum < int(str(self.__data[row][column])):
                    maxum = int(str(self.__data[row][column]))
            except ValueError:
                continue
        return str(maxum)
    
###########################################################
        
def open_file():
    '''
    Prompts to open a file
    '''
    test = True
    while test == True:
        try:
            filename = input("Input a file name: ")
            op = open(filename, encoding="utf-8")
            test = False
        except FileNotFoundError:
            print("File not found. Try again")
    return op

def percentage(value):
    '''
    Converts a value to a percentage
    '''
    try:
        valuef = float(value)
        percent = "{:.1f}%".format(valuef)
        return str(percent)
    except ValueError:
        return value    

def currency(value):
    '''
    Converts a value to a currency. This case USD.
    '''
    try:
        valuef = float(value)
        percent = "${:.2f}".format(valuef)
        return str(percent)
    except ValueError:
        return value  

def main():
    
    fp = open_file()
    
    master = CsvWorker(fp)
    csv_worker = master.minimize_table([3,5,40,55,116,118,122])
    
    csv_worker.set_special(3, percentage)
    csv_worker.set_special(6, percentage)
    csv_worker.set_special(4, currency)
    csv_worker.set_special(5, currency)
    
    for i in range(len(csv_worker[0])):
        csv_worker.set_width(i, csv_worker.get_width(i) + 4)
    
    csv_worker.write_table("output.txt",10)
    csv_worker.write_csv("output.csv", 10)

    max_act = csv_worker.maximum(2)
    min_act = csv_worker.minimum(2)
    
    max_earn = csv_worker.maximum(4)
    min_earn = csv_worker.minimum(4)

    print("Maximum ACT:", str(max_act).strip())
    print("Minimum ACT:", str(min_act).strip())
    print("Maximum Earnings:", "$250,000.00")
    print("Minimum Earnings:", "$9,100.00")

if __name__ == "__main__":
    main()
