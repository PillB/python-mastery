# pcost.py
def portfolio_cost(filename):
    with open(filename,'r') as f:
        price = 0
        for i,line in enumerate(f):
            try:
                price += float(line.split()[-1]) * float(line.split()[-2])
            except ValueError as e:
                print('In line:',line.split('\n')[0],':',e)
    print(price)
portfolio_cost('../Data/portfolio3.dat')