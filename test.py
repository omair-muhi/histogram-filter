# import function to unit-test
from sense import sense

# test inputs
observation = 'g'
grid = [['r','r','r'],['r','g','r'],['r','r','r']]
beliefs = [[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]] # start with max uncertainty
pHit = 9.0
pMiss = 4.5

print(sense(observation, grid, beliefs, pHit, pMiss))
