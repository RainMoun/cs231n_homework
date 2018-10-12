from collections import Counter


class NearestNeighbor:
    def __init__(self, k):
        self.k = k
        self.x = None
        self.y = None

    def train(self, train_data, train_label):
        self.x = train_data
        self.y = train_label

    def predict(self, test_data):
        num_test = len(test_data)
        y_pre = [0] * num_test
        count = 0
        for i in test_data:
            distance = []
            for j in self.x:
                dis = 0
                for num in range(len(j)):
                    dis += abs(j[num] - i[num])
                distance.append(dis)
            labels_in_k = []
            for j in range(self.k):
                min_dis = min(distance)
                min_train_set = distance.index(min_dis)
                distance[min_train_set] = float('inf')
                labels_in_k.append(self.y[min_train_set])
            y_pre[count] = Counter(labels_in_k).most_common(1)[0][0]
            count += 1
        return y_pre


if __name__ == '__main__':
    train_x = [[1, 2],
               [1, 1],
               [2, 1],
               [4, 4],
               [4, 5]]
    train_y = [1, 2, 1, 2, 2]
    test_x = [[2, 2]]
    classifier = NearestNeighbor(5)
    classifier.train(train_x, train_y)
    print(classifier.predict(test_x))

