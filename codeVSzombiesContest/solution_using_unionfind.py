import sys
import math
import random
import bisect

# Save humans, destroy zombies!
class SortedList(list):
    '''just a list but with an insort (insert into sorted position)'''
    def insort(self,x):
        self=bisect.insort(self,x)

class UnionFind:
    """Union-find data structure. Items must be hashable."""

    def __init__(self):
        """Create a new empty union-find structure."""
        self.weights = {}
        self.parents = {}

    def __getitem__(self, obj):
        """X[item] will return the token object of the set which contains `item`"""

        # check for previously unknown object
        if obj not in self.parents:
            self.parents[obj] = obj 
            self.weights[obj] = 1
            return obj 

        # find path of objects leading to the root
        path = [obj]
        root = self.parents[obj]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root

    def union(self, obj1, obj2):
        """Merges sets containing obj1 and obj2."""
        roots = [self[obj1], self[obj2]]
        heavier = max([(self.weights[r],r) for r in roots])[1]
        for r in roots:
            if r != heavier:
                self.weights[heavier] += self.weights[r]
                self.parents[r] = heavier
                
                
def groupTPL(TPL, distance=1):
    U = UnionFind()

    for (i, x) in enumerate(TPL):
        for j in range(i + 1, len(TPL)):
            y = TPL[j]
            if max(abs(x[0] - y[0]), abs(x[1] - y[1])) <= distance:
                U.union(x, y)

    disjSets = {}
    for x in TPL:
        s = disjSets.get(U[x], set())
        s.add(x)
        disjSets[U[x]] = s

    return [list(x) for x in disjSets.values()]
    

def calculateCentroid(tuples):
        numPoints = len(tuples)
        # Get a list of all coordinates in this cluster
        coords = [list(elem) for elem in tuples]
        # Reformat that so all x's are together, all y'z etc.
        unzipped = zip(*coords)
        # Calculate the mean for each dimension
        return [math.fsum(dList)/numPoints for dList in unzipped]


while 1:
    x, y = [int(i) for i in raw_input().split()]
    
    human_count = int(raw_input())
    humans = []
    for i in xrange(human_count):
        human_id, human_x, human_y = [int(j) for j in raw_input().split()]
        human = (human_x, human_y)
        # human = (human_x, human_y)
        humans.append(human)
        
    zombie_count = int(raw_input())
    zombies = []
    for i in xrange(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in raw_input().split()]
        zombie = (zombie_xnext, zombie_ynext)
        zombies.append(zombie)
    
    clusters = groupTPL(humans, 3000)
    # sort in ascending order of number of tuples in one cluster
    clusters = sorted(clusters, key=lambda element: len(element), reverse=True)
    # print >> sys.stderr, clusters
    # clusterCentroids = []
    
    # for i in xrange(len(clusters)):
    #     centroid = calculateCentroid(clusters[i])
    #     clusterCentroids.append(centroid)
    
    # print >> sys.stderr, clusterCentroids
    
    # clusterCentroids = sorted(clusterCentroids, key=lambda element: (element[0], element[1]))
    
    # print >> sys.stderr, clusterCentroids
    
    centroid = calculateCentroid(clusters[0])
    
    # print "%d %d" % (clusterCentroids[0][0], clusterCentroids[0][1])
    print "%d %d" % (centroid[0], centroid[1])
    
        
        
        
