"""Entry point for ``python -m pr_fixer_sandbox``."""

from __future__ import annotations

import sys

from pr_fixer_sandbox.cli import main

if __name__ == "__main__":
    sys.exit(main())
