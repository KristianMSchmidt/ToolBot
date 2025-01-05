from src.chatbot.tool_manager import ToolManager

# Test the initialization of ToolManager
def test_tool_manager_initialization():
    tool_config = [
        {
            "name": "test_tool",
            "description": "A test tool",
            "parameters": {"type": "object", "properties": {}},
            "function": lambda: "test result",
        }
    ]

    tool_manager = ToolManager(tool_config)

    # Check if the tool is registered
    assert len(tool_manager.tools) == 1
    assert tool_manager.tools[0]["function"]["name"] == "test_tool"

    # Check if the function is mapped
    assert "test_tool" in tool_manager.function_map

# Test the define_tool method
def test_define_tool():
    tool_manager = ToolManager([])

    # Define a new tool
    tool_manager.define_tool(
        name="new_tool",
        description="A new tool for testing",
        parameters={"type": "object", "properties": {}},
        function=lambda: "new tool result",
    )

    # Verify the tool is added
    assert len(tool_manager.tools) == 1
    assert tool_manager.tools[0]["function"]["name"] == "new_tool"
    assert "new_tool" in tool_manager.function_map

# Test call_function success case
def test_call_function_success():
    tool_manager = ToolManager([])

    # Define a test tool
    tool_manager.define_tool(
        name="test_tool",
        description="A test tool",
        parameters={"type": "object", "properties": {}},
        function=lambda x: f"Hello, {x}",
    )

    # Call the tool
    result = tool_manager.call_function("test_tool", {"x": "World"})
    assert result == "Hello, World"

# Test call_function when the function is not registered
def test_call_function_unregistered():
    tool_manager = ToolManager([])

    # Call a non-existent function
    result = tool_manager.call_function("non_existent_tool", {})
    assert "Error: Function 'non_existent_tool' is not registered." in result

# Test call_function exception handling
def test_call_function_exception_handling():
    def faulty_function():
        raise ValueError("Something went wrong")

    tool_manager = ToolManager([])
    tool_manager.define_tool(
        name="faulty_tool",
        description="A tool that raises an exception",
        parameters={"type": "object", "properties": {}},
        function=faulty_function,
    )

    # Call the faulty tool
    result = tool_manager.call_function("faulty_tool", {})
    assert "Error calling function 'faulty_tool'" in result
