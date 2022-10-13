import collections
import copy
import numpy as np

def get_euclidean_distance(p1:list(), p2: list()):
    """get_euclidean_distance
    Args:
        p1 (list()): The point 1 with x1 coordinate, y1 coordinate in caretesian coordinates plane
        p2 (list()): The point 1 with x1 coordinate, y1 coordinate in caretesian coordinates plane

    Returns:
       distance : Euclidean distance between two pairs pf points
    """
    assert len(p1) > 0 and len(p2) > 0, "One of the two points p1 or p2 is zero length!"

    x1,y1 = p1
    x2, y2 = p2
    d = np.power( np.power(x2-x1,2) + np.power(y2-y1,2), 0.5 )
    return d

def brute_force(points: list()):
    """brute_force method has O(dn^2), where d = 2 (2 Dimensions)
    Args:
        points (list()): List of pairs of points
    Returns:
        min_distance: minimum distance between the closest pair of points
    """
    n = len(points)
    min_distance = float('inf')

    for i in range(n):
        for j in range(i+1,n):
            this_distance = get_euclidean_distance(points[i], points[j])
            if this_distance < min_distance:
                min_distance = this_distance
    return min_distance

def deterministic_algorithm(points:list(), sorted_points:list(), n):
    """deterministic_algorithm where we sort the x and y points. Use Binary search for divide and conquer.
    Sort : O(n log n)


    Args:
        points (list()): [description]
    """

    def get_closer_points(p, m, min_distance):

        this_min = min_distance

        #get all points that are closest for each set of points until difference between y coordinates is less than min_distance
        for i in range(m):
            j = i + 1
            while j < m and (p[j][1] - p[i][1]) < this_min:
                this_min = get_euclidean_distance(p[i], p[j])
                j += 1
        return this_min
    
    min_distance = float('inf')

    mean = n // 2
    mean_point = points[mean]

    this_left_set = points[:mean]
    this_right_set = points[mean:]

    this_left_min_distance = deterministic_algorithm(this_left_set, sorted_points, mean)
    this_right_min_distance = deterministic_algorithm(this_right_set, sorted_points, n - mean)

    min_distance = min(this_left_min_distance, this_right_min_distance)

    #now get all the points that are closer than min_distance
    this_sortedx_points = []
    this_sortedy_points = []
    for i in range(n):
        if abs(this_right_set[i][0] - mean_point[0]) < min_distance:
            this_sortedx_points.append(this_left_set[i])
        if abs(sorted_points[i][0] - mean_point[0]) < min_distance:
            this_sortedy_points.append(sorted_points[i])
    
    this_sortedx_points.sort(key = lambda point: point[1])
    min_a = min(min_distance, get_closer_points(this_sortedx_points, len(this_sortedx_points), min_distance))
    min_b = min(min_distance, get_closer_points(this_sortedy_points, len(this_sortedy_points), min_distance))

    return min(min_a, min_b)


def get_closest_points(points, n):
    points.sort(key = lambda point : point[0])
    sortedy = copy.deepcopy(points)
    sortedy.sort(key = lambda point : point[1])

    return deterministic_algorithm(points, sortedy, n)


#Test results

points = [[2,3], [12,30], [40, 50], [5, 1], [12, 10], [3, 4]]
n = len(points)

print("The closest distance with brute force: ", brute_force(points))
print("The closest distance is: ", get_closest_points(points, n))







