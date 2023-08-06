# pylint: disable=missing-docstring
from __future__ import annotations

from typing import Any

import pytest
from beancount.query.query import run_query

from fava.core import FavaLedger
from fava.helpers import FavaAPIException

from .conftest import data_file
from .conftest import SnapshotFunc

LEDGER = FavaLedger(data_file("query-example.beancount"))
QUERY = LEDGER.query_shell


def run(query_string: str) -> Any:
    return QUERY.execute_query(LEDGER.all_entries, query_string)


def run_text(query_string: str) -> str:
    """Run a query that should only return string contents."""
    contents, types, result = run(query_string)
    assert types is None
    assert result is None
    assert isinstance(contents, str)
    return contents


def test_query() -> None:
    assert run_text("help")
    assert (
        run_text("help exit") == "Doesn't do anything in Fava's query shell."
    )
    assert run("lex select date, balance")[0] == "\n".join(
        [
            "LexToken(SELECT,'SELECT',1,0)",
            "LexToken(ID,'date',1,7)",
            "LexToken(COMMA,',',1,11)",
            "LexToken(ID,'balance',1,13)",
        ]
    )

    assert run_text("run") == "custom_query\ncustom query with space"
    bal = run("balances")
    assert run("run custom_query") == bal
    assert run("run 'custom query with space'") == bal
    assert run("balances")[1:] == run_query(
        LEDGER.all_entries, LEDGER.options, "balances"
    )
    assert (
        run_text("asdf")
        == "ERROR: Syntax error near 'asdf' (at 0)\n  asdf\n  ^"
    )


def test_query_to_file(snapshot: SnapshotFunc) -> None:
    entries = LEDGER.all_entries
    name, data = QUERY.query_to_file(entries, "run custom_query", "csv")
    assert name == "custom_query"
    name, data = QUERY.query_to_file(entries, "balances", "csv")
    assert name == "query_result"
    snapshot(data.getvalue())

    with pytest.raises(FavaAPIException):
        QUERY.query_to_file(entries, "select sdf", "csv")

    with pytest.raises(FavaAPIException):
        QUERY.query_to_file(entries, "run testsetest", "csv")
