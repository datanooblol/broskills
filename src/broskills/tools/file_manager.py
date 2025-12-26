"""File management tool for CRUD operations"""

import os
from pathlib import Path
from typing import Any
from .base import BaseTool


class FileManagerTool(BaseTool):
    """Tool for file CRUD operations"""
    
    name = "file_manager"
    description = "Create, read, update, and delete files"
    
    def execute(self, action: str, **kwargs) -> Any:
        """Execute file operation"""
        if action == "create":
            return self.create_file(kwargs["path"], kwargs["content"])
        elif action == "read":
            return self.read_file(kwargs["path"])
        elif action == "update":
            return self.update_file(kwargs["path"], kwargs["content"])
        elif action == "delete":
            return self.delete_file(kwargs["path"])
        else:
            raise ValueError(f"Unknown action: {action}")
    
    def create_file(self, path: str, content: str) -> str:
        """Create a new file"""
        file_path = Path(path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding='utf-8')
        return f"File created: {path}"
    
    def read_file(self, path: str) -> str:
        """Read file content"""
        return Path(path).read_text(encoding='utf-8')
    
    def update_file(self, path: str, content: str) -> str:
        """Update existing file"""
        Path(path).write_text(content, encoding='utf-8')
        return f"File updated: {path}"
    
    def delete_file(self, path: str) -> str:
        """Delete file"""
        Path(path).unlink()
        return f"File deleted: {path}"
    
    def get_available_actions(self) -> dict:
        return {
            "create": "Create a new file",
            "read": "Read file content",
            "update": "Update existing file",
            "delete": "Delete file"
        }