def foo(x: int):
    pass


foo(10)
foo("10")  # expect-type-error
