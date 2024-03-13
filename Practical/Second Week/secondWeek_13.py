#
# File: secondWeek_13.py
# Author: Jaylord
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Practical 2, Excercise 13
# This is my own work as defined by the University's
# Academic Misconduct policy.
#
num_buy_shares = int(input('Enter the number of shares: '))
price_buy_share= int(input('Enter price per share: '))
number_sell_shares = int(input('Enter the number of shares to sell: '))
price_sold_share= int(input('Enter price per selling shares: '))

total_buy_price = num_buy_shares*price_buy_share
total_sell_price = number_sell_shares*price_sold_share
print("The amount of money Joe paid for the stick is", total_buy_price)
print("The amount of commission Joe paid his broker when he bought the stock is", total_buy_price*0.03)
print("The amount that Joe sold the stock for is", total_sell_price)
print("The amount of commission Joe paid his broker when he bought the stock is", total_sell_price*0.03)
print("The amount of money that Joe had left when he sold the stock and paid his broker is", total_buy_price-total_sell_price)