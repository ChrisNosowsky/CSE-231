###########################################################
#  Computer Project #2
#  Created by: Chris Nosowsky
#
#    Progressive Tax System
#     Prompt for input
#     Print user's input
#     Calculates user's input into tax brackets for '17 and '18
#     Prints expected tax bill for '17 and '18
#     Prints tax bill difference between '17 and '18 and it's percent
###########################################################

income_str = input("Enter income as an integer with no commas: ") #Prompts user for input
income_int = int(income_str) #Input converted to integer

###2017 INCOME MAX FOR EACH RATE###
income_range_ten = 9325 #10% max income
income_range_fifteen = 37950 #15% max income
income_range_twentyfive = 91900 #25% max income
income_range_twentyeight = 191650 #28% max income
income_range_thirtythree = 416700 #33% max income
income_range_thirtyfive = 418400 #35% max income

###2017 TAX CALCULATIONS###
ten_percent_tax = income_range_ten*.10 #10% tax
fifteen_percent_tax = (37950-9325) * .15 #15% tax
twentyfive_percent_tax = (91900-37950)*.25 #25% tax
twentyeight_percent_tax = (191650-91900) * .28 #28% tax
thirtythree_percent_tax = (416700-191650) * .33 #33% tax
thirtyfive_percent_tax = (418400-416700) * .35 #35% tax
################################################################

###2018 INCOME MAX FOR EACH RATE###
income_2018_ten = 9525 #10% max income
income_2018_twelve = 38700 #12% max income
income_2018_twentytwo = 82500 #22% max income
income_2018_twentyfour = 157500 #24% max income
income_2018_thirtytwo = 200000 #32% max income
income_2018_thirtyfive = 500000 #35% max income

###2017 TAX CALCULATIONS###
ten_2018_tax = income_2018_ten*.10 #10% tax
twelve_2018_tax = (38700-9525) * .12 #12% tax
twentytwo_2018_tax = (82500-38700)*.22 #22% tax
twentyfour_2018_tax = (157500-82500) * .24 #24% tax
thirtytwo_2018_tax = (200000-157500) * .32 #32% tax
thirtyfive_2018_tax = (500000-200000) * .35 #35% tax


#TAX LOOP#
while income_int >= 0:
    #2017 TAX STATEMENT#
    if income_int <= income_range_ten: #10% RATE
        tax_2017 = income_int * .10
    elif income_int > income_range_ten and income_int <= income_range_fifteen: #15% RATE
        r_amount = income_int - income_range_ten
        tax_2017 = r_amount*.15 + ten_percent_tax
    elif income_int > income_range_fifteen and income_int <= income_range_twentyfive: #25% RATE
        r_amount = income_int - income_range_fifteen
        tax_2017 = r_amount*.25 + fifteen_percent_tax + ten_percent_tax
    elif income_int > income_range_twentyfive and income_int <= income_range_twentyeight: #28% RATE
        r_amount = income_int - income_range_twentyfive
        tax_2017 = r_amount*.28 + twentyfive_percent_tax + fifteen_percent_tax + ten_percent_tax
    elif income_int > income_range_twentyeight and income_int <= income_range_thirtythree: #33% RATE
        r_amount = income_int - income_range_twentyeight
        tax_2017 = r_amount*.33 + twentyeight_percent_tax + twentyfive_percent_tax + fifteen_percent_tax + ten_percent_tax
    elif income_int > income_range_thirtythree and income_int <= income_range_thirtyfive: #35% RATE
        r_amount = income_int - income_range_thirtythree
        tax_2017 = r_amount * .35 + thirtythree_percent_tax +twentyeight_percent_tax + twentyfive_percent_tax + fifteen_percent_tax + ten_percent_tax
    else: #39.6% RATE
        r_amount = income_int - income_range_thirtyfive
        tax_2017 = r_amount * .396 + thirtyfive_percent_tax + thirtythree_percent_tax +twentyeight_percent_tax + twentyfive_percent_tax + fifteen_percent_tax + ten_percent_tax
    #2018 TAX STATEMENT# 
    if income_int <= income_2018_ten: #10% RATE
        tax_2018 = income_int * .10
    elif income_int > income_2018_ten and income_int <= income_2018_twelve: #12% RATE
        r_amount = income_int - income_2018_ten
        tax_2018 = r_amount*.12 + ten_2018_tax
    elif income_int > income_2018_twelve and income_int <= income_2018_twentytwo: #22% RATE
        r_amount = income_int - income_2018_twelve
        tax_2018 = r_amount*.22 + twelve_2018_tax + ten_2018_tax
    elif income_int > income_2018_twentytwo and income_int <= income_2018_twentyfour: #24% RATE
        r_amount = income_int - income_2018_twentytwo
        tax_2018 = r_amount*.24 + twentytwo_2018_tax + twelve_2018_tax + ten_2018_tax
    elif income_int > income_2018_twentyfour and income_int <= income_2018_thirtytwo: #32% RATE
        r_amount = income_int - income_2018_twentyfour
        tax_2018 = r_amount*.32 + twentyfour_2018_tax + twentytwo_2018_tax + twelve_2018_tax + ten_2018_tax
    elif income_int > income_2018_thirtytwo and income_int <= income_2018_thirtyfive: #35% RATE
        r_amount = income_int - income_2018_thirtytwo
        tax_2018 = r_amount * .35 + thirtytwo_2018_tax +twentyfour_2018_tax + twentytwo_2018_tax + twelve_2018_tax + ten_2018_tax
    else: #37% RATE
        r_amount = income_int - income_2018_thirtyfive
        tax_2018 = r_amount * .37 + thirtyfive_2018_tax + thirtytwo_2018_tax +twentyfour_2018_tax + twentytwo_2018_tax + twelve_2018_tax + ten_2018_tax
    print("Income:" , income_int)
    print("2017 tax:" , round(tax_2017,2))
    print("2018 tax:" , round(tax_2018,2))
    print("Difference:" , round(tax_2018 - tax_2017,2))
    print("Difference (percent):", round(100-(tax_2018/tax_2017*100),2))
    income_str = input("Enter income as an integer with no commas: ")
    income_int = int(income_str)
