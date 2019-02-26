for i in range(3,40):
    find = True
    for j in range(1,280):
        if(5**j % 2**i == 1 and find == True):
            find = False
            print(2**i," has finished with ", j)
            
    
