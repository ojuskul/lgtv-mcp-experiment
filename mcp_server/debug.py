# mcp_server/main.py

from fastmcp import FastMCP
#from tools.tv_controller.netflix_controller import play_netflix

mcp = FastMCP(name="Media Assistant")

@mcp.tool()
def say_hello(name: str) -> str:
    """Say hello."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    print("Starting test server...")
    mcp.run()


