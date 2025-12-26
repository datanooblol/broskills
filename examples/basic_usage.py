"""Basic usage example for broskills"""

from broskills import SkillExecutor

def main():
    # Initialize executor
    executor = SkillExecutor()
    
    # Load skills from directory
    executor.load_skills("skills")
    
    # List available skills
    print("Available skills:")
    for name, desc in executor.list_available_skills().items():
        print(f"  {name}: {desc}")
    
    # List available tools
    print("\nAvailable tools:")
    for name, desc in executor.list_available_tools().items():
        print(f"  {name}: {desc}")
    
    # Execute a tool directly
    try:
        result = executor.execute_tool("file_manager", "create", 
                                     path="test.txt", content="Hello World!")
        print(f"\nTool execution result: {result}")
    except Exception as e:
        print(f"Tool execution failed: {e}")

if __name__ == "__main__":
    main()