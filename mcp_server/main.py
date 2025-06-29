# mcp_server/main.py

import os
os.environ["PYLGTV_STORE"] = "/Users/ojaskulkarni/dev/mcp-server-project/lgtv-mcp-experiment/.aiopylgtv.sqlite"

from fastmcp import FastMCP
from tools.tv_controller.netflix_controller import play_netflix
from typing import Annotated
from pydantic import Field


#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# Explicit override BEFORE importing any pylgtv/webos modules


mcp = FastMCP(name="Media Assistant")

@mcp.tool(
    name="play_netflix_show",
    description="Play the given tv show or movie on Netflix",
    tags={"netflix"},
)
async def play_netflix_show(
    show_name: Annotated[str, Field(description="name of the show or movie to be played")]
) -> str:
    await play_netflix(show_name)
    return f"Started playing '{show_name}' on Netflix."

if __name__ == "__main__":
    mcp.run()