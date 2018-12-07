###########################################################
#  Computer Project #4
#  Created by: Chris Nosowsky
#
#    Cipher Encryption and Decryption
#     Asks for rotations
#     Asks for string to rotate using cipher
#     Converts into cipher text if no errors
###########################################################

import math,string
PUNCTUATION = string.punctuation #Constant
ALPHA_NUM = string.ascii_lowercase + string.digits #Constant

def multiplicative_inverse(A,M):
    '''Return the multiplicative inverse for A given M.
       Find it by trying possibilities until one is found.'''
       
    for x in range(M):
        if (A*x)%M == 1:
            return x
  
def check_co_prime(num, M):
    '''Checks to see if there the number and alphabet count have a GCD of 1'''
    if math.gcd(num,M) == 1:
        return True
    else:
        return False
        
def get_smallest_co_prime(M):
    '''Checks for smallest co_prime in the alphabet count'''
    num = 2
    while num <= M:
        if check_co_prime(num,M) == True:
            return num
        else:
            num += 1
        
def caesar_cipher_encryption(ch,N,alphabet):
    '''caesar cipher encryption is used to cipher punctuation
    this function encrypts it'''
    m_num = len(alphabet)
    x_index = alphabet.find(ch)
    E_x = (x_index + N) % m_num #Formula
    E_x_ch = alphabet[E_x]
    return E_x_ch

def caesar_cipher_decryption(ch,N,alphabet):
    '''caesar cipher decryption is used to cipher punctuation
    this function decrypts it'''    
    m_num = len(alphabet)
    x_index = alphabet.find(ch)
    D_x = (x_index-N) % m_num #Formula
    D_x_ch = alphabet[D_x]
    return D_x_ch

def affine_cipher_encryption(ch,N,alphabet):
    '''affine cipher encryption is used to cipher the English alphabet and digits
    this function encrypts it'''  
    m_num = len(alphabet)
    A = get_smallest_co_prime(m_num)
    x_index = alphabet.find(ch)
    E_x = (A*x_index + N) % m_num #Formula
    E_x_ch = alphabet[E_x]
    return E_x_ch

def affine_cipher_decryption(ch,N,alphabet):
    '''affine cipher decryption is used to cipher the English alphabet and digits
    this function decrypts it''' 
    m_num = len(alphabet)
    A = get_smallest_co_prime(m_num)
    A_Inverse = multiplicative_inverse(A,m_num)
    x_index = alphabet.find(ch)
    D_x = A_Inverse*(x_index-N) % m_num #Formula
    D_x_ch = alphabet[D_x]
    return D_x_ch
    
def main():
    '''Main function. Prompts user for input. If any input is incorrect, it will give an error message.
    Function ends only when user enters command "q"'''
    test = True #placeholder
    while test == True:
        try:
            rot = input("Input a rotation (int): ")
            rot_int = int(rot)
            test = False #Changes to stop the while loop from executing
        except ValueError:
            print("Error; rotation must be an integer.") #Error message
            continue
    cmd = input("Input a command (e)ncrypt, (d)ecrypt, (q)uit: ")
    while cmd != "q": #While user doesn't want to quit.
        if cmd.lower() == "e": #If command "e"
            password = "" #placeholder
            bad_char = 0 #placeholder
            e_msg = input("Input a string to encrypt: ")
            e_msg_low = e_msg.lower()
            for char in e_msg_low: #Checks every character in the lowercase string the user wants to encrypt
                if char in ALPHA_NUM or char in PUNCTUATION: #If the character is in ALPHA_NUM or PUNCTUATION
                    if char in ALPHA_NUM: #If it's in ALPHA_NUM, run the affine cipher function
                        password += affine_cipher_encryption(char,rot_int,ALPHA_NUM)
                    elif char in PUNCTUATION: #If the character is in PUNCTUATION, run the caesar cipher function
                        password += caesar_cipher_encryption(char,rot_int,PUNCTUATION)
                    else: #If in neither, continue on
                        continue      
                else: #If not in either
                   bad_char += 1 #Test variable
                   bad_bad_char = char  #Character that errors       
            else: 
                if bad_char > 0: #If there is a bad character, print the error message
                    print("Error with character:{}".format(bad_bad_char))
                    print("Cannot encrypt this string.")
            if bad_char > 0: #If there is any bad characters, prompt for a command again
                cmd = input("Input a command (e)ncrypt, (d)ecrypt, (q)uit: ")
            else:  #If no bad characters, print the original text, ciphered text, and prompt for command
                print("Plain text: {}".format(e_msg))
                print("Cipher text: {}".format(password))
                cmd = input("Input a command (e)ncrypt, (d)ecrypt, (q)uit: ")
        elif cmd.lower() == "d": #If command "d"
            password = "" #placeholder
            bad_char = 0 #placeholder
            e_msg = input("Input a string to decrypt: ")
            e_msg_low = e_msg.lower()
            for char in e_msg_low:
                if char in ALPHA_NUM or char in PUNCTUATION:
                    if char in ALPHA_NUM:
                        password += affine_cipher_decryption(char,rot_int,ALPHA_NUM)
                    elif char in PUNCTUATION:
                        password += caesar_cipher_decryption(char,rot_int,PUNCTUATION)
                    else:
                        continue      
                else:
                   bad_char += 1
                   bad_bad_char = char         
            else: 
                if bad_char > 0:
                    print("Error with character:{}".format(bad_bad_char))
                    print("Cannot decrypt this string.")
            if bad_char > 0:
                cmd = input("Input a command (e)ncrypt, (d)ecrypt, (q)uit: ")
            else:
                print("Cipher text: {}".format(e_msg))
                print("Plain text: {}".format(password))

                cmd = input("Input a command (e)ncrypt, (d)ecrypt, (q)uit: ")
        else: #If "e", "d", or "q" are not entered
            print("Command not recognized.") #Error message
            cmd = input("Input a command (e)ncrypt, (d)ecrypt, (q)uit: ")
            
    
    
    
if __name__ == "__main__":
    main()
    
