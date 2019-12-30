import os
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from .KeywordQueryEventListener import KeywordQueryEventListener
from .ItemEnterEventListener import ItemEnterEventListener


class PassstoreExtension(Extension):
    def __init__(self):
        super(PassstoreExtension, self).__init__()
        path = os.environ.get("PASSWORD_STORE_DIR", "~/.password-store")
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener(path))
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())
