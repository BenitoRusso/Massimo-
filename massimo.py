N = int(input("inserisci 1° numero = "))
M = N


i = 1

while i < 10:
   
   N = int(input("inserisci "+str(i+1)+"° numero = "))
   if N > M:
      M = N
   i +=1

print ("il numero massimo è "+str(M))