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

#function to reverse list elements
def listReverse(list):
    revList = list;
    revList.reverse();
    return revList;


#main code
list = [];
i = 0;
element = None;

#Input the list
print("Enter 5 integers for the list");
while i < 5:
    list.append(int(input()));
    i += 1;

#Print out the results
print("List is:");
print(list);
print("Sum of elements is: " + str(listAdd(list)));
print("Product of elements is: " + str(listProd(list)));
print("The list reversed:");
print(listReverse(list));

#just adding some commentary at the bottom for Part 10
print("Making final additions...");