"""Prompt implementations for Sample MCP server."""


def greeting_prompt(name: str) -> str:
    """Generate a greeting prompt.

    Args:
        name: Name of the person to greet.

    Returns:
        A prompt for generating a personalized greeting.
    """
    return f"Please write a warm and friendly greeting for {name}."


def summarize_prompt(topic: str) -> str:
    """Generate a summarization prompt.

    Args:
        topic: The topic to summarize.

    Returns:
        A prompt for summarizing the topic.
    """
    return f"Please provide a brief summary of: {topic}"
