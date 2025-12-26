import pytest
import sys
from pathlib import Path

# Add src to path for development
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from broskills.core.skill_loader import SkillLoader
from broskills import SkillExecutor

def test_skill_loader():
    loader = SkillLoader()
    skill = loader.load_skill("skills/spelling-correction/SKILL.md")
    assert skill.name == "spelling correction"
    assert "spelling correction" in skill.description

def test_skill_executor():
    executor = SkillExecutor()
    executor.load_skills("skills")
    
    # Test tool execution
    result = executor.execute_tool("file_manager", "create", 
                                 path="test_file.txt", content="test")
    assert "File created" in result
    
    # Cleanup
    executor.execute_tool("file_manager", "delete", path="test_file.txt")