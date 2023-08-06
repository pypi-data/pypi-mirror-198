try:
    import gql
    import ariadne
except ImportError:
    raise ImportError(
        "Not found GraphQL dependencies."
        " Please run `pip3 install sz-libs-core -E grapqhl`"
        " or `pip3 install sz-libs-core -E all`"
    )
