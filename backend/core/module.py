from abc import ABC, abstractmethod


class JarvisModule(ABC):
    """
    Base interface for every JARVIS module.
    """

    name = "unnamed"

    @abstractmethod
    def initialize(self):
        """Initialize the module."""
        pass

    @abstractmethod
    def shutdown(self):
        """Cleanly shut down the module."""
        pass

    def status(self):
        """Return module status."""
        return {
            "name": self.name,
            "status": "unknown"
        }
