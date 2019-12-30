from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from .KeywordQueryEventListener import KeywordQueryEventListener
from .ItemEnterEventListener import ItemEnterEventListener


class PassstoreExtension(Extension):

    def __init__(self):
        super(PassstoreExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())
