import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# path = ""
# train_data = pd.read_csv(path+"training_data.csv", header=None)

# print(train_data.shape)

# class Trader:
#     def __init__(self):


class Tester:
    state = 0
    money = 0
    prevAction = 0
    lastRow = None
    def __init__(self):
        self.state = 0
        self.money = 0
        self.prevAction = 0
        self.lastRow = pd.Series()

    def doAction(self, row, action):
        if self.prevAction == 1 or self.prevAction == "1":
            self.state += 1
            self.money -= row[0]
        elif self.prevAction == -1 or self.prevAction == "-1":
            self.state -= 1
            self.money += row[0]

        self.prevAction = action
        self.lastRow = row
    
    def endAction(self):
        # return 0 unit
        if self.lastRow.size >= 3:
            self.money += self.state * self.lastRow[3]
        print('money : ' + str(self.money) )


# You can write code above the if-main block.

if __name__ == '__main__':
    # You should not modify this part.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
                       default='training_data.csv',
                       help='input training data file name')
    parser.add_argument('--testing',
                        default='testing_data.csv',
                        help='input testing data file name')
    parser.add_argument('--output',
                        default='output.csv',
                        help='output file name')
    args = parser.parse_args()
    
    # The following part is an example.
    # You can modify it at will.
    training_data = pd.read_csv(args.training)
    # trader = Trader()
    # trader.train(training_data)
    
    testing_data = pd.read_csv(args.testing, header=None)
    tester = Tester()
    # print(testing_data.shape)
    with open(args.output, 'w') as output_file:
        for index,row in testing_data.iterrows():
            # We will perform your action as the open price in the next day.
            # action = trader.predict_action(datum)

            action = "0"
            if (index == 0):
                action = "1"

            tester.doAction(row, action)

            if (index != 0):
                output_file.write("\n")
            output_file.write(action)

            # this is your option, you can leave it empty.
            # trader.re_training(i)
        
        tester.endAction()