import pytest


def test_imports():
    from rockpool.nn.combinators.sequential import (
        SequentialMixin,
        Sequential,
        JaxSequential,
        ModSequential,
        TorchSequential,
    )

    from rockpool.nn.combinators.ffwd_stack import (
        FFwdStackMixin,
        ModFFwdStack,
        JaxFFwdStack,
        FFwdStack,
    )


def test_Sequential_mod():
    from rockpool.nn.combinators.sequential import Sequential
    from rockpool.nn.modules.native.linear import Linear
    from rockpool.nn.modules.module import Module
    from rockpool.parameters import State, Parameter

    import numpy as np

    # - Define a simple module
    class Mod(Module):
        def __init__(self, shape=None, *args, **kwargs):
            super().__init__(shape=shape, *args, *kwargs)
            self.activation = State(shape=self._shape[-1], init_func=np.zeros)
            self.bias = Parameter(
                shape=self._shape[-1], init_func=np.random.standard_normal
            )

        def evolve(self, input_data, record: bool = False):
            return input_data + self.bias, {}, {}

    seq = Sequential(
        Mod(10),
        Linear((10, 20)),
        Mod(20),
        Linear((20, 30)),
        Mod(30),
        Linear((30, 1)),
        Mod(1),
    )
    print(seq)

    input_data = np.random.rand(100, 10)

    # - Test evolve
    (output, _, _) = seq(input_data)
    print(output.shape)

    # - Test parameters
    print(seq.parameters())
    print(seq.state())


def test_Sequential_jax():
    pytest.importorskip("jax")
    from rockpool.nn.combinators import Sequential
    from rockpool.nn.modules import RateJax
    from rockpool.nn.modules import LinearJax
    from rockpool.nn.modules import JaxModule
    from rockpool.parameters import State, Parameter
    from copy import deepcopy

    import numpy as np
    import jax

    # - Define network size
    Nin = 5
    Nhidden = 2
    Nout = 1

    # - Use 'tanh' in neuron layers, to make sure we don't have vanishing gradients
    seq = Sequential(
        LinearJax((Nin, Nhidden)),
        RateJax(Nhidden, activation_func="tanh"),
        LinearJax((Nhidden, Nout)),
        RateJax(Nout, activation_func="tanh"),
    )
    print("network:", seq)

    # - Test evolve
    T = 10
    input_data = np.random.rand(T, Nin)

    (
        output,
        new_state,
        recorded_state,
    ) = seq(input_data)
    seq = seq.set_attributes(new_state)
    print("output: ", output.T)

    # - Test parameters and state
    print("parameters:", seq.parameters())
    print("state:", seq.state())
    seq = seq.reset_state()

    # - Test compilation
    je = jax.jit(seq)
    (
        output_jit,
        _,
        _,
    ) = je(input_data)
    print("jax.jit output: ", output_jit.T)

    # - Test differentiation
    def loss_sse(grad_params, net, input, target):
        net = net.reset_state()
        net = net.set_attributes(grad_params)
        outputs, _, _ = net(input)
        return np.sum((target - outputs) ** 2)

    params = deepcopy(seq.parameters())

    loss_vgf = jax.jit(jax.value_and_grad(loss_sse))
    loss, grads = loss_vgf(params, seq, input_data, np.random.rand(T, Nout))
    loss, grads = loss_vgf(params, seq, input_data, np.random.rand(T, Nout))

    print("loss:", loss)
    print("grads: ", grads)


def test_Sequential_torch():
    pytest.importorskip("torch")
    from rockpool.nn.combinators.sequential import Sequential
    from rockpool.nn.modules.torch.linear_torch import LinearTorch
    from rockpool.nn.modules.torch.torch_module import TorchModule
    from rockpool.parameters import State, Parameter

    import torch

    # - Define a simple module
    class Mod(TorchModule):
        def __init__(self, shape=None, *args, **kwargs):
            super().__init__(shape=shape, *args, *kwargs)
            self.activation = State(shape=self._shape[-1], init_func=torch.zeros)
            self.bias = Parameter(shape=self._shape[-1], init_func=torch.randn)

        def evolve(self, input_data, record: bool = False):
            return input_data + self.bias, {}, {}

    seq = Sequential(
        Mod(10),
        LinearTorch((10, 20)),
        Mod(20),
        LinearTorch((20, 30)),
        Mod(30),
        LinearTorch((30, 1)),
        Mod(1),
    )
    print(seq)

    input_data = torch.randn((100, 10))

    # - Test evolve
    (
        output,
        _,
        _,
    ) = seq(input_data)
    print(output.shape)

    # - Test parameters
    print(seq.parameters())
    print(seq.state())


def test_FFwdStack_mod():
    from rockpool.nn.combinators.ffwd_stack import FFwdStack
    from rockpool.nn.modules.native.linear import Linear
    from rockpool.nn.modules.module import Module
    from rockpool.parameters import State, Parameter

    import numpy as np

    # - Define a simple module
    class Mod(Module):
        def __init__(self, shape=None, *args, **kwargs):
            super().__init__(shape=shape, *args, *kwargs)
            self.activation = State(shape=self._shape[-1], init_func=np.zeros)
            self.bias = Parameter(
                shape=self._shape[-1], init_func=np.random.standard_normal
            )

        def evolve(self, input_data, record: bool = False):
            return input_data + self.bias, {}, {}

    seq = FFwdStack(
        Mod(10),
        Mod(20),
        Mod(30),
        Mod(1),
    )
    print(seq)

    input_data = np.random.rand(100, 10)

    # - Test evolve
    (
        output,
        _,
        _,
    ) = seq(input_data)
    print(output.shape)

    # - Test parameters
    print(seq.parameters())
    print(seq.state())


def test_FFwdStack_jax():
    pytest.importorskip("jax")
    from rockpool.nn.combinators import FFwdStack
    from rockpool.nn.modules import LinearJax
    from rockpool.nn.modules import JaxModule
    from rockpool.parameters import State, Parameter

    import numpy as np
    from jax import jit

    # - Define a simple module
    class Mod(JaxModule):
        def __init__(self, shape=None, *args, **kwargs):
            super().__init__(shape=shape, *args, *kwargs)
            self.activation = State(shape=self._shape[-1], init_func=np.zeros)
            self.bias = Parameter(
                shape=self._shape[-1], init_func=np.random.standard_normal
            )

        def evolve(self, input_data, record: bool = False):
            return input_data + self.bias, {}, {}

    seq = FFwdStack(
        Mod(10),
        Mod(20),
        Mod(30),
        Mod(1),
    )
    print(seq)

    input_data = np.random.rand(100, 10)

    # - Test evolve
    seq_jit = jit(seq)
    (
        output,
        _,
        _,
    ) = seq_jit(input_data)
    print(output.shape)

    # - Test parameters
    print(seq.parameters())
    print(seq.state())

    # - Test compilation
    je = jit(seq)
    (
        output,
        _,
        _,
    ) = seq(input_data)


def test_FFwdStack_torch():
    pytest.importorskip("torch")
    from rockpool.nn.combinators.ffwd_stack import FFwdStack
    from rockpool.nn.modules.native.linear import Linear
    from rockpool.nn.modules.torch.torch_module import TorchModule
    from rockpool.parameters import State, Parameter

    import torch

    # - Define a simple module
    class Mod(TorchModule):
        def __init__(self, shape=None, *args, **kwargs):
            super().__init__(shape=shape, *args, *kwargs)
            self.activation = State(shape=self._shape[-1], init_func=torch.zeros)
            self.bias = Parameter(shape=self._shape[-1], init_func=torch.randn)

        def evolve(self, input_data, record: bool = False):
            return input_data + self.bias, {}, {}

    seq = FFwdStack(
        Mod(10),
        Mod(20),
        Mod(30),
        Mod(1),
    )
    print(seq)

    input_data = torch.rand((100, 10))

    # - Test evolve
    (
        output,
        _,
        _,
    ) = seq(input_data)
    print(output.shape)

    # - Test parameters
    print(seq.parameters())
    print(seq.state())
