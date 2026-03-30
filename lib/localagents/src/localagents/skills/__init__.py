"""Agent Skills standard implementation for localAI.

Provides filesystem-based skill packaging with progressive disclosure.
"""

from localagents.skills.loader import activate_skill, discover_skills
from localagents.skills.models import Skill, SkillFrontmatter
from localagents.skills.parser import SkillParseError


__all__ = [
    "Skill",
    "SkillFrontmatter",
    "SkillParseError",
    "activate_skill",
    "discover_skills",
]
