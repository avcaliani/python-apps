#!/usr/bin/env python3
from importlib import import_module
from time import time

from fire import Fire


def main(pipeline: str, **kwargs) -> None:
    started_at = time()
    pipeline = str(pipeline).replace("-", "_").strip().lower()
    module = import_module(f'app.{pipeline}')
    getattr(module, 'run')(**kwargs)
    print(f"Elapsed Time: {round(time() - started_at, 2)}s")


if __name__ == "__main__":
    Fire(main)
