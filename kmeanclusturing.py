import clusters
def kMean():
    kMeanValues = [5, 10, 20]
    Username, colnames, data = clusters.readfile('tweetdata.txt')
    for i in kMeanValues:

        kclust, itercount = clusters.kcluster(data, k=i)
        print(kclust)
        f = open("kclust_%d.txt" % i, 'w')
        f.write("Total Number Of Iterations: %d \n" % itercount)
        print(len(kclust))
        clusterCount = 1
        for cluster in kclust:
            i=1
            f.write("---\n")
            f.write("Cluster %d \n" % clusterCount)
            for tweetID in cluster:
                f.write(str(i)+".\t"+Username[tweetID] + "\n")
                i+=1
            f.write("\n")
            clusterCount+=1
if __name__ == "__main__":
    kMean()