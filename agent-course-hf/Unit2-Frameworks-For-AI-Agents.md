# When to Use an Agentic Framework
An agentic framework is not always needed when building an application around LLMs. They provide flexibility in the workflow to efficiently solve a specific task, but they’re not always necessary.

Sometimes, predefined workflows are sufficient to fulfill user requests, and there is no real need for an agentic framework. If the approach to build an agent is simple, like a chain of prompts, using plain code may be enough. The advantage is that the developer will have full control and understanding of their system without abstractions.

However, when the workflow becomes more complex, such as letting an LLM call functions or using multiple agents, these abstractions start to become helpful.

Considering these ideas, we can already identify the need for some features:

- An LLM engine that powers the system.
- A list of tools the agent can access.
- A parser for extracting tool calls from the LLM output.
- A system prompt synced with the parser.
- A memory system.
- Error logging and retry mechanisms to control LLM mistakes. We’ll explore how these topics are resolved in various frameworks, 
including smolagents, LlamaIndex, and LangGraph.

## Agentic Frameworks Units
- smolagents	Agents framework developed by Hugging Face.	
- Llama-Index	End-to-end tooling to ship a context-augmented AI agent to production	
- LangGraph	Agents allowing stateful orchestration of agents	

# smolagents

`smolagents` is a simple yet powerful framework for building AI agents. It provides LLMs with the agency to interact with the real world, such as searching or generating images.

As we learned in unit 1, AI agents are programs that use LLMs to generate ‘thoughts’ based on ‘observations’ to perform ‘actions’. Let’s explore how this is implemented in smolagents.

