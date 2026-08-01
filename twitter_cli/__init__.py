"""twitter-lyr: A CLI for Twitter/X."""

try:
    from importlib.metadata import version

    __version__ = version("twitter-lyr")
except Exception:
    __version__ = "0.0.0"
