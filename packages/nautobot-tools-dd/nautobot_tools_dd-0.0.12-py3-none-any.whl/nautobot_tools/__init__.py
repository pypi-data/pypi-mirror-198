import os

from nautobot.extras.plugins import PluginConfig


class NautobotYangConfig(PluginConfig):
    name = 'nautobot_tools'
    verbose_name = 'Nautobot Yang'
    description = 'Nautobot Yang'
    version = '0.1'
    author = 'Dimas Ari'
    author_email = 'dimas.ari@dataductus.com'
    base_url = 'yang'
    required_settings = []
    default_settings = {
        'loud': False
    }


config = NautobotYangConfig

_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_data_yang_module():
    return os.path.join(_ROOT, 'yang')
