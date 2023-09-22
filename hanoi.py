import matplotlib.pyplot as plt
from stack import Stack
import matplotlib.patches as patches

class Hanoi:
    def __init__(self, N):
        self._left = Stack()
        self._middle = Stack()
        self._right = Stack()
        for i in range(N):
            self._left.push(N-i)
        self._frame_idx = 0
        self._N = N
            
    def draw_frame(self):
        """
        Draw the discs where they currently are, and increment the frame number
        """
        plt.clf()
        ax = plt.gca()
        for k, stack in enumerate([s.get_entire_stack() for s in \
                                    [self._left, self._middle, self._right]]):
            x_center = 0.5 + self._N/2 + k*(0.5 + self._N)
            w = 0.1
            rect = patches.Rectangle((x_center-w, 0), w*2, self._N+1, edgecolor='k', facecolor='k')
            ax.add_patch(rect) 
            for y, disc in enumerate(stack):
                x = x_center - disc/2
                rect = patches.Rectangle((x, y), disc, 1, edgecolor='k', facecolor='C1')
                ax.add_patch(rect)  
        plt.xlim([0, self._N*3+3])
        plt.ylim([0, self._N+1])
        plt.axis('off')
        plt.title("Step {}".format(self._frame_idx))
        plt.savefig("{}.png".format(self._frame_idx), bbox_inches='tight')
        self._frame_idx += 1

    def solve_rec(self, source, free, target, n):
        """
        Parameters
        ----------
        source: stack
            A stack of discs and their sizes that are currently at
            our source peg
        free: stack
            A stack of discs at a peg that can be used as a staging area
        target: stack
            A stack of discs at a peg where we want to put the source discs
        n: int
            The top n discs should be moved from the source peg to the target peg

        Move the top n discs from the source to the target,
        using the free area as a staging area if necessary.
        Hint: 
        1) Recursively move the top n-1 discs out of the way
        2) Move the nth disc from the source to the target, then draw with self.draw_frame()
        3) Recursively move the top n-1 discs over the nth one

        When you're finished, check the directory in which you
        ran this code for a bunch of pictures showing the steps!
        """
        ## TODO: Fill this in
        pass
    
    def solve(self):
        """
        Do an animation of the discs
        """
        fscale = 0.5
        plt.figure(figsize=(fscale*(self._N*3+3), fscale*(self._N+1)))
        self._frame_idx = 0
        self.draw_frame()
        self.solve_rec(self._left, self._middle, self._right,self._N)


h = Hanoi(5)
h.solve()
