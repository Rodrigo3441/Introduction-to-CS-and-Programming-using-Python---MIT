## 6.100A PSet 1: Part C
## Name: Rodrigo SG
## Time Spent: around 30 minutes
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input('Enter the initial deposit: '))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
house_cost = 800000
down_payment = 0.25 * house_cost
months = 36
steps = 0

r = []
for i in range(0, 100000):
    r.append(i/100000)

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
if not initial_deposit >= down_payment - 100:
    while True:
        steps += 1
        position = len(r) // 2

        amount_saved = initial_deposit * (pow(1 + (r[position]/12), months))

        if down_payment - 100 < amount_saved < down_payment + 100:
            r = r[position]
            break
        elif amount_saved < down_payment:
            r = r[position:]
            if len(r) == 1:
                r = None
                break
        elif amount_saved > down_payment:
            r = r[:position]
        else:
            r = None
else:
    r = 0.0




print(f'Best saving rage: {r} [or very close to this number]')
print(f'Steps in bisection search: {steps} [or very close to this number]')