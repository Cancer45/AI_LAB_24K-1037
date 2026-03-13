import random

def mathsFunc(x):
    return (6*x) - (x*x)

def climbHill():
    x = random.randint(0, 6)
    curr = mathsFunc(x)

    print("x_init: ", x)
    while (True):
        tmp1 = mathsFunc(x + 1)
        tmp2 = mathsFunc(x - 1)

        if (tmp1 > tmp2):
            highest = tmp1
            tmp_x = x + 1
        else:
            highest = tmp2
            tmp_x = x - 1

        if (curr < highest):
            curr = highest
            x = tmp_x
            print("curr_f(x): ", curr)
        
        else: break
    print("optimal value: ", curr)

climbHill()


        


