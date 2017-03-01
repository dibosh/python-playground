import sys
import math
import random

# Save humans, destroy zombies!

def main(points, k):
    
    # Number of points in dataset
    num_points = len(points)
    
    # Dim of each point
    dimensions = 2
    
    # The mighty K in k-means
    num_clusters = k
    
    # Optimization convergence cut off
    opt_cutoff = 0.5
    
    return kmeans(points, num_clusters, opt_cutoff)
    
    
class Point:
    def __init__(self, coords):
        self.coords = coords
        self.n = len(coords)
        
    def __repr__(self):
        return str(self.coords)

class Cluster:
    def __init__(self, points):
        if len(points) == 0: return
        # The points that belong to this cluster
        self.points = points
        
        # The dimensionality of the points in this cluster
        self.n = points[0].n
        
        # Assert that all points are of the same dimensionality
        for p in points:
            if p.n != self.n: return
            
        # Set up the initial centroid
        self.centroid = self.calculateCentroid()
        
    def __repr__(self):
        return str(self.points)
    
    def update(self, points):
        '''
        Returns the distance between the previous centroid and the new after
        recalculating and storing the new centroid.
        '''
        old_centroid = self.centroid
        self.points = points
        self.centroid = self.calculateCentroid()
        shift = getDistance(old_centroid, self.centroid) 
        return shift
    
    def calculateCentroid(self):
        '''
        Finds a virtual center point for a group of n-dimensional points
        '''
        numPoints = len(self.points)
        # Get a list of all coordinates in this cluster
        coords = [p.coords for p in self.points]
        # Reformat that so all x's and y's are together
        unzipped = zip(*coords)
        # Calculate the mean for each dimension
        centroid_coords = [math.fsum(dList)/numPoints for dList in unzipped]
        
        return Point(centroid_coords)

def kmeans(points, k, cutoff):
    
    # Pick out k random points to use as our initial centroids
    # There might be cases when human beings are killed, so number of people might become less than k
    k = k if len(points) >= k else len(points)
    initial = random.sample(points, k)
    
    # Create k clusters using those centroids
    clusters = [Cluster([p]) for p in initial]
    
    # Loop through the dataset until the clusters stabilize
    loopCounter = 0
    while True:
        # Create a list of lists to hold the points in each cluster
        lists = [ [] for c in clusters]
        clusterCount = len(clusters)
        
        # Start counting loops
        loopCounter += 1
        # For every point in the dataset ...
        for p in points:
            # Get the distance between that point and the centroid of the first
            # cluster.
            smallest_distance = getDistance(p, clusters[0].centroid)
        
            # Set the cluster this point belongs to
            clusterIndex = 0
        
            # For the remainder of the clusters ...
            for i in range(clusterCount - 1):
                # calculate the distance of that point to each other cluster's
                # centroid.
                distance = getDistance(p, clusters[i+1].centroid)
                # If it's closer to that cluster's centroid update what we
                # think the smallest distance is, and set the point to belong
                # to that cluster
                if distance < smallest_distance:
                    smallest_distance = distance
                    clusterIndex = i+1

            # Add the point to proper cluster
            lists[clusterIndex].append(p)
        
        # Set our biggest_shift to zero for this iteration
        biggest_shift = 0.0
        
        # As many times as there are clusters ...
        for i in range(clusterCount):
            # Calculate how far the centroid moved in this iteration
            shift = clusters[i].update(lists[i])
            # Keep track of the largest move from all cluster centroid updates
            biggest_shift = max(biggest_shift, shift)
        
        # If the centroids have stopped moving much, say we're done!
        if biggest_shift < cutoff:
            break
    return clusters

def getDistance(a, b):
    '''
    Euclidean distance between two n-dimensional points.
    Note: This can be very slow and does not scale well
    '''
    print >> sys.stderr, a
    print >> sys.stderr, b
    # There are cases when a and b becomes null list causing the program to fail : weirdo :/
    if not a.coords:
        a.coords = [0, 0]
    elif not b.coords:
        b.coords = [0, 0]
    ret = math.pow((a.coords[0] - b.coords[0]), 2) + math.pow((a.coords[1] - b.coords[1]), 2)
    return math.sqrt(ret)
    

while 1:
    x, y = [int(i) for i in raw_input().split()]
    
    human_count = int(raw_input())
    humans = []
    for i in xrange(human_count):
        human_id, human_x, human_y = [int(j) for j in raw_input().split()]
        human = Point([human_x, human_y])
        # human = (human_x, human_y)
        humans.append(human)
        
    zombie_count = int(raw_input())
    zombies = []
    for i in xrange(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in raw_input().split()]
        zombie = (zombie_xnext, zombie_ynext)
        zombies.append(zombie)
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    # humans = sorted(humans, key=lambda element: (element[0], element[1]))
    # zombies = sorted(zombies, key=lambda element: (element[0], element[1]), reverse=True)
    
    # if len(humans) <= 5:
    #     min_dist_index = 0
    #     min_dist = get_distance((x,y), (humans[0][0], humans[0][1]))
    #     for i in range(1, len(humans)):
    #         dist = get_distance((x,y), (humans[i][0], humans[i][1]))
    #         print >> sys.stderr, dist
    #         print >> sys.stderr, min_dist
    #         if dist < min_dist:
    #             min_dist = dist
    #             min_dist_index = i
    #         print >> sys.stderr, min_dist
        
    #     print "%d %d" % (get_xy(humans[min_dist_index][0], humans[min_dist_index][1]))
    # else:
    print >> sys.stderr, "Using clustering"
    # points = []
    # for i in xrange(len(humans)):
    #     p = Point([humans[i][0], humans[i][1]])
    #     points.append(p)
        
    print >> sys.stderr, humans
        
    clusters = main(humans, 3)
    clusters = sorted(clusters, key=lambda element: (len(element.points)), reverse = True)

    # if len(clusters[0].points) == len(clusters[1].points) and len(clusters[1].points) == len(clusters[2].points):
    #     min_dist = get_distance((x,y), (clusters[len(clusters) - 1].centroid.coords[0], 
    #     clusters[len(clusters) - 1].centroid.coords[1]))
    #     for i in range(1, len(clusters)):
    #         dist = get_distance((x,y), (clusters[i].centroid.coords[0], clusters[i].centroid.coords[1]))
    #         print >> sys.stderr, dist
    #         print >> sys.stderr, min_dist
    #         if dist < min_dist:
    #             min_dist = dist
    #             min_dist_index = i
    #         print >> sys.stderr, min_dist
    
    # clusters[0] must be the largest cluster after sort
    print "%d %d" % (clusters[0].centroid.coords[0], clusters[0].centroid.coords[1])
    
        
        
        
