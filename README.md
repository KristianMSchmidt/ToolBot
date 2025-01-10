
# Flexible OpenAI Function-Calling Chatbot

This project is a learning-focused implementation of a chatbot that uses OpenAI's function-calling capabilities. The structure is designed to be flexible, allowing for easy customization of tools and system behavior. While the project includes two specific examples (a weather bot using a weather-related API and a calculator bot), its architecture supports integration with a variety of tools and APIs for other use cases.

## Features

- **Tool-Based Extensibility**: Define tools with specific functions, descriptions, and parameters. Easily integrate additional tools by modifying the tool configuration.
- **Function-Calling with OpenAI API**: Enables dynamic interaction with tools, allowing the chatbot to call functions in response to user input.
- **Customizable Behavior**: System instructions, greeting messages, and tools can be modified to suit different use cases without extensive code changes.
- **Logging and Debugging**: Tool calls and their results are logged for easy debugging and analysis.

## Project Structure

- `src/main.py`: Entry point for the chatbot application.
- `src/chatbot/`: Core chatbot logic, including message handling and tool management.
- `src/tools/`: Definitions and configurations for tools (e.g., weather-related APIs).
- `src/config/`: System-level configurations, such as instructions and greeting messages.
- `src/pytests/`: Unit tests for chatbot components and tools.

## Getting Started

1. **Set up Environment Variables**:
    Create a `.env` file in the project root and provide the required API keys:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    WEATHER_API_KEY=your_weather_api_key
    ```

2. **Install Dependencies**:
    Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Chatbot**:
    ```bash
    python run.py
    ```

## Example Use

While this project includes configurations for two specific chatbots with each their set of tools, the modular design makes it straightforward to replace or add custom chatbots with tools for other domains like finance, travel, or customer support. Simply configure the new chatbot and its tool, and it should work right out of the box. 

## Contributions and Feedback

This project is a personal learning endeavor. If you find it useful or have suggestions for improvement, feel free to share feedback or ideas.

