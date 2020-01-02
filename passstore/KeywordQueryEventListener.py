import json
import logging
from pathlib import Path
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction

logger = logging.getLogger(__name__)


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        passstore_dir = extension.preferences["passstore_dir"]
        p = Path(passstore_dir).expanduser()
        if not p.is_dir():
            p = Path(extension.PASSSTORE_DIR).expanduser()

        fmt = lambda x: str(x).replace(str(p) + "/", "").replace(".gpg", "")
        search_term = "".join(event.get_argument()) if event.get_argument() else None

        if not search_term:
            items = [fmt(i) for i in p.glob("**/*.gpg")]
        else:
            items = [fmt(i) for i in p.glob("**/*.gpg") if search_term in fmt(i)]

        try:
            max_num = int(extension.preferences["max_num"])
            keys = items[0:max_num]
        except ValueError:
            keys = items[0:extension.SEARCH_MAX_NUM]

        results = []
        for key in keys:
            logger.info(key)
            results.append(
                ExtensionResultItem(
                    icon="images/icon.png",
                    name="%s" % key,
                    on_enter=ExtensionCustomAction(
                        {"key": key, "path": str(p),}, keep_app_open=True,
                    ),
                )
            )

        return RenderResultListAction(results)
