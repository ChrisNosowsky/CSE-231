###########################################################
#  Computer Project 06
#  Created by: Chris Nosowsky
#
#    Chromosomes
#     Opens a GFF File from a genome database
#     Reads file and returns a gene list
#     Extracts chromosome user wants information on
#     Computes chromosome length mean and standard deviation
#     Displays computation in a chart that's easily readable to user
###########################################################
import math

CHROMOSOMES = ['chri','chrii','chriii','chriv','chrv','chrx'] #Constant list

def open_file():
    '''Opens the file entered for reading. Returns an error if the file is not found.'''
    test = True #Placeholder.
    while test == True: #Keeps looping until the file is found.
        try:
            prompt = input("Input a file name: ")
            op_file = open(prompt, "r")
            test = False
        except FileNotFoundError:
            print("Unable to open file.")
            continue
    return op_file
            
def read_file(fp):
    '''If file is opened, it will read the file. It will search for the genes
    and return these genes found in a list'''
    a_list = []
    for line in fp:
        if "chr" in line: #I did this to find only the lines with chromosome info, ignoring all other lines
            chromosome = line.split("\t")
            my_tuple = chromosome[0],int(chromosome[3]),int(chromosome[4]) #Taking columns 0, 3, and 4 only
            a_list.append(my_tuple)
    return a_list #genes_list
def extract_chromosome(genes_list, chromosome):
    '''Takes the gene list from the read file and the chromosome entered by user
    as parameters. Uses these parameters to extract the chromosome the user entered.'''
    chrom_gene_list = []
    for tup in genes_list: #Searches every tuple stored in genes_list
        if tup[0] == chromosome: #If the column 0(chromosome names) is equal to the chromosome the user entered.
            chrom_gene_list.append(tup)
    return sorted(chrom_gene_list)      
def extract_genome(genes_list):
    '''Takes the gene list and sorts the chromosomes into a list based on chromosome type.'''
    chrom_gene_lists = []
    for chromosome in CHROMOSOMES:  
        gene = extract_chromosome(genes_list, chromosome)
        chrom_gene_lists.append(gene)
    return chrom_gene_lists
    
def compute_gene_length(chrom_gene_list):
    '''Computes the gene that the user wants to find information about.
    Returns the genes mean and standard deviation.'''
    gene_lens = []
    sum_genes = 0
    for gene in chrom_gene_list: #Calculate every gene length and store it in a list
        gene_len = gene[2] - gene[1] + 1
        gene_lens.append(gene_len)
    gene_mean = sum(gene_lens)/len(gene_lens)
    gene_number = len(gene_lens)
    for gene in gene_lens: #This is the sum loop that will later be used for the standard deviation equation.
        sum_genes += math.pow((gene-gene_mean),2)
    gene_stddev = math.sqrt(sum_genes/gene_number) #Standard deviation equation
    return gene_mean, gene_stddev #Returns the gene mean and standard deviation
 
def display_data(gene_list, chrom):
    '''Displays the gene the user wants into a readable chart.
    Calls the compute_gene_length to calculate mean and standard deviation'''
    values = compute_gene_length(gene_list)
    print("{:<11s}{:9.2f}{:9.2f}".format(chrom,values[0],values[1]))
    
def main():
    print("Gene length computation for C. elegans.\n")
    fp = open_file() #Open file call
    rf = read_file(fp) #Read file call
    chrom_prompt = input("\nEnter chromosome or 'all' or 'quit': ")
    test = True #Placeholder. Will change when we want to break out of the while loop below.
    while test == True:
        for c in CHROMOSOMES: #Searches the chromosomes to see if the user's entered chromosome is found.
            if chrom_prompt.lower() == c: #If chromosome found, display the chart with the chromosomes mean and std. dev.
                chro = chrom_prompt[:3].lower() #Slicing to lower case "chr"
                numeral = chrom_prompt[3:].upper() #Slicing to upper case the roman numeral
                chrom = chro + numeral #Add the slices together
                print("\nChromosome Length")
                print("{:<11s}{:>9s}{:>9s}".format("chromosome","mean","std-dev"))
                display_data(extract_chromosome(rf,chrom_prompt.lower()),chrom)
                break
            elif chrom_prompt.lower() == "quit": #If user enters quit, break out of loop
                test = False
                break
            elif chrom_prompt.lower() == "all": #If user wants all chromosomes, print them all!
                print("\nChromosome Length")
                print("{:<11s}{:>9s}{:>9s}".format("chromosome","mean","std-dev"))
                for c in CHROMOSOMES: #Every chromosome, display them all.
                    chro = c[:3].lower()
                    numeral = c[3:].upper()
                    chrom = chro + numeral
                    display_data(extract_chromosome(rf,c),chrom)
                break
            else:
                continue
        else: #If chromosome isn't found.
            print("Error in chromosome.  Please try again.")
            chrom_prompt = input("\nEnter chromosome or 'all' or 'quit': ")
            continue
        if chrom_prompt.lower() != "quit": #If the user never wanted to quit, try again.
            chrom_prompt = input("\nEnter chromosome or 'all' or 'quit': ")  
if __name__ == "__main__":
    main()
