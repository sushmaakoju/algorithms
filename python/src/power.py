def recursive_power(x,y):
    print(x,y)
    if y == 0:
        return 1
    temp = recursive_power(x, int(y/2)) 
    if int(y % 2) == 0 :
        return (temp * temp)
    else:
        return (x* temp * temp)

def rec_power(x,y):
    print(x,y)
    if y == 0:
        return 1
    elif int(y % 2) == 0 :
        return (rec_power(x, int(y/2))  * rec_power(x, int(y/2)) )
    else:
        return (x* rec_power(x, int(y/2))  * rec_power(x, int(y/2)) )

print("O(log(n))")
print(recursive_power(2,3))
print(recursive_power(2,5))
print("O(n)")
print(rec_power(2,5))
