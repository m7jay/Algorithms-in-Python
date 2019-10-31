#a program to calculate the value of Pi based on the Leibniz formula
#pi = 4/1 - 4/3 + 4/5 - 4/7 + .....

def Calculate_Pi(sequence_length:int)->float:
    """
    calculates the value of Pi for 2*sequence_length of sequence size
    params:
    sequence_length     the half size of the sequnce from which the pi should be calculated
    """
    denominator = 1
    pi:float = 0
    for _  in range(sequence_length):
        pi += (4/denominator - 4/(denominator + 2))
        denominator += 4
    return pi

if __name__ == "__main__":
    print(Calculate_Pi(100000000000000))



