import inquirer
from bottlenest.metaClasses.NestProvider import NestProvider
from bottlenest.transports.cli.CommandFactory import CommandFactory
from bottlenest.transports.cli.decorators.NestCommandArgument import NestCommandArgument
import sys


class NestCommand(NestProvider):
    __name__ = 'NestCommand'

    def __init__(self, cls, commandName, description):
        self.cls = cls
        self.commandName = commandName
        self.description = description
        CommandFactory.register(self)

    def eventName(self):
        # return NestRoute.__name__
        return self.commandName

    def getName(self):
        return self.commandName

    def parseArguments(self, parser):
        arguments = [ag for ag in dir(self.cls) if isinstance(
            getattr(self.cls, ag), NestCommandArgument)]
        for argumentName in arguments:
            argument = getattr(self.cls, argumentName)
            print(f"argument: {argumentName} {argument}")
            if argument.optional is False:
                parser.add_argument(
                    argument.argumentName,
                    **argument.kwargs,
                    required=True,
                )
            parser.add_argument(
                argument.argumentName,
                **argument.kwargs,
            )

    def setupProvider(self, module, context):
        self._setupProvider(module, context)
        # args = sys.argv[1:]
        # self.provider.run(inquirer, args)
