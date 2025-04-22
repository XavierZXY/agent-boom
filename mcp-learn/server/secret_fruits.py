import random
from typing import Any
import datetime

import httpx
from mcp.server.fastmcp import FastMCP

# Create FastMCP server instance
mcp = FastMCP("secret_fruits")


@mcp.tool()
async def get_fruits() -> dict:
    """
    Get a list of fruits with their corresponding emojis.

    Returns:
        A dictionary mapping fruit names to their emoji representations.
    """
    fruits = {"苹果": "🍎", "香蕉": "🍌", "草莓": "🍓"}
    return {"random_fruit": random.choice(list(fruits.items()))}


@mcp.tool()
async def get_fruit_by_date(year: int, month: int, day: int) -> dict:
    """
    Get a specific fruit based on the day of the week.

    Args:
        year: The year (e.g., 2023)
        month: The month (1-12)
        day: The day (1-31)

    Returns:
        A dictionary with the fruit name and emoji based on day of week:
        - Monday, Tuesday, Wednesday: Apple (苹果)
        - Thursday, Friday: Banana (香蕉)
        - Saturday, Sunday: Strawberry (草莓)
    """
    date = datetime.date(year, month, day)
    weekday = date.weekday()  # 0 is Monday, 6 is Sunday

    fruits = {"苹果": "🍎", "香蕉": "🍌", "草莓": "🍓"}

    if weekday < 3:  # Monday, Tuesday, Wednesday
        fruit_name = "苹果"
    elif weekday < 5:  # Thursday, Friday
        fruit_name = "香蕉"
    else:  # Saturday, Sunday
        fruit_name = "草莓"

    return {"fruit": (fruit_name, fruits[fruit_name])}


if __name__ == "__main__":
    mcp.run(transport="stdio")
