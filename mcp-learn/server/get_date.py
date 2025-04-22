import datetime
from typing import Any

from mcp.server.fastmcp import FastMCP

# Create FastMCP server instance
mcp = FastMCP("get_date")


@mcp.tool()
async def get_current_date() -> dict:
    """
    Get the current date.

    Returns:
        A dictionary containing the current date in various formats.
    """
    current_date = datetime.datetime.now()
    return {
        "year": current_date.year,
        "month": current_date.month,
        "day": current_date.day,
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")
