import logging
from mxnet.lr_scheduler import LRScheduler

class PIX2PIXScheduler(LRScheduler):
    """Reduce learning rate to linearly decay learning rate to zero
    after certain steps
    ----------
    step:  int
        # of iter at starting learning rate
    step_decay: int
        # of iter to linearly decay learning rate to zero
    """
    def __init__(self, step, step_decay, base_lr):
        super(PIX2PIXScheduler, self).__init__()
        self.step = step
        self.base_lr = base_lr
        self.dlr = base_lr / float(step_decay + 1)

    def __call__(self, num_update):
        """
        Call to schedule current learning rate
        Parameters
        ----------
        num_update: int
            the maximal number of updates applied to a weight.
        """
        if num_update > self.step:
            self.base_lr -= self.dlr
        return self.base_lr