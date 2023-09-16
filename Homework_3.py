#function to find sum of the elements of a list
def listAdd(list):
    sum = 0;
    for i in range(len(list)):
        sum = sum + list[i];
    return sum;

#function to find product of the elements of a list
def listProd(list):
    prod = 1;
    for i in range(len(list)):
        prod *= list[i];
    return prod;