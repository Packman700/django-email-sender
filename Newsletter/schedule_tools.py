import functools
import inspect
from datetime import datetime, timedelta

from django_q.tasks import Schedule


def get_function_argument_value(func, args, kwargs, argument_name):
    """function returns argument name
    WARNING Function should be placed in wrapper"""

    try:
        # Get kwarg
        value = kwargs[argument_name]
    except KeyError:
        try:
            # Get arg
            args_names_tuple = func.__code__.co_varnames[:func.__code__.co_argcount]

            arg_index = args_names_tuple.index(argument_name)
            value = args[arg_index]
        except IndexError:
            # Get default value
            signature = inspect.signature(func)
            default_arguments = {
                k: v.default
                for k, v in signature.parameters.items()
                if v.default is not inspect.Parameter.empty
            }

            value = default_arguments[argument_name]
        except ValueError:
            raise ValueError(f"Argument {argument_name} not found")

    return value


def prevent_multiple_schedule_in_one_day(function):
    """Decorator allow to create new schedule only if similar does not exist"""

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        name = get_function_argument_value(function, args, kwargs, 'name')
        func = get_function_argument_value(function, args, kwargs, 'func')

        tomorrow = datetime.now() + timedelta(days=1)
        if not Schedule.objects.filter(
                func=func,
                next_run__year=tomorrow.year,
                next_run__month=tomorrow.month,
                next_run__day=tomorrow.day,
                name=name):
            return function(*args, **kwargs)
        return lambda: None

    return wrapper
    # return decorator
