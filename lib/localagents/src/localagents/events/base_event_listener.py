"""Base event listener for LocalAI event system."""

from abc import ABC, abstractmethod

from localagents.events.event_bus import LocalAgentsEventsBus, localagents_event_bus


class BaseEventListener(ABC):
    """Abstract base class for event listeners."""

    verbose: bool = False

    def __init__(self) -> None:
        """Initialize the event listener and register handlers."""
        super().__init__()
        self.setup_listeners(localagents_event_bus)
        localagents_event_bus.validate_dependencies()

    @abstractmethod
    def setup_listeners(self, localagents_event_bus: LocalAgentsEventsBus) -> None:
        """Setup event listeners on the event bus.

        Args:
            localagents_event_bus: The event bus to register listeners on.
        """
