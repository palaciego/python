def fizz_buzz(): 
    count=0
    for numero in range (1,102):
        
        if numero % 3==0 and numero%5==0:
            print ("fizz" + "buzz")
        elif numero %3 ==0:
            print("fizz")
        elif numero %5==0:
            print("buzz")
        else: print(count)
        count+=1

fizz_buzz()


