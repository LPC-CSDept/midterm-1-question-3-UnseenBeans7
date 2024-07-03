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
        # next number
        pnumber += 1
        for i in range(2, pnumber):
            if pnumber % i == 0:
                #has a factor, not prime
                break
        else:
            # has no factors (besides 1 and itself)
            pfound = True

    print(pnumber)

    ########################################
    # Do not delete the return statement
    ########################################
    return pnumber
##


if __name__ == '__main__':
    main()
