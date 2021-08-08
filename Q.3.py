

# Aapke paas ek list hai.
# Iss list mein har string ko ek file-question3.
# txt naam ki file mein nayi line mein daalo. Aapki list yeh rahi:
 
banks_list = ["Kotak\n", "HDFC\n", "RBL\n", "SBI\n", "Bank of Baroda\n"] 
k=open("banks_list","w")
i=0
while i<len(banks_list):
    k.write(banks_list[i])
    i=i+1
k.close()


    


