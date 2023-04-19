'''
return the multiplication tables from 1 to 9.
'''
for i in range(1, 10):
    mt = [i*j for j in range(1, 13)]
    print(mt)