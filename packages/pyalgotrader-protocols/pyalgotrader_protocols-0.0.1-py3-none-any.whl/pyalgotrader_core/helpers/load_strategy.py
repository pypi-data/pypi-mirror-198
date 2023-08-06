from git import Repo
import pathlib
import shutil
from importlib import import_module


async def load_strategy(repository: str):
    try:
        path = pathlib.Path("algorithm")

        if path.exists():
            shutil.rmtree(path)

        Repo.clone_from(repository, path)

        strategy = import_module("algorithm.strategy")

        return getattr(strategy, "Strategy")
    except Exception as e:
        print("Invalid strategy")
