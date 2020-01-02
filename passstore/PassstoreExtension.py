from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from .KeywordQueryEventListener import KeywordQueryEventListener
from .ItemEnterEventListener import ItemEnterEventListener


class PassstoreExtension(Extension):

    PASSSTORE_DIR = "~/.password-store"
    SEARCH_MAX_NUM = 10

    def __init__(self):
        super(PassstoreExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())
