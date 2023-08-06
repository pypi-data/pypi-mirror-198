from bottlenest.common import Module
from bottlenest.transports.cli import CommandFactory
from bottlenest.corecommands.BuildCoreCommand import BuildCoreCommand


@Module(
    providers=[BuildCoreCommand],
)
class CoreCliModule:
    pass


def main():
    CommandFactory.run(CoreCliModule)


if __name__ == "__main__":
    main()
