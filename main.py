import statistics
import matplotlib.pyplot as plt
from collections import Counter


class Iris:
    varieties = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    x_column = 3
    y_column = 1
    k = 0
    dims = 0
    trainSET = None
    testSET = None

    accuracy = 0

    my_colors = {'Iris-setosa': 'red', 'Iris-versicolor': 'green', 'Iris-virginica': 'blue'}

    def __init__(self, k, train_set='iris.data', test_set='iris.test.data'):
        self.trainSET = self.load_data(train_set)
        self.testSET = self.load_data(test_set)
        self.k = k
        self.dims = self.find_dims()

    def set_k(self, new_k):
        self.k = new_k

    def find_dims(self):
        d = 0
        while type(self.trainSET[0][d]) == int or type(self.trainSET[0][d]) == float:
            d += 1
        return d

    def print_data(self):
        print(' ll' + ' |\t' + 'lw' + ' |\t' + 'pl' + ' |\t' + 'pw' + ' |\t' + '?')
        for e in self.testSET:
            print('#' * 30)
            print(
                str(e[0]) + ' |\t' + str(e[1]) + ' |\t' + str(e[2]) + ' |\t' + str(e[3]) + ' |\t' + str(e[4]) + ' |\t')
        print('#' * 30)
        print('#' * 30)

    def draw_points(self, set, x_column=x_column, y_column=y_column):
        # print(type(set[x_column]))
        xs = []
        ys = []
        if type(set[x_column][0]) == float and type(set[y_column][0]) == float:
            for i in set:
                # print(set[x_column][0], set[y_column][0])
                # print(i[x_column], i[y_column])
                xs.append(i[x_column])
                ys.append(i[y_column])
            for i in range(0, len(xs)):
                # print(set[i][-1])
                plt.scatter(xs[i], ys[i], color=self.my_colors.get(set[i][-1], 'black'))

            plt.ylabel(y_column)
            plt.xlabel(x_column)
            plt.show()

        # print(xs)
        # print(ys)

    def load_data(self, path):
        with open(path) as f:
            lines = f.read().splitlines()
            entries = []
            for i in range(0, len(lines)):
                data = []
                entry = lines[i].split(sep=',')
                for e in entry[:-1]:
                    data.append(float(e))
                data.append(entry[-1])
                entries.append(data)
            return entries

    # def get_distance(self, set, i, j):
    #     scorei = 0
    #     scorej = 0
    #
    #     for e in set[i][1:-1]:
    #         scorei += e**2
    #     for e in set[j][1:-1]:
    #         scorej += e**2
    #     scorei = scorei ** 1/2
    #     scorej = scorej ** 1/2
    #
    #     return abs(scorej - scorei)

    def get_euclidean_neighbours(self, i):
        neighbours = []
        for idx, e in enumerate(self.trainSET):
            res = ((self.trainSET[idx][0] - self.testSET[i][0]) ** 2
                   + (self.trainSET[idx][1] - self.testSET[i][1]) ** 2
                   + (self.trainSET[idx][2] - self.testSET[i][2]) ** 2
                   + (self.trainSET[idx][3] - self.testSET[i][3]) ** 2) ** 0.5
            neighbours.append([idx, round(res, 3), self.trainSET[idx][-1]])

        neighbours = sorted(neighbours, key=lambda distance: distance[1])

        return neighbours

    # for n dimensional vectors

    def get_n_euclidean_neighbours(self, i):
        neighbours = []
        for idx, e in enumerate(self.trainSET):
            res = 0

            for d in range(0, self.dims-1):
                res += (self.trainSET[idx][d] - self.testSET[i][d]) ** 2

            res = res ** 0.5

            neighbours.append([idx, round(res, 3), self.trainSET[idx][-1]])

        neighbours = sorted(neighbours, key=lambda distance: distance[1])

        return neighbours


def main():
    iris = Iris(7)
    print(iris.dims)
    correct = 0
    total = len(iris.testSET)

    # Loop throught the test vectors.
    for idx, e in enumerate(iris.testSET):
        species = []
        occurences = dict()
        neig = iris.get_n_euclidean_neighbours(idx)
        # print(neig[0:iris.k])
        for i in range(iris.k):
            species.append(neig[i][-1])
        print(species)

        for s in species:
            if s in occurences:
                occurences[s] += 1
            else:
                occurences[s] = 1

        prediction = max(occurences, key=occurences.get)

        if prediction == iris.testSET[idx][-1]:
            print(prediction)
            print(iris.testSET[idx][-1])
            correct += 1
        else:
            print("WRONG")
            print(prediction)
            print(iris.testSET[idx][-1])

    print(correct, '\t', total)
    acc = correct / total
    print(acc)


if __name__ == '__main__':
    print('Run main')
    main()
