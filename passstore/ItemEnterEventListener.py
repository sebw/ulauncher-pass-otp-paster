import logging
import subprocess
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

logger = logging.getLogger(__name__)


class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        data = event.get_data()
        logger.info(data["value"])
        subprocess.run(["pass", "-c", data["value"]], check=True)

        return HideWindowAction()
