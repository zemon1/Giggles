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
             pup[1] += 1 
             if pup[1] > 0 and pup[1] < 4:
                new.append([popId, 0, pup[0]])
                new.append([popId + 1, 0, pup[0]])
                popId += 2
             
         pop.extend(new)
         
     mate(pop)
     return pop

if __name__ == "__main__":
     end = mate([])
     
     ages = []

     for i in range(0, end[0][1] + 1):
         ages.append([])

     for pup in end:
         ages[pup[1]].append(pup)

     
     for i in range(0, end[0][1] + 1):
         print "Age group:", i
         print len(ages[i])
         print "\n-------------"
     

     print (len(end) - 1)*.3 
     print "\n----------------------------------\n"
     print end
