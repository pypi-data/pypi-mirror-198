from typing import Dict

from .base import BaseService
from ..common.model import Callback


class OssService(BaseService):

    def download_file(self, task_params: Dict = None, callback: Callback = None, **kwargs):
        return self.celery_client.apply(task_name='oss.download_file', task_params=task_params, callback=callback, **kwargs)
