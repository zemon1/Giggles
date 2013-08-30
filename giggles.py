#Jeff Haak
#Harlan Haskins
import random

popId = 0

def mate(pop):
     global popId
     
     if len(pop) == 0:
         pop.append([popId, 0, 0]) #Giggles
         popId += 1
     
     elif pop[0][1] > 4:
         return pop

     else:
         new = []

         for pup in pop:
             pup[1] += 1 #do they age before or after the loop??
             if pup[1] > 0 and pup[1] < 4:
                new.append([popId, 0, pup[0]])
                new.append([popId + 1, 0, pup[0]])
                popId += 2
             #pup[1] += 1 #do they age before or after the loop??
         pop.extend(new)
         
     mate(pop)
     return pop

if __name__ == "__main__":
     #random.seed(1)
     end = mate([])
     '''
     thresh = 30
     meet = []

     for pup in end:
          
          chance = random.randrange(1, 100)
          if (chance <= thresh) and not pup == end[0]:
               meet.append(pup)     
     '''

     print (len(end) - 1)*.3 
     print "\n----------------------------------\n"
     print end
