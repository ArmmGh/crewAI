# GenerateLocalagentsAutomationTool

## Description

The GenerateLocalagentsAutomationTool integrates with LocalAI Studio API to generate complete LocalAI automations from natural language descriptions. It translates high-level requirements into functional LocalAI implementations and returns direct links to Studio projects.

## Environment Variables

Set your LocalAI Personal Access Token (LocalAI AMP > Settings > Account > Personal Access Token):

```bash
export LOCALAGENTS_PERSONAL_ACCESS_TOKEN="your_personal_access_token_here"
export LOCALAGENTS_PLUS_URL="https://app.localagents.com"  # optional
```

## Example

```python
from localagents_tools import GenerateLocalagentsAutomationTool
from localagents import Agent, Task, Crew

# Initialize tool
tool = GenerateLocalagentsAutomationTool()

# Generate automation
result = tool.run(
    prompt="Generate a LocalAI automation that scrapes websites and stores data in a database",
    organization_id="org_123"  # optional but recommended
)

print(result)
# Output: Generated LocalAI Studio project URL: https://studio.localagents.com/project/abc123

# Use with agent
agent = Agent(
    role="Automation Architect",
    goal="Generate LocalAI automations",
    backstory="Expert at creating automated workflows",
    tools=[tool]
)

task = Task(
    description="Create a lead qualification automation",
    agent=agent,
    expected_output="Studio project URL"
)

crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
```
