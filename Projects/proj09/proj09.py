###########################################################
#  Computer Project 09
#  Created by: Chris Nosowsky
#
#    Decrypting Text
#     Prompts to open a file. In this case, english_quadgrams.txt Reads it.
#     Prompts for either to attack or give analysis
#     Based on what user requests, runs through code and decrypts a text that the user entered in plain and ciphered text
###########################################################


from math import log10
import string
from operator import itemgetter

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


def chosen_plaintext_attack(plaintext, ciphertext, bifurcation, texttodecrypt):
    text_dict = {}
    new = []
    i = 0
    decryptedtext = ""
    ciphertext = ciphertext.strip(string.punctuation) #ciphertext being stripped from any punctuation
    for ch in range(len(ciphertext)): #every character in the the range of cipher text
        if ciphertext[-bifurcation:] in new: #If the last loop of bifurcation is in the new list, then break from loop to avoid out of bounds
            break
        else:
            new.append(ciphertext[ch*bifurcation:bifurcation*(ch+1)])
    for ch in plaintext: #every character in plaintext
        if i < len(new): #this is to update the dictionary
            text_dict.update({new[i]:ch})
            i += 1
    for ch in range(len(text_dict)):
        try:
            char = texttodecrypt[ch*bifurcation:bifurcation*(ch+1)]
            decryptedtext += text_dict[char]
        except KeyError: #key error thrown if the key is not found
            return print( "Decryption interrupted. Key not found: {}".format(texttodecrypt[ch*bifurcation:bifurcation*(ch+1)]))
   
    return decryptedtext

def log_probability_dictionary(fp):
    so = []
    quads_final ={}
    quads = {}
    total = 0
    new = []
    for line in fp:
        line = line.strip().split()
        so.append(line)
    for i in range(len(so)): #this grabs the total amount of frequency
        total += int(so[i][1])
    for i in range(len(so)):
        value = int(so[i][1])
        prob = log10(value/total) #log probability
        new.append([so[i][0],value,prob])
    ordered = sorted(new, key=itemgetter(2), reverse=True) #sorts by the log
    ordered_alpha = sorted(new, key =itemgetter(0)) #sorts by the name
    print("\n{:<8s}{:>13s}{:>22s}".format('Quadgram','Count','Log Probability'))
    print("-------------------------------------------") 
    for e in range(len(ordered_alpha)):
        quads.update({ordered_alpha[e][0]:[ordered_alpha[e][1],ordered_alpha[e][2]]})
    for i in range(10):
        quads_final.update({ordered[i][0]:[ordered[i][1],ordered[i][2]]})
    for key, value in quads_final.items():
        print("{:<8s}{:>13d}{:>22.6f}".format(key,value[0],value[1]))         
    return quads
def bruteforce_shift_cipher(ciphertext, ngrams_dictionary):
    print("{:<5s}{:^35s}   {:>10s}".format("\nKey", "Plaintext", "Fitness")) 
    print("------------------------------------------------------") 
    ciphertext_upper = ciphertext.upper() #upper cases the ciphertext
    alphabet = list(string.ascii_uppercase)
    rot = {}
    k = []
    for i in range(26):
        v = 26 - i
        temp = 26 - (26-i)
        for a in range(v):  
            k.append(alphabet[a+i])
        for t in range(temp):
            k.append(alphabet[t])
    for i in range(26):
        if i == 0:
            rot.update({i:k[0:26]})
        else:
            rot.update({i:k[i*26:(i+1)*26]})
    print(rot)
    #"\npress any key to continue..."
    #"\nDecrypted ciphertext: "
def fitness_calculator(potential_plaintext, quadgram_dictionary):
    endpt = 4 #since we are taking every 4, this is the starting enpoint
    start = 0
    quads_all = []
    total = 0
    while True:
        if endpt <= len(potential_plaintext):
           quad = potential_plaintext[start:endpt]
           start += 1
           endpt +=1
           quads_all.append(quad)
        else:
            break
    for key,val in quadgram_dictionary.items():
        if key in quads_all:
            total += val[1]
        else:
            continue
    return total       
           
        

def main():
    '''
    fp = open_file()
    #fitbit = fitness_calculator("PYTHON", quadgram)
    quadgram = log_probability_dictionary(fp)
    bruteforce = bruteforce_shift_cipher("0C0D0E", quadgram)
    '''
    BANNER = """\
    ------------------------------------------------------------------------
    Welcome to the world of code breaking. This program is meant to help
    decipher encrypted ciphertext in absence of knowledge of algorithm/key.
    ------------------------------------------------------------------------
    """
    MENU = """\
    1. Chosen plaintext attack
    2. Ngram frequency analysis
    """
    print(BANNER)
    print(MENU)
    c = input("Choice: ")
    if c == "1":
        pt = input("Plaintext: ")
        ct = input("Ciphertext: ")
        bi = input("Bifurcation: ")
        bi_int = int(bi)
        td = input("Text to decrypt: ")
        attacc = chosen_plaintext_attack(pt,ct,bi_int,td)
    elif c == "2":
        fp = open_file()
        quadgram = log_probability_dictionary(fp)
        
    else:
        print("Invalid input.")
  
if __name__ == "__main__":
    main()
           
