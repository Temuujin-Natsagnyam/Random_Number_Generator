import datetime
def rand_list(list):
    now = datetime.datetime.now()
    list1 = []                             #big list
    list2 = []                             # refined list

    x = 0
    ctr = 0
    coeff = now.second

    while (ctr <= 0xff ):
        nnn = now.microsecond        #external source of randomness
        k = coeff * x^3 + coeff * x^2 + x + nnn  #polynomial formula used to create random value

        k = k & 0xff                 #killing all the bigger bytes

        list1.append(k)              # creating big list
        ctr = ctr + 1                # counter for while loop
        x = x + 1                    # x increment for polynomial

    ctr1 = 0
    while ( ctr1 < 256) :
        if list1[ctr1] <= list and list1[ctr1] != 0 :                    #
            list2.append(list1[ctr1])       #filtering big list to make small list
        ctr1 = ctr1 + 1

    return list2
while 1:
    print(" Enter random sequence length")
    a = int(input())
    print(rand_list(a))
