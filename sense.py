# DESCRIPTION: Sense function for a robot-localizer
# PARAMETERS:
# 1) color: the observation that was just made
# 2) grid: a 2D-grid (list of lists) representation of the world
# 3) beliefs: a probability-distribution of initial beliefs
# 4) p_hit: probability of making a correct observation of 'color'
# 5) p_miss: probability of making an incorrect observation of 'color'
# RETURNS: updated probability-distribution of beliefs
def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    # 1) Iterate over 2D-grid
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == color:
                # update the cell with the observed colour
                new_beliefs.append(beliefs[row][col] * p_hit)
            else:
                new_beliefs.append(beliefs[row][col] * p_miss)
    # 2) Normalize the updated grid - TODO
    return new_beliefs
