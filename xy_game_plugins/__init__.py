# -*- coding: utf-8 -*-

from packages.blueking.component import collections
from packages.blueking.component.base import ComponentAPI
from packages.blueking.component.client import ComponentClient


class CollectionsSendTelegram(object):

    def __init__(self, client):
        self.client = client

        self.send_tele = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi/xy_game/send_telegram/',
            description=u"发送纸飞机"
        )
        

class CollectionsPushWsCdn(object):

    def __init__(self, client):
        self.client = client

        self.push_wscdn = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi/xy_game/push_ws_cdn/',
            description=u"推送CDN"
        )

collections.AVAILABLE_COLLECTIONS.update({
    'send_telegram': CollectionsSendTelegram,
    'push_ws_cdn': CollectionsPushWsCdn
})

ComponentClient.setup_components(collections.AVAILABLE_COLLECTIONS)