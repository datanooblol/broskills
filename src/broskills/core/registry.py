"""Skill registry for managing skills and tools"""

from typing import Dict, Any, Optional
from .skill_loader import Skill, SkillLoader
from ..tools.base import BaseTool
from ..tools.file_manager import FileManagerTool


class SkillRegistry:
    """Registry for skills and tools"""
    
    def __init__(self):
        self.skills: Dict[str, Skill] = {}
        self.tools: Dict[str, BaseTool] = {}
        self.loader = SkillLoader()
        
        # Register default tools
        self.register_tool(FileManagerTool())
    
    def register_skill(self, skill: Skill):
        """Register a skill"""
        self.skills[skill.name] = skill
    
    def register_tool(self, tool: BaseTool):
        """Register a tool"""
        self.tools[tool.name] = tool
    
    def get_skill(self, name: str) -> Optional[Skill]:
        """Get a skill by name"""
        return self.skills.get(name)
    
    def get_tool(self, name: str) -> Optional[BaseTool]:
        """Get a tool by name"""
        return self.tools.get(name)
    
    def load_skills_directory(self, directory: str):
        """Load all skills from directory"""
        skills = self.loader.load_skills_from_directory(directory)
        for skill in skills.values():
            self.register_skill(skill)
    
    def list_skills(self) -> Dict[str, str]:
        """List all available skills"""
        return {name: skill.description for name, skill in self.skills.items()}
    
    def list_tools(self) -> Dict[str, str]:
        """List all available tools"""
        return {name: tool.description for name, tool in self.tools.items()}