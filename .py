def ekok(sayı):
    tam_bölenler = []
    for i in sayı :
        for j in range(1, i+ 1) :
            if i % j == 0:
                if j not in tam_bölenler:
                    tam_bölenler.append(j)
    for i in tam_bölenler:
        tam_bölenler.remove(i)
        for j in tam_bölenler:
            if i % j == 0:
                tam_bölenler.remove(j)
        tam_bölenler.insert(-1, i)
    
   # a = 1
    #for i in tam_bölenler:
     #  a = i * a             
   
    
    
                #for ii in tam_bölenler:
                 #   if j % ii == 0:
                  #      if ii not in tam_bölenler : 
                   #         tam_bölenler.append(j)
        #if count == 0:
            #tam_bölenler.append(i)
     
    return tam_bölenler

print(ekok([5,7,9,8,10]))