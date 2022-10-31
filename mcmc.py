# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 09:13:07 2022

@author: alixp
"""
# Import libraries
from random import choices
import numpy as np

transition_matrix = [
                        [0.9322 , 0.0068 , 0.0610, 0     ],
                        [0.4932 , 0.1620 , 0,      0.3448],
                        [0.4390 , 0      , 0.4701, 0.0909],
                        [0      , 0.1552 , 0.4091, 0.4357]
                    ]
def part_a():
    print("Part A. The sampling probabilities")
    print("P(C|-s,r) = <0.8780, 0.1220>")
    print("P(C|-s,-r) = <0.3103, 0.6897>")
    print("P(R|c,-s,w) = <0.9863, 0.0137>")
    print("P(R|-c,-s,w) = <0.8182, 0.1818>\n\n")

    
def part_b():
    print("Part B. The transition probability matrix")
    print("    S1      S2       S3       S4")
    print("S1  0.9322  0.0068   0.0610   0")
    print("S2  0.4932  0.1620   0        0.3448")
    print("S3  0.4390  0        0.4701   0.0909")
    print("S4  0       0.1552   0.4091   0.4357\n\n")

    
def random_state():
    #[C,S = F,R,W =T]
    var = choices(["T","F"],[0.5,0.5],k=2)
    return var[0] + "F"+ var[1] + "T"

def transition(state):
    if state == 'TFTT' :      # if S1
        return choices(['TFTT' , 'TFFT' , 'FFTT' , 'FFFT'],transition_matrix[0])[0]
    
    elif state == 'TFFT' :    # if S2
        return choices(['TFTT' , 'TFFT' , 'FFTT' , 'FFFT'],transition_matrix[1])[0]

    elif state == 'FFTT' :    # if S3
        return choices(['TFTT' , 'TFFT' , 'FFTT' , 'FFFT'],transition_matrix[2])[0]

    elif state == 'FFFT' :    # if S4
        return choices(['TFTT' , 'TFFT' , 'FFTT' , 'FFFT'],transition_matrix[3])[0]

    else : 
        return "ERROR", state
    


def mcmc_estimation():
   dic = {
       'TFTT' : 0, #S1
       'TFFT' : 0, #S2
       'FFTT' : 0, #S3
       'FFFT' : 0  #S4
       }
   
   # Initialization
   state = random_state()
   dic[state] += 1
   
   for i in range(1000000):
       state = transition(state)
       dic[state] += 1
       
   alpha = 1/1000000
  
   print("P(C|-s,w) = <" + str(round(alpha*(dic['TFTT']+dic['TFFT']),4)) + ", " + str(round(alpha*(dic['FFTT']+dic['FFFT']),4)) + ">")

def part_c():
    print("Part C. The probability for the query")
    mcmc_estimation()

def main():
    part_a()
    part_b()
    part_c()
    
    
if __name__ == "__main__" :
    main()