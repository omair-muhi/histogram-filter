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
        new_beliefs_tmp = []
        for col in range(len(grid[row])):
            # update individual cells with new probability
            # based on observation made
            if grid[row][col] == color:
                # create a sub-list
                new_beliefs_tmp.append(beliefs[row][col] * p_hit)
            else:
                new_beliefs_tmp.append(beliefs[row][col] * p_miss)
        # add sub-list to main list
        new_beliefs.append(new_beliefs_tmp)
    # 2) Normalize the updated grid
    sum_tmp = []
    for nested_list in new_beliefs:
        # sum all nested-lists
        sum_tmp.append(sum(nested_list))
    # collapse the nested-lists into total sum
    normalized_sum = sum(sum_tmp)
    for i in range(len(new_beliefs)):
        for j in range(len(new_beliefs[i])):
            # normalize
            new_beliefs[i][j] = new_beliefs[i][j]/normalized_sum
    return new_beliefs
