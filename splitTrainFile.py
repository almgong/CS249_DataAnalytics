# load training and test data into (user, product, rating) tuples
def parseRating(line):
	fields = line.split()	
	return (int(fields[0]), int(fields[1]), float(fields[2]))   
data = sc.textFile("/Users/hanwang/CS249_DataAnalytics/data/rec_log_train.txt").map(parseRating).cache()
file1, file2, file3 = data.randomSplit([0.3, 0.5, 0.2])
file1.coalesce(1, True).saveAsTextFile("/Users/hanwang/CS249_DataAnalytics/data/train1")
file2.coalesce(1, True).saveAsTextFile("/Users/hanwang/CS249_DataAnalytics/data/train2")
file3.coalesce(1, True).saveAsTextFile("/Users/hanwang/CS249_DataAnalytics/data/train3")