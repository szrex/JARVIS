from collections import defaultdict
from typing import Callable, Any


class EventBus:
    """
    Lightweight internal event system for communication
    between JARVIS modules.
    """

    def __init__(self):
        self._listeners = defaultdict(list)

    def subscribe(self, event_name: str, callback: Callable):
        """Subscribe a callback to an event."""
        self._listeners[event_name].append(callback)

    def unsubscribe(self, event_name: str, callback: Callable):
        """Remove a callback from an event."""
        if callback in self._listeners[event_name]:
            self._listeners[event_name].remove(callback)

    def publish(self, event_name: str, data: Any = None):
        """Publish an event to all registered listeners."""
        for callback in self._listeners[event_name]:
            callback(data)


event_bus = EventBus()
