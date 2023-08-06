from plyway.argument_parser import parse_args
from plyway.plyway_config import PlywayConfig


def main() -> None:
    arg_namespace = parse_args()
    plyway_config = PlywayConfig.from_namespace(arg_namespace)
    print(plyway_config)


if __name__ == "__main__":
    main()
