"""Utilities for parsing skill files"""

import yaml
from pathlib import Path
from typing import Dict, Any


def parse_skill_file(file_path: str) -> Dict[str, Any]:
    """Parse a SKILL.md file with YAML frontmatter"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.startswith('---'):
        raise ValueError("Skill file must start with YAML frontmatter")
    
    end = content.find('---', 3)
    if end == -1:
        raise ValueError("Invalid YAML frontmatter format")
    
    yaml_content = content[3:end].strip()
    body = content[end+3:].strip()
    
    return {
        'metadata': yaml.safe_load(yaml_content),
        'content': body
    }


def validate_skill_metadata(metadata: Dict[str, Any]) -> bool:
    """Validate skill metadata structure"""
    required_fields = ['name', 'description']
    return all(field in metadata for field in required_fields)