import logging

from localagents.tools import BaseTool

from localagents_tools.adapters.tool_collection import ToolCollection
from localagents_tools.tools.localagents_platform_tools.localagents_platform_tool_builder import (
    LocalagentsPlatformToolBuilder,
)


logger = logging.getLogger(__name__)


def LocalagentsPlatformTools(  # noqa: N802
    apps: list[str],
) -> ToolCollection[BaseTool]:
    """Factory function that returns localagents platform tools.

    Args:
        apps: List of platform apps to get tools that are available on the platform.

    Returns:
        A list of BaseTool instances for platform actions
    """
    builder = LocalagentsPlatformToolBuilder(apps=apps)

    return builder.tools()  # type: ignore
