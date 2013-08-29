#Jeff Haak
#Harlan Haskins
import random

popId = 0

def mate(pop, count):
     global popId

     if count >= 5:
         return pop

     else:
         new = []

         if len(pop) == 0:
             pop.append(popId)
             pop.append(popId + 1)
             popId += 2
         else:
             for ele in pop:
                 new.append(popId)
                 new.append(popId + 1)
                 popId += 2
             pop.extend(new)
         mate(pop, count + 1)

if __name__ == "__main__":
    print mate([], 0)
