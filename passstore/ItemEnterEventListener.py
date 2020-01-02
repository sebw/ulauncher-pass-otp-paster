import logging
import os
import subprocess
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

logger = logging.getLogger(__name__)


class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        data = event.get_data()
        logger.info(data["key"])
        logger.info(data["path"])
        os.environ["PASSWORD_STORE_DIR"] = data["path"]
        subprocess.run(["pass", "-c", data["key"]], check=True)

        return HideWindowAction()
