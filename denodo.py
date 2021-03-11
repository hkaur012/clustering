import clusters
import sys


def createDendrogram():
    Username, colnames, data = clusters.readfile('tweetdata.txt')
    cluster = clusters.hcluster(data)
    clusters.drawdendrogram(cluster, Username, jpeg='Dendrogram.jpg')
    f = open("ASCII.txt", 'w')
    sys.stdout = f
    clusters.printclust(cluster, labels=Username)
    f.close()
    sys.stderr.close()


if __name__ == "__main__":
    createDendrogram()