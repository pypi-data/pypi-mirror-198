import numpy as np
import torch
from torch import nn, optim
from torch.nn.modules import Module
from torch.optim import Optimizer

class NN(Module):
    def __init__(self):
        super().__init__()

    def converge_to(self, other_mlp, tau=0.1):
        """
        Make the weights of the current model be a bit closer to the given mlp.
        self.weights = (1 - tau) * self.weights + tau * other_mlp.weights
        Precondition: other_mlp have the exact same shape of self.
        """
        for self_param, other_param in zip(self.parameters(), other_mlp.parameters()):
            self_param.data.copy_(
                self_param.data * (1.0 - tau) + other_param.data * tau
            )

    def learn(self, loss, retain_graph=False):
        self.optimizer.zero_grad()
        loss.backward(retain_graph=retain_graph)
        self.optimizer.step()



class MLP(NN):
    """
    A general MLP class. Initialisation example:
    mlp = MLP(input_size, 64, ReLU(), 64, ReLU(), output_size, Sigmoid())
    """

    def __init__(self, input_size, *layers_data, device, learning_rate=0.01,
                 optimizer_class=optim.Adam):
        """
        For each element in layers_data:
         - If the element is an integer, it will be replaced by a linear layer with this integer as output size,
         - If this is a model (like activation layer) il will be directly integrated
         - If it is a function, it will be used to initialise the weights of the layer before
            So we call layer_data[n](layer_data[n - 1].weights) with n the index of the activation function in
            layers_data
        """
        super().__init__()
        assert issubclass(optimizer_class, Optimizer)
        assert device is not None

        self.layers = nn.ModuleList()
        self.input_size = input_size  # Can be useful later ...
        for data in layers_data:
            layer = data
            if isinstance(data, int):
                layer = nn.Linear(input_size, data)
                input_size = data
            if callable(data) and not isinstance(data, nn.Module):
                data(self.layers[-1].weight)
                continue
            self.layers.append(layer)  # For the next layer

        self.device = device
        self.to(self.device)
        self.learning_rate = learning_rate
        self.optimizer = optimizer_class(params=self.parameters(), lr=learning_rate)

    def forward(self, input_data):
        if isinstance(input_data, np.ndarray):
            input_data = torch.from_numpy(input_data).to(self.device)
        input_data = input_data.float()
        for layer in self.layers:
            input_data = layer(input_data)
        return input_data
