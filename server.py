"""
userinyerface-mcp-server

A minimal MCP (Model Context Protocol) server that exposes the test
cases for the userinyerface.com project as MCP tools. The test cases
are stored in test_cases.json.

Run it directly for local testing:
    python server.py

Or point your MCP client (e.g. Cursor) at it - see README.md for the
exact config.
"""

import json
from pathlib import Path

from mcp.server.fastmcp import FastMCP

DATA_FILE = Path(__file__).parent / "test_cases.json"

mcp = FastMCP("userinyerface-test-cases")


def _load_test_cases() -> list[dict]:
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)["test_cases"]


@mcp.tool()
def list_test_cases() -> list[dict]:
    """
    List every test case available in the test case management system
    for the userinyerface.com project. Returns only the id and title of
    each test case - call get_test_case with a specific id to see the
    full test case (preconditions, steps, expected results).
    """
    return [{"id": tc["id"], "title": tc["title"]} for tc in _load_test_cases()]


@mcp.tool()
def get_test_case(test_id: str) -> dict:
    """
    Retrieve the full test case for a given id (e.g. "TC1", "TC4").
    Returns the host, preconditions, and the full step-by-step table
    (action / expected result) exactly as recorded by the team.

    If the id doesn't exist, returns an error message instead of
    raising - call list_test_cases first if you're not sure of the id.
    """
    for tc in _load_test_cases():
        if tc["id"].lower() == test_id.strip().lower():
            return tc
    return {
        "error": f"No test case found with id '{test_id}'. "
        "Call list_test_cases to see the available ids."
    }


if __name__ == "__main__":
    mcp.run()
