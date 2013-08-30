#Jeff Haak
#Harlan Haskins
import random

popId = 0

def mate(pop):
     global popId
     
     if len(pop) == 0:
         pop.append([popId, 0]) #Giggles
         popId += 1
     
     elif pop[0][1] > 4:
         return pop

     else:
         new = []

         for ele in pop:
             if ele[1] > 0 and ele[1] < 6:
                new.append([popId, 0])
                new.append([popId + 1, 0])
                popId += 2
             ele[1] += 1
         pop.extend(new)
         
     mate(pop)
     return pop

if __name__ == "__main__":
    end = mate([])
    print end
