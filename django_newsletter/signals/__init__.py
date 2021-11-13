from .email_message import init_signals as email_init_signals
from .member import init_signals as member_init_signals


def init_signals():
    email_init_signals()
    member_init_signals()
