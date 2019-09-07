# import function to unit-test
from sense import sense

# test inputs
observation = 'g'
grid = [['r','r','r'],['r','g','r'],['r','r','r']]
beliefs = [[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]] # start with max uncertainty
pHit = 18.0
pMiss = 9.0

print(sense(observation, grid, beliefs, pHit, pMiss))
