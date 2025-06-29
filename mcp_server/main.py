# mcp_server/main.py

import os
os.environ["PYLGTV_STORE"] = "/Users/ojaskulkarni/dev/mcp-server-project/lgtv-mcp-experiment/.aiopylgtv.sqlite"

from fastmcp import FastMCP
from tools.tv_controller.netflix_controller import play_netflix

#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# Explicit override BEFORE importing any pylgtv/webos modules


mcp = FastMCP(name="Media Assistant")

@mcp.tool()
async def play_netflix_show(show_name: str) -> str:
    """
    Starts playing a TV show or movie on netflix

    Args:
        show_name (str): The name of the show to play.

    Returns:
        str: Confirmation that the show has started.
    """
    await play_netflix(show_name)
    return f"Started playing '{show_name}' on Netflix."

if __name__ == "__main__":
    mcp.run()