import json
import logging
from pathlib import Path
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction

logger = logging.getLogger(__name__)


class KeywordQueryEventListener(EventListener):
    def __init__(self, passstore_path):
        self.passstore_path = passstore_path

    def on_event(self, event, extension):
        p = Path(self.passstore_path)
        fmt = (
            lambda x: str(x).replace(self.passstore_path + "/", "").replace(".gpg", "")
        )
        search_term = "".join(event.get_argument()) if event.get_argument() else None

        if not search_term:
            values = [fmt(i) for i in p.glob("**/*.gpg")]
        else:
            values = [fmt(i) for i in p.glob("**/*.gpg") if search_term in fmt(i)]

        items = []
        for value in values:
            logger.info(value)
            items.append(
                ExtensionResultItem(
                    icon="images/icon.png",
                    name="%s" % value,
                    on_enter=ExtensionCustomAction(
                        {"value": value}, keep_app_open=True
                    ),
                )
            )

        return RenderResultListAction(items)
