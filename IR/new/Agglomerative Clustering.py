import numpy as np

points = {
    'A': np.array([1,2]),
    'B': np.array([4,3]),
    'C': np.array([2,5]),
    'D': np.array([8,3])
}

# - - - - - - - - - - Functions - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - -

# There are 2 common Distances
# 1) Euclidean Distance
# 2) Manhattan Distance
# complex distances measure can also be used here such as Cosine Similarity


def dist(a, b):   # Euclidean Distance
    ### Method 1 (Compact) - - - - - - 
    eu_dist = np.sqrt(np.sum((a - b) ** 2))
    return np.round(eu_dist,2)
    
    ### Method 2 (Discriptive) - - - - - - 
    # diff = a - b # [(1-4), (2-3)] => [-3, -1]
    # squared_diff = np.square(diff)
    # squared_diff_sum = np.sum(squared_diff) 
    # final_dist = np.sqrt(squared_diff_sum)
    
    # return np.round(final_dist,2)
    
# - - - - - - - - - - - - - - - - - - - - - - - - - -
    
# There are 4 types of linkages
# 1) Single linkage: minimum distance between points in clusters
# 2) Complete linkage: maximum distance between points in clusters
# 3) Average linkage: average distance between all points in clusters
# 4) Ward's method: minimizes variance within clusters


def mid(a, b): # Average linkage
    return (a+b)/2
# - - - - - - - - - - - - - - - - - - - - - - - - - -




print(f'{points = }\n')
while len(points)!=1:
    min_dist = np.inf
    min_pair = None
    min_mid = None
    for (p1_name,p1_val) in points.items():
        for (p2_name,p2_val) in points.items():
            if p1_name != p2_name:
                curr_dist = dist(p1_val,p2_val)
                if min_dist > curr_dist:
                    min_dist = curr_dist
                    min_pair = (p1_name,p2_name)
                    min_mid = mid(p1_val,p2_val)
                
    print(f'{min_pair = }')
    points.pop(min_pair[0])
    points.pop(min_pair[1])
    points[''.join(min_pair)] = min_mid
    print(f'{points = }\n')