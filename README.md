# userinyerface-mcp-server

A small MCP (Model Context Protocol) server that exposes the official test
cases for the `userinyerface.com` capstone project (Unit 4 — Allure &
Reporting) as MCP tools.

The test cases for this project are **not** included in the practice
repositories. Just like on a real project, they live in a separate test
case management system — here, that system is this MCP server. Connect
your AI client to it and retrieve the test cases you need as part of
Phase 0 of the capstone task.

## What it exposes

Two tools, backed by a single `test_cases.json` file:

* `list_test_cases()` — returns the id and title of every available test
  case (`TC1` Cards, `TC2` Help Form, `TC3` Cookies Form, `TC4` Timer).
* `get_test_case(test_id)` — returns the full test case for a given id:
  host, preconditions, and the step-by-step table (action / expected
  result).

## Setup

Requires Python 3.10+.

```sh
pip install -r requirements.txt
```

You can sanity-check the server runs locally with:

```sh
python server.py
```

(It will sit waiting on stdio — that's expected. Press Ctrl+C to stop.
You don't need to run it manually; your MCP client launches it for you.)

## Connecting via Cursor (free tier)

1. Open Cursor → Settings → MCP.
2. Add a new MCP server with a config like this (adjust the path to
   wherever you cloned this repo):

```json
{
  "mcpServers": {
    "userinyerface-test-cases": {
      "command": "python",
      "args": ["/absolute/path/to/userinyerface-mcp-server/server.py"]
    }
  }
}
```

3. Cursor should show the server as connected, with `list_test_cases`
   and `get_test_case` available as tools.
4. Ask your AI assistant something like *"list the available test cases"*
   or *"get me the test case for TC4"* to confirm it's working.

See the Unit 4 setup video for a full walkthrough.

## Project structure

```
userinyerface-mcp-server/
├── server.py          # MCP server entry point — tool definitions
├── test_cases.json    # The actual test case data
├── requirements.txt
└── README.md
```
