"""Explain catalog — markdown keyed by command-path tuples (stable-contract).

Every noun/verb registered in the CLI should have a catalog entry.
"""

from __future__ import annotations

from pr_fixer_sandbox.cli._errors import EXIT_USER_ERROR, CliError
from pr_fixer_sandbox.explain.catalog import ENTRIES


def resolve(path: tuple[str, ...]) -> str:
    if path in ENTRIES:
        return ENTRIES[path]
    display = " ".join(path) if path else "<root>"
    raise CliError(
        code=EXIT_USER_ERROR,
        message=f"no explain entry for: {display}",
        remediation="list entries with: pr-fixer-sandbox explain pr-fixer-sandbox",
    )


def known_paths() -> list[tuple[str, ...]]:
    return list(ENTRIES.keys())
