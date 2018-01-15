# DECK FOR TEST
#KingSpades QueenSpades JackSpades 10Spades AceSpades KingDiamond QueenDiamond JackDiamond 10Diamond AceDiamond KingClubs QueenClubs JackClubs 10Clubs AceClubs    KingHearts QueenHearts JackHearts 10Hearts AceHearts Joker



def map(set, idx):   #function that uses second parameter as index for first parameter, and maps it back
    sety = []      #Used in line 54
    ctr = 0
    while ctr < len(set):
        a = idx[ctr]
        a = (int(a) - 1)
        sety.append(set[a])
        ctr += 1
    return sety
def rand_list(list):      # function that can return shuffle a list
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
        if list1[ctr1] <= len(list) and list1[ctr1]: #filtering the numbers i want from big list
            list2.append(list1[ctr1])                #and putting it into list 2
        ctr1 = ctr1 + 1

    return list2
def threerandpile(list): # function that divides 1 list into three different lists
    result_list = []
    list1 = []
    list2 = []
    list3 = []


    if len(list)%3 != 0: #error message, if wrong number of elements is in list
        import sys
        sys.exit("The number of elements in your list has to be divisible by three!")

    listy = rand_list(list) #random function called here to use as index below
    idx1 = 0
    idx2 = len(list) / 3
    idx2 = int(idx2)
    idx3 = len(list) * 2 / 3
    idx3 = int(idx3)

    listy = map(list,listy) #the random sequence is mapped as the index of the list
    ctr = 0
    maxI = idx2
    for ctr in range(0,maxI):
        list1.append(listy[idx1])
        list2.append(listy[idx2])
        list3.append(listy[idx3])
        idx1 += 1
        idx2 += 1
        idx3 += 1
        ctr += 1
    result_list.append(list1)
    result_list.append(list2)
    result_list.append(list3)
    return result_list

print("\n")
print("Enter list")
a = input().split()
print("\n")
print(threerandpile(a)[0])
print("\n")
print(threerandpile(a)[1])
print("\n")
print(threerandpile(a)[2])


