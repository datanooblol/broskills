"""Skill executor for running skills with tools"""

from typing import Any, Dict, Optional
from .registry import SkillRegistry
from .skill_loader import Skill


class SkillExecutor:
    """Executes skills with tool integration"""
    
    def __init__(self, registry: Optional[SkillRegistry] = None):
        self.registry = registry or SkillRegistry()
    
    def run_skill(self, skill_name: str, prompt: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Execute a skill with given prompt and context"""
        skill = self.registry.get_skill(skill_name)
        if not skill:
            raise ValueError(f"Skill '{skill_name}' not found")
        
        context = context or {}
        
        # Prepare skill context
        skill_context = {
            'skill_name': skill.name,
            'skill_description': skill.description,
            'skill_content': skill.content,
            'prompt': prompt,
            'context': context,
            'available_tools': [self.registry.get_tool(tool_name) for tool_name in skill.tools if self.registry.get_tool(tool_name)]
        }
        
        # For now, return the prepared context
        # In a full implementation, this would integrate with an LLM
        return {
            'skill': skill_name,
            'prompt': prompt,
            'context': skill_context,
            'tools_available': [tool.name for tool in skill_context['available_tools']]
        }
    
    def execute_tool(self, tool_name: str, action: str, **kwargs) -> Any:
        """Execute a tool action"""
        tool = self.registry.get_tool(tool_name)
        if not tool:
            raise ValueError(f"Tool '{tool_name}' not found")
        
        return tool.execute(action, **kwargs)
    
    def load_skills(self, directory: str):
        """Load skills from directory"""
        self.registry.load_skills_directory(directory)
    
    def list_available_skills(self) -> Dict[str, str]:
        """List all available skills"""
        return self.registry.list_skills()
    
    def list_available_tools(self) -> Dict[str, str]:
        """List all available tools"""
        return self.registry.list_tools()