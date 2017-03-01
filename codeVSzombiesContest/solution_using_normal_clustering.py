import sys
import math
import random

def getDistance(a, b):
    ret = math.pow((a[0] - b[0]), 2) + math.pow((a[1] - b[1]), 2)
    return math.sqrt(ret)

def getLargestCluster(tuples, distance=4000):
    cluster = [tuples[0]]
    for i in range(1, len(tuples)):
        tuple = tuples[i]
        for j in xrange(len(cluster)):
            tuple_in_cluster = cluster[j]
            if getDistance(tuple_in_cluster, tuple) <= distance:
                cluster.append(tuple)
                break
    
    return cluster

def calculateCentroid(tuples):
        numPoints = len(tuples)
        # Get a list of all coordinates in this cluster
        coords = [list(elem) for elem in tuples]
        # Reformat that so all x's are together, all y'z etc.
        unzipped = zip(*coords)
        # Calculate the mean for each dimension
        return [math.fsum(dList)/numPoints for dList in unzipped]
        

def getSelectedClusterCentroid(ass_pos, human_clusters, zombi_clusters):
    for i in xrange(len(human_clusters)):
        human_cluster_centroid = calculateCentroid(human_clusters[i])
        dist_with_ash = getDistance(ass_pos, human_cluster_centroid)
        for j in xrange(len(zombi_clusters)):
            zombie_cluster_centroid = calculateCentroid(zombi_clusters[j])
            dist_with_zombies = getDistance(zombie_cluster_centroid, human_cluster_centroid)
            if divmod(dist_with_ash, dist_with_zombies)[0] <= 5:
                return human_cluster_centroid
                
    return calculateCentroid(human_clusters[0])


while 1:
    x, y = [int(i) for i in raw_input().split()]
    
    human_count = int(raw_input())
    humans = []
    for i in xrange(human_count):
        human_id, human_x, human_y = [int(j) for j in raw_input().split()]
        human = (human_x, human_y)
        humans.append(human)
        
    zombie_count = int(raw_input())
    zombies = []
    for i in xrange(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in raw_input().split()]
        zombie = (zombie_xnext, zombie_ynext)
        zombies.append(zombie)
        
    human_clusters = []
    
    while humans:
        cluster = getLargestCluster(humans)
        human_clusters.append(cluster)
        humans = list(set(humans) - set(cluster))
        
    human_clusters = sorted(human_clusters, key=lambda cluster: (len(cluster)), reverse = True)
    
    zombi_clusters = []
    
    while zombies:
        cluster = getLargestCluster(zombies, 2000)
        zombi_clusters.append(cluster)
        zombies = list(set(zombies) - set(cluster))
        
    zombi_clusters = sorted(zombi_clusters, key=lambda cluster: (len(cluster)), reverse = True)
    # print >> sys.stderr, "cluster_len:%d" % len(clusters)
    
    # print >> sys.stderr, zombi_clusters
    
     
    
    centroid = getSelectedClusterCentroid([x, y], human_clusters, zombi_clusters)
    
    # print "%d %d" % (clusterCentroids[0][0], clusterCentroids[0][1])
    print "%d %d" % (centroid[0], centroid[1])
    
        
        
        
