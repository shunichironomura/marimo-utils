from pathlib import Path

import marimo as mo


def notebook_dir_unwrap() -> Path:
    """`mo.notebook_dir()` wrapper that raises an error if it returns None.

    This function is useful to write code without handling the None case.

    Example:
        ```python
        # Without `notebook_dir_unwrap()`
        import marimo as mo
        parent_dir = mo.notebook_dir().parent # Type checker complains that `mo.notebook_dir()` may return None

        # With `notebook_dir_unwrap()`
        import marimo_utils_sn as mo_sn
        nb_dir = mo_sn.notebook_dir_unwrap() # Type checker knows that the return type is `Path`
        ```

    """
    result = mo.notebook_dir()
    if result is None:
        msg = "mo.notebook_dir() returned None"
        raise RuntimeError(msg)
    return result
