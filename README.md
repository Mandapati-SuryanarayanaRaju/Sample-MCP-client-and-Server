# Sample MCP client and Server

This repository contains a minimal example of an MCP (Model Context Protocol) server and client.

- `hello.py` — a small MCP server exposing the `say_hello` tool.
- `client.py` — an MCP client that connects to the server and calls the `say_hello` tool.

## Requirements
- Python 3.13+
- The `mcp` package (version >= 1.22.0)

## Install
From the repository root (recommended inside a virtual environment):

```powershell
python -m pip install --upgrade pip
pip install -e .
```

or install the runtime dependency directly:

```powershell
pip install "mcp[cli]>=1.22.0"
```

## Run
Start the server:

```powershell
python hello.py
```

Run the client (in a separate terminal):

```powershell
python client.py
```

The client will initialize an MCP session with the server and call the `say_hello` tool.

## Notes
- This repo was pushed from a local workspace; local changes may be present.
- Consider adding a `.gitattributes` to normalize line endings on CI if needed.

## License
Add a license file if you plan to share this repository publicly.
