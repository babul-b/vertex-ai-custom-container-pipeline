"""Simple entrypoint used by Vertex AI custom training jobs.

This file intentionally keeps the logic small for learning purposes.
In a real project, replace this with preprocessing, training, evaluation,
or batch prediction logic.
"""

import os


def main() -> None:
    """Print a test message and the value passed from the pipeline."""
    print("hello_world")
    print(os.getenv("MY_CUSTOM_VAR", "MY_CUSTOM_VAR was not provided"))


if __name__ == "__main__":
    main()
