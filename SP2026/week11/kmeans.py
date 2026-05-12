import matplotlib.pyplot as plt

points = [
    [1, 2], [1.5, 1.8], [2, 2.2],
    [8, 8], [8.5, 8.2], [9, 7.8],
    [4, 9], [4.5, 9.5], [5, 8.8]
]

# separate x and y
x = [p[0] for p in points]
y = [p[1] for p in points]

plt.scatter(x, y)
plt.title("Raw Data")
plt.xlabel=("x")
plt.ylabel=("y")
plt.show()

# pick centers
'''
centers = [
        [1,2],
        [8,8],
        [4,9] ]
'''

centers = [
        [1,1],
        [2,2],
        [3,3] ]
        
'''        
centers = [
        [1,1],
        [5,5],
        [8,8] ]
'''

import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def assign_points(points, centers):
    labels = []
    for point in points:
        distances = [distance(point, center) for center in centers]
        label = distances.index(min(distances))
        labels.append(label)
    return labels

def update_centers(points, labels, k):
    new_centers = []
    for i in range(k):
        cluster_points = [points[j] for j in range(len(points)) if labels[j] == i]
        X_mean = sum(p[0] for p in cluster_points)/len(cluster_points)
        Y_mean = sum(p[1] for p in cluster_points)/len(cluster_points)
        new_centers.append([X_mean, Y_mean])
    return new_centers
    
# One iteration example
labels = assign_points(points, centers)
new_centers = update_centers(points, labels, 3)
print("Labels ", labels)
print("Updated centers: ", new_centers)

colors = ["red", "green", "blue"]
for i, point in enumerate(points):
    plt.scatter(point[0], point[1], color=colors[labels[i]])

for center in new_centers:
    plt.scatter(center[0], center[1], color="black", marker="x", s=100)

plt.title("Cluster Assignment After One Iteration")
plt.xlabel=("x")
plt.xlabel=("y")
plt.show()

print("=============================")


for step in range(5):
    labels = assign_points(points, centers)
    centers = update_centers(points, labels, 3)
    print("Labels ", labels)
    print("Updated centers: ", centers)

for i, point in enumerate(points):
    plt.scatter(point[0], point[1], color=colors[labels[i]])

for center in centers:
    plt.scatter(center[0], center[1], color="black", marker="x", s=100)


plt.title("Cluster Assignment After Five Iterations")
plt.xlabel=("x")
plt.xlabel=("y")
plt.show()


        
        
        
        
        
        
        
        
        
        
        
        












