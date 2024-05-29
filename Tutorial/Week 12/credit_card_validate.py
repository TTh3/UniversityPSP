# Credit card validation!

infile = open('credit_test.txt', 'r')

credit_card_list = []
for line in infile:
    new_line = line.strip()
    credit_card_list.append(new_line)

# print(credit_card_list)

def validate_card_number(credit_card, updated_card, total):
    for index in range(len(credit_card)):
        
        if index % 2 != 0:
            double_num = f'{int(credit_card[index])*2}'

            if int(double_num) > 9:
                num = int(double_num[0])+int(double_num[1])
                updated_card = f'{num}' + updated_card
            else:
                updated_card = f'{double_num}' + updated_card
                
        else:
            updated_card=f'{credit_card[index]}'+updated_card

    for i in updated_card:
        total+= int(i)

    if total % 10 == 0:
        print(f'{updated_card} {total} is valid!')
    else:
        print(f'{updated_card} {total} is not valid!')

for card in credit_card_list:
    updated_card = ""
    total = 0
    credit_card = card[::-1]
    validate_card_number(credit_card,updated_card,total)
    
        
    

