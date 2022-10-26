from __future__ import annotations
from abc import ABC, abstractmethod

try:
    import detectorjetson
except ImportError:
    pass
try:
    import jetson.utils
except ImportError:
    pass


class Context():
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, strategy: int, paths_tuple) -> None:
        """
        Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """
        if strategy == 1:
            self._strategy = ConcreteStrategyB
        elif strategy == 2:
            self._strategy = JetsonStrategy(paths_tuple)
        else:
            self._strategy = None

    @property
    def strategy(self) -> Strategy:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._strategy = strategy

    def execute(self, file: str):
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """

        # ...
        return self._strategy.do_algorithm(str)

        # ...


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def do_algorithm(self, file: str):
        pass


"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""


class JetsonStrategy(Strategy):
    detector = None
    paths_tuple = None

    def __init__(self, paths_tuple) -> None:
        self.paths_tuple = paths_tuple
        self.detector = detectorjetson.DetectorJetson(str(self.paths_tuple.path_to_model),
                                                      str(self.paths_tuple.path_to_images_label))

    def do_algorithm(self, file: str):
        image = jetson.utils.loadImage(str(self.paths_tuple.path_to_images) + "/" + file)
        return self.detector.run(image), image.shape[0], image.shape[1]


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, file: str):
        pass
