from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Election Tools")

@mcp.tool()
def voter_count():
    return {
        "constituency": "Hyderabad",
        "total_voters": 234567
    }

# IMPORTANT: Run as HTTP server (SSE) for Render
if __name__ == "__main__":
    mcp.run_sse(
        host="0.0.0.0",
        port=int(__import__("os").environ.get("PORT", 10000)),
        path="/sse"
    )
