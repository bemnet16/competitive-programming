class Solution(object):
    def kClosest(self, points, k):

        #check weather k(length) is valid or not
        if k < 1 or k > len(points):
            return "The required lenght is not valid!"

        for i in range(len(points)):
            for j in range((i + 1),len(points)):
                xi, xj = points[i][0], points[j][0]
                yi, yj = points[i][1], points[j][1]

                #Check value constraints, are point values valid or not
                if (xi <= -10000 or xi >= 10000 or yi <= -10000 or yi >= 10000):
                    return "This is large value/ sorry!"
                elif ((xi ** 2) + (yi ** 2)) > ((xj ** 2) + (yj ** 2)):
                    points[i], points[j] = points[j], points[i]
        
        return points[:k]
