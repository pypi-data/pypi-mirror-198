from bottlenest.transports.cli.decorators.NestCommand import NestCommand
from bottlenest.transports.cli.decorators.NestCommandArgument import NestCommandArgument


def Command(name, *args, **kwargs):
    def decorator(cls):
        return NestCommand(
            cls=cls,
            commandName=name,
            *args,
            **kwargs,
        )
    return decorator


def CommandArgument(name, optional=None, *args, **kwargs):
    def decorator(callback):
        return NestCommandArgument(
            callback=callback,
            argumentName=name,
            optional=optional,
            *args,
            **kwargs,
        )
    return decorator
