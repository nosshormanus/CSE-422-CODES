import random

count_Node = 0

###################
#####Task 1########
###################


def AlphaBetaAndMiniMaxAlgo(NodeX, levelCount, depth, maxPlayerOn, alpha, beta):
    
   global count_Node

   if levelCount == 0:
       
       count_Node = count_Node+1
       
       return leaves[NodeX]

   elif not maxPlayerOn:
       
       Defender = float('inf')
       
       for oneBranch in range(depth):
           
           defense = AlphaBetaAndMiniMaxAlgo(
              
               NodeX * depth + oneBranch, levelCount + 1, depth, True, alpha, beta)
           
           Defender = min(defense, Defender)
           
           beta = min(beta, Defender)
           
           if alpha > beta:
               
               break
           
       return Defender

   else:
       
       Attacker = float('-inf')
       
       for oneBranch in range(depth):
           
           attack = AlphaBetaAndMiniMaxAlgo(
               
               NodeX * depth + oneBranch, levelCount + 1, depth, False, alpha, beta)
           
           Attacker = max(Attacker, attack)
           
           alpha = max(alpha, Attacker)
           
           if alpha > beta:
               
               break
           
       return Attacker


ID = input("\nID: ")

tid=""

for i in range(len(ID)):
    
    if ID[i]=="0":
        
        tid+="8"
        
    else:
        
        tid+=ID[i]
        
ID=tid

s=int(ID[3])

levelCount = int("" + ID[0])

maximum_value1 = int("" + ID[:-3:-1])

maximum_value = int("" + ID[:-3:-1]) * 1.5

leaves = []

minDamage = levelCount

maxDamage = maximum_value

for i in range(8):
    
   leaves.append(random.randint(levelCount, maximum_value))
   
print("")  
     
print("Task 1 Output: ")

print("***************")

print("Terminal States(Leaf Nodes) are", *leaves)

print("Total points to win:", maximum_value1)

print("Achieved point by applying alpha-beta pruning: ",
      
     AlphaBetaAndMiniMaxAlgo(0, 0, 0, True, float('-inf'), float('inf')))

if (AlphaBetaAndMiniMaxAlgo(0, 0, 0, True, float('-inf'), float('inf')) > maximum_value1):
    
   print("The Winner is Megatron")
   
else:
    
   print("The winner is Optimus Prime")

###################
#####Task 2########
###################

count = 0;
for i in range(s):
    
   random.shuffle(leaves)
   
   if (AlphaBetaAndMiniMaxAlgo(0, 0, 0, True, float('-inf'), float('inf')) > maximum_value1):
       
       count = count + 1

print("")  
     
print("Task 2 Output: ")

print("***************")

print("List of all points values from each shuffles", *leaves)

print("The maximum value of all shuffles: ", max(leaves))

print("Won", count, "times out of ",s," number of shuffles")

