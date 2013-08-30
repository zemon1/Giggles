#Jeff Haak
#Harlan Haskins
import random

popId = 0

def mate(pop):
     global popId
     
     #print "Pop:", pop
     if len(pop) == 0:
         pop.append([popId, 0, 0]) #Giggles
         popId += 1
     
     elif pop[0][1] > 4:
         return pop

     else:
         new = []

         for ele in pop:
             #ele[1] += 1 #do they age before or after the loop??
             if ele[1] > 0 and ele[1] < 6:
                new.append([popId, 0, ele[0]])
                new.append([popId + 1, 0, ele[0]])
                popId += 2
             ele[1] += 1 #do they age before or after the loop??
         pop.extend(new)
         
     mate(pop)
     return pop

if __name__ == "__main__":
     random.seed(1)
     end = mate([])
     thresh = 30
     meet = []

     for pup in end:
          
          chance = random.randrange(1, 100)
          if (chance <= thresh) and not pup == end[0]:
               meet.append(pup)     
     
     print len(meet) 
     print meet
     print "\n----------------------------------\n"
     print end
