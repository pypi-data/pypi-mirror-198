try:
    import consul
except ImportError:
    raise ImportError(
        "Not found Consul dependencies."
        " Please run `pip3 install sz-libs-core -E consul`"
        " or `pip3 install sz-libs-core -E all`"
    )
