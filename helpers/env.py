import argparse


def get_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--reload', dest="reload", help="Enable app reloading", action="store_true")
    parser.add_argument('--port', dest="port", type=int, default=8000, help="App Port")

    return parser.parse_args()
