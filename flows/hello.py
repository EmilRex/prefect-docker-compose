"""A simple flow that says hello"""

from prefect import flow, tags, get_run_logger


@flow
def hello(name: str = "Marvin") -> None:
    get_run_logger().info(f"Hello {name}")


if __name__ == "__main__":
    with tags("local"):
        hello()
