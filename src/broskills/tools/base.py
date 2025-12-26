"""Base tool interface for broskills"""

from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseTool(ABC):
    """Base class for all tools"""
    
    name: str = ""
    description: str = ""
    
    @abstractmethod
    def execute(self, action: str, **kwargs) -> Any:
        """Execute a tool action"""
        pass
    
    def get_available_actions(self) -> Dict[str, str]:
        """Get available actions for this tool"""
        return {}
    
    def __str__(self) -> str:
        return f"{self.name}: {self.description}"