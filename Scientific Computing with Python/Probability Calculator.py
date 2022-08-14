import copy
import random
# Consider using the modules imported above.

class Hat:
    '''A hat object containing balls that should be copied inside the function.'''
    def __init__(self,**contents):
        self.contents =[]
        for i,j in contents.items():
            for k in range(j):
                self.contents.append(i)

    def draw(self, draws):
        '''This method should remove balls at random from contents and return those balls as a list of strings.
        The balls should not go back into the hat during the draw, similar to an urn experiment without replacement.
        If the number of balls to draw exceeds the available quantity, return all the balls.'''
        A = min(draws, len(self.contents))
        total = []
        # here it will choose a random number then will pop the stack according to this number
        for i in range(A):
            B = random.randrange(len(self.contents))
            total.append(self.contents.pop(B))
        return total

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for i in range(num_experiments):
        A = copy.deepcopy(hat)
        out = {}
        out_list = A.draw(num_balls_drawn)
        for i in out_list:
            out[i] = 1 if (not i in out) else out[i] + 1

        if_success = True
        for i,j in expected_balls.items():
            out_i = out[i] if i in out else 0
            stop = out_i >=j
            if stop == False:
                if_success = False
                break
        if if_success == True: success += 1
    return success / num_experiments

if __name__ == '__main__':
    print(Hat(yellow=3, blue=3, green=6))