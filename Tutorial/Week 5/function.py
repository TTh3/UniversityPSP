def functionName(a,b):
    if a<b:
        return a
    return b

# proper
def get_smallest(num1,num2):
    smallest=num1
    if num2<smallest:
        smallest = num2
    return smallest
n1=5
n2=10

result = get_smallest(n1,n2)
print("Smallest is: ", result)