from fastmcp import FastMCP

app = FastMCP(name="remote mcp server")

@app.tool
async def divide(a: int,b: int)->float:
    """Given two numbers a and b this divides them and returns the result."""
    return a/b


if __name__=="__main__":
    app.run(
        transport="http",
        host="0.0.0.0",
        port=8000
    )