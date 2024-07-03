def main():

    number = int(input('Enter your number: '))
    """
    ########################################
    Code Your Program here
    ########################################
    """
    pnumber = number
    pfound = False
    
    while pfound == False:
        pnumber += 1
        for i in range(2, pnumber):
            if pnumber % i == 0:
                #has a multiple, not prime
                break
            else:
                #is a prime number
                pfound = True
                break

    print(pnumber)

    ########################################
    # Do not delete the return statement
    ########################################
    return pnumber
##


if __name__ == '__main__':
    main()
