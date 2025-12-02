from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
import traceback

server_params = StdioServerParameters(
    command= "uv",
    args=["run", "hello.py"],
)

async def run():
    try:
        print("Starting client...")
        async with stdio_client(server_params) as (read, write):

            print("Client started. Creating session...")
            async with ClientSession(read, write) as session:
                
                print("Intializing session...")
                await session.initialize()

                print("Listing available tools...")
                tools = await session.list_tools()
                print("Available tools:", tools)

                print("Calling say_hello tool...")
                result = await session.call_tool( tools.tools[0].name, arguments = {"name": "Surya"})

                print("Result from say_hello:", result)

    except Exception as e:
        print("An error occurred:", str(e))
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(run())