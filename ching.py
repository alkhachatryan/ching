import itertools
import random

class Game:
    STONE, PAPER, SCISSORS = 0, 1, 2

    def __init__(self):
        indices = [combination for combination in itertools.product([self.STONE, self.PAPER, self.SCISSORS], repeat=6)]

        self.combinations = {}
        for index in indices:
            self.combinations[index] = 0

        self.prev0 = self.prev1 = self.prev2 = self.prev3 = self.prev4 = None

    def user_turn(self, move):
        if self.prev0 is not None and self.prev1 is not None and self.prev2 is not None and self.prev3 is not None and self.prev4 is not None:
            if (
                    self.combinations[(self.prev4, self.prev3, self.prev2, self.prev1, self.prev0, self.SCISSORS)] > self.combinations[
                (self.prev4, self.prev3, self.prev2, self.prev1, self.prev0, self.STONE)]
                    and self.combinations[(self.prev4, self.prev3, self.prev2, self.prev1, self.prev0, self.SCISSORS)] > self.combinations[
                (self.prev4, self.prev3, self.prev2, self.prev1, self.prev0, self.PAPER)]
            ):
                predicted = self.STONE
            elif (
                    self.combinations[(self.prev4, self.prev3, self.prev2, self.prev1, self.prev0, self.STONE)] > self.combinations[
                (self.prev4, self.prev3, self.prev2, self.prev1, self.prev0, self.SCISSORS)]
                    and self.combinations[(self.prev4, self.prev3, self.prev2, self.prev1, self.prev0, self.STONE)] > self.combinations[
                        (self.prev4, self.prev3, self.prev2, self.prev1, self.prev0, self.PAPER)]
            ):
                predicted = self.PAPER

            else:
                predicted = self.SCISSORS

            self.combinations[(self.prev4, self.prev3, self.prev2, self.prev1, self.prev0, predicted)] += 1

        else:
            predicted = random.choice([self.SCISSORS, self.STONE, self.PAPER])

            if self.prev0 is not None and self.prev1 is not None and self.prev2 is not None and self.prev3 is not None and self.prev4 is not None:
                self.combinations[(self.prev4, self.prev3, self.prev2, self.prev1, self.prev0, predicted)] += 1

        self.prev4 = self.prev3
        self.prev3 = self.prev2
        self.prev2 = self.prev1
        self.prev1 = self.prev0
        self.prev0 = move

        return predicted
