def rand_list(max,min):      # function that can return shuffle a list
    import datetime
    now = datetime.datetime.now()
    list1 = []                             #big list
    list2 = []                             # refined list

    x = 0
    ctr = 0
    coeff = now.second
    mask = 0xff

    while (ctr <= 0xff ):
        nnn = now.microsecond        #external source of randomness
        k = coeff * x^3 + coeff * x^2 + x + nnn  #polynomial formula used to create random value

        k = k & mask                #casting / killing upper bytes

        list1.append(k)              # creating big list
        ctr = ctr + 1                # counter for while loop
        x = x + 1                    # x increment for polynomial

    ctr1 = 0
    while ( ctr1 < 256) :
        if list1[ctr1] <= max and list1[ctr1] >= min: #filtering the numbers i want from big list
            list2.append(list1[ctr1])                #and putting it into list 2
        ctr1 = ctr1 + 1

    return list2
def user():
    print("\nEnter 1 to start the Random sequence generator")
    inp = (input())
    if inp == "1":
        print("Enter Max value in sequence\n")
        maxy = int(input())
        print("\nEnter lowest value in sequence\n")
        lowy = int(input())
        print("\n")
        print(rand_list(maxy,lowy))
    elif inp is tuple:
        print("\nThen what are you here for! (ﾉꐦ ◎曲◎)ﾉ=͟͟͞͞ ⌨ ")

    else: print("\nThen what are you here for! (ﾉꐦ ◎曲◎)ﾉ=͟͟͞͞ ⌨ ")
    return ("Thank you by the way")

while 1 == 1:
    print(user())