from typing import Never


def stop() -> Never:
    """TODO: implement this function to make it type check"""
    raise RuntimeError("")


from typing import assert_never

assert_never(stop())
