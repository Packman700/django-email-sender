"""Here we store all custom exceptions"""

# settings exceptions

class EmailHostUserIsNoneError(Exception):
    def __init__(self, msg='Set value of EMAIL_HOST_USER in settings', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class EmailPasswordIsNoneError(Exception):
    def __init__(self, msg='Set value of EMAIL_HOST_PASSWORD in settings', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class AdminReorderIsNotSetError(Exception):
    def __init__(self, msg='Set value of ADMIN_REORDER in settings', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class QClusterIsNotSetError(Exception):
    def __init__(self, msg='Set value of Q_CLUSTER in settings', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


# schedule_mail_message exceptions

class IdIsNotTypeIntError(Exception):
    def __init__(self, msg='Id must be integer value', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class InvalidMethodValueError(Exception):
    def __init__(self, msg='Method argument accept only "DELETE", "INSERT" and "UPDATE" string value', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)