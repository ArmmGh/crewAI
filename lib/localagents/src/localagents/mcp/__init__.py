"""MCP (Model Context Protocol) client support for LocalAI agents.

This module provides native MCP client functionality, allowing LocalAI agents
to connect to any MCP-compliant server using various transport types.
"""

from localagents.mcp.client import MCPClient
from localagents.mcp.config import (
    MCPServerConfig,
    MCPServerHTTP,
    MCPServerSSE,
    MCPServerStdio,
)
from localagents.mcp.filters import (
    StaticToolFilter,
    ToolFilter,
    ToolFilterContext,
    create_dynamic_tool_filter,
    create_static_tool_filter,
)
from localagents.mcp.tool_resolver import MCPToolResolver
from localagents.mcp.transports.base import BaseTransport, TransportType


__all__ = [
    "BaseTransport",
    "MCPClient",
    "MCPServerConfig",
    "MCPServerHTTP",
    "MCPServerSSE",
    "MCPServerStdio",
    "MCPToolResolver",
    "StaticToolFilter",
    "ToolFilter",
    "ToolFilterContext",
    "TransportType",
    "create_dynamic_tool_filter",
    "create_static_tool_filter",
]
