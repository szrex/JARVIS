from core.events import event_bus
from core.logger import logger


def handle_test_event(data):
    logger.info(f"Event received: {data}")


def run_event_test():
    event_bus.subscribe("test_event", handle_test_event)

    event_bus.publish(
        "test_event",
        {
            "message": "JARVIS event system operational"
        }
    )
