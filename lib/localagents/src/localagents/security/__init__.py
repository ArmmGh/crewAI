"""
LocalAI security module.

This module provides security-related functionality for LocalAI, including:
- Fingerprinting for component identity and tracking
- Security configuration for controlling access and permissions
- Future: authentication, scoping, and delegation mechanisms
"""

from localagents.security.fingerprint import Fingerprint
from localagents.security.security_config import SecurityConfig


__all__ = ["Fingerprint", "SecurityConfig"]
