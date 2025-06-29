# LGTV MCP Experiment

This project exposes LG Smart TV app actions as tools via Model Context Protocol (MCP), enabling direct integration with Claude Desktop.

---

## Setup Instructions

### 1. Install Dependencies

Install the required Python dependencies using the provided requirements file:

```bash
pip install -r requirements.txt
```

---

### 2. Identify Your TV's IP Address

On your LG Smart TV, go to:

**Settings → Network → Wi-Fi (or Ethernet) → IP Address**

Note the IP address shown (e.g., `192.168.1.10`). You will need this for configuration.

---

### 3. Set SQLite Store Path

This tool uses a SQLite file (`.aiopylgtv.sqlite`) to persist pairing data. The path must be explicitly defined and writable.

Place the file inside your project directory to avoid permission issues (do not use root-level paths like `/.aiopylgtv.sqlite`).

---

## Claude Desktop MCP Configuration

In your Claude Desktop app, edit or create the `claude_desktop_launch_config.json` file with the following content:

```json
{
  "mcpServers": {
    "lgtv-mcp-server": {
      "command": "/Users/ojaskulkarni/dev/mcp-server-project/lgtv-mcp-experiment/mcp_env/bin/python",
      "args": [
        "/Users/ojaskulkarni/dev/mcp-server-project/lgtv-mcp-experiment/mcp-server/main.py"
      ],
      "stdio": true,
      "cwd": "/Users/ojaskulkarni/dev/mcp-server-project/lgtv-mcp-experiment",
      "env": {
        "PYTHONPATH": "/Users/ojaskulkarni/dev/mcp-server-project/lgtv-mcp-experiment",
        "PYLGTV_KEY": "/Users/ojaskulkarni/dev/mcp-server-project/lgtv-mcp-experiment/.aiopylgtv.sqlite",
        "LGTV_IP": "192.168.1.10"
      }
    }
  }
}
```

**Important:** All paths must be absolute. Claude Desktop does not reliably resolve `~` or relative paths.

---

## Using the Tool

1. Open the Claude Desktop app.
2. Navigate to the **Tools** section.
3. Confirm that the MCP server (`lgtv-mcp-server`) is running.
4. Type a prompt such as:

```
Play Bridgerton on Netflix
```

This will trigger the tool, launch the Netflix app on your LG TV, perform a search for "Bridgerton," and start playing the result.
The TV prompts to accept connection during first usage, but is then remembered in the sqlite file.

---

## Roadmap

- [Maybe] Auto-discovery of LG TV IP address via SSDP or mDNS
- [Must] Support for additional streaming apps (YouTube, Prime Video, etc.)
- Enable a discovery server to identify apps and region automatically, and then find content
- Current actions are hardcoded. Possible agent to orchestrate actions automatically (intelligence)

---

## License

This project is intended for educational and experimental use only.