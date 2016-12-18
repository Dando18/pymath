
class LinearInterpolator(object):

    def __init__(self, x, y):
        if type(x) is not list or type(y) is not list:
            raise ValueError('inputs must be lists')
        self.pts = sorted(zip(x, y), key= lambda l: l[0])

    def eval(self, x):
        # y - y1 = m (x - x1)
        if self.pts[0][0] < x < self.pts[len(self.pts)-1][1]:
            for index, item in enumerate(self.pts[1:-1]):
                if item[0] == x:
                    return item[1]
                if self.pts[index-1][0] < x < self.pts[index+1][0]:
                    m = (self.pts[index+1][1] - self.pts[index-1][1]) / (self.pts[index+1][0] - self.pts[index-1][0])
                    return m * (x - self.pts[index+1][0]) + self.pts[index+1][1]
