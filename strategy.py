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

    def __init__(self, strategy: int, path_to_model, path_to_images_label, path_to_images) -> None:
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
        self._strategy = JetsonStrategy(path_to_model, path_to_images_label, path_to_images)


    def strategy(self):
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._strategy


    def strategy(self, strategy) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._strategy = strategy

    def execute(self, file):
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """

        # ...
        return self._strategy.do_algorithm(file)

        # ...


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    def do_algorithm(self, file):
        pass


"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""


class JetsonStrategy(Strategy):
    detector = None
    path_to_model = None
    path_to_images_label = None
    path_to_images = None

    def __init__(self, path_to_model, path_to_images_label, path_to_images) -> None:
        self.path_to_model = path_to_model
        self.path_to_images_label = path_to_images_label
        self.path_to_images = path_to_images
        self.detector = detectorjetson.DetectorJetson(str(self.path_to_model),
                                                      str(self.path_to_images_label))

    def do_algorithm(self, file):
        image = jetson.utils.loadImage(str(self.path_to_images) + "/" + file)
        return self.detector.run(image), image.shape[0], image.shape[1]


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, file):
        pass
