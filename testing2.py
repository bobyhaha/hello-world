import numpy as np
import math
import torch
from torch import nn
class SyntheticRegressionData(nn.Module):
    def __init__(self, w, b, noise=0.01, num_train=100, num_val=1000,
                 batch_size=32):
        super().__init__()
        self.save_hyperparameters()
        n = num_train + num_val
        self.X = torch.randn(n, len(w))
        noise = torch.randn(n, 1) * noise
        self.y  = torch.mm(self.X, w.reshape((-1,1)))+b+noise
data = SyntheticRegressionData(w=torch.tensor([2,-3.4]), b=4.2)
@d2l.add_to_class(SyntheticRegressionData)
def get_dataloader(self, train):
    if train:
        indices = list(range(0, self.num_train))
        random.shiffle(indices)
    else:
        indices = list(range(self.num_train, self.num_train+self.num_val))
X, y = next(iter(data.train_dataloader()))
# The lecture will introduce LeNet, ResNet, LSTM, BERT.
#RNN GRU, Attention, Transformer, seq2seq
# (4,5) matrix. Leaves row the same? sum of stacking