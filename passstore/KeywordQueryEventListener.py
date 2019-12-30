import json
import logging
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction

logger = logging.getLogger(__name__)


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        logger.info('preferences %s' % json.dumps(extension.preferences))
        for i in range(5):
            item_name = extension.preferences['item_name']
            data = {'new_name': '%s %s was clicked' % (item_name, i)}
            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name='%s %s' % (item_name, i),
                                             description='Item description %s' % i,
                                             on_enter=ExtensionCustomAction(data, keep_app_open=True)))

        return RenderResultListAction(items)
