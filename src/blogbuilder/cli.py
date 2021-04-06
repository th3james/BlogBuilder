import argparse
parser = argparse.ArgumentParser()
parser.add_argument("name", help="Your name")
args = parser.parse_args()


def cli_main() -> None:
    name = args.name
    print(f"Hello {name} from Blog Builder")
