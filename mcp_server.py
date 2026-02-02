from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("Election Tools")

# Register tool
@mcp.tool()
def voter_count():
    """
    Returns voter count for Hyderabad constituency.
    """
    return {
        "constituency": "Hyderabad",
        "total_voters": 234567
    }

# Run server
if __name__ == "__main__":
    mcp.run()
