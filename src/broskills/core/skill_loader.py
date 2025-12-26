"""Skill loader for parsing and loading skills"""

from pathlib import Path
from typing import Dict, Any, List
from ..utils.parsers import parse_skill_file, validate_skill_metadata


class Skill:
    """Represents a loaded skill"""
    
    def __init__(self, name: str, description: str, content: str, tools: List[str] = None):
        self.name = name
        self.description = description
        self.content = content
        self.tools = tools or []
    
    def __str__(self) -> str:
        return f"Skill({self.name}): {self.description}"


class SkillLoader:
    """Loads skills from files or directories"""
    
    def load_skill(self, skill_path: str) -> Skill:
        """Load a single skill from file"""
        parsed = parse_skill_file(skill_path)
        metadata = parsed['metadata']
        
        if not validate_skill_metadata(metadata):
            raise ValueError(f"Invalid skill metadata in {skill_path}")
        
        return Skill(
            name=metadata['name'],
            description=metadata['description'],
            content=parsed['content'],
            tools=metadata.get('tools', [])
        )
    
    def load_skills_from_directory(self, directory: str) -> Dict[str, Skill]:
        """Load all skills from a directory"""
        skills = {}
        skill_dir = Path(directory)
        
        for skill_folder in skill_dir.iterdir():
            if skill_folder.is_dir():
                skill_file = skill_folder / "SKILL.md"
                if skill_file.exists():
                    try:
                        skill = self.load_skill(str(skill_file))
                        skills[skill.name] = skill
                    except Exception as e:
                        print(f"Failed to load skill from {skill_file}: {e}")
        
        return skills