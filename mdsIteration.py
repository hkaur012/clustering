import clusters    


Username, words, data = clusters.readfile('tweetdata.txt')
coords, itercount = clusters.scaledown(data)
clusters.draw2d(coords, labels=Username, jpeg='mds.jpg')
print ('Iteration count: %d' % itercount)