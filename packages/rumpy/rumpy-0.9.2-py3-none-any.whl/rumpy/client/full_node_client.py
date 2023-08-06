import logging
import os

from rumpy.api import BaseAPI, FullNodeAPI, PaidGroup
from rumpy.client._flask_extensions import _init_app
from rumpy.client._requests import HttpRequest
from rumpy.types.data import ApiBaseURLS

logger = logging.getLogger(__name__)


class FullNode:
    _group_id = None

    def __init__(
        self,
        port=None,
        api_base=None,
        jwt_token=None,
    ):
        api_base = api_base or ApiBaseURLS(protocol="http", port=port, host="127.0.0.1").FULL_NODE
        self.http = HttpRequest(api_base=api_base, jwt_token=jwt_token)
        self.api = self.http.api = FullNodeAPI(self.http)
        self.paid = self.http.paid = PaidGroup(self.http)
        # TODO:paid其实也是 api 的一类，这个处理需要集中搞下

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        self._group_id = group_id
        self.http.group_id = group_id

    def init_app(self, app, rum_kspasswd=None, rum_port=None):
        return _init_app(self, app, rum_kspasswd, rum_port)
