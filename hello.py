from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Greetings")

@mcp.tool(name="say_hello")
def say_hello(name: str) -> str:
    """
    Returns a greeting message for the given name.
    args:
    - name: The name of the person to greet.
    - returns: A greeting string.
    """
    return f"Hey, {name}!, how are you doing today?"


if __name__ == "__main__":
    mcp.run()