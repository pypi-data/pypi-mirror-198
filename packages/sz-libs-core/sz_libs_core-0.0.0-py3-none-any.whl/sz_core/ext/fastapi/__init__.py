try:
    import fastapi
except ImportError:
    raise ImportError(
        "Not found FastAPI dependency."
        " Please run `pip3 install sz-libs-core -E fastapi`"
        " or `pip3 install sz-libs-core -E all`"
    )
