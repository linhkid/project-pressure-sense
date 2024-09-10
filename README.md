# project-pressure-sense
Project Pressure-Sense: Investigating how AI systems understand and respond to pressure, both in terms of performance and ethical considerations.

This repository is part of my final project under [AI Alignment course](https://aisafetyfundamentals.com/) from AI Safety Fundamentals by Bluedot Impact. 

The project aims to investigate how AI systems, particularly Large Language Models (LLMs), understand and respond to different types of pressure. The project will explore both the performance and ethical implications of AI behaviours under pressure, focusing on identifying potential vulnerabilities

This repository includes prompts and evaluated model completions extended from the work of [technical report](https://www.apolloresearch.ai/s/deception_under_pressure.pdf) "Large Language Models can Strategically Deceive their Users when Put Under Pressure."

## Install

If you want to upload prompts to the OpenAI Playground, you will need to install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To upload a prompt (`prompts/scenario_*/*.json`) to the OpenAI Playground, run:

```bash
python request_playground_json_openai.py prompts/scenario_1/you_prompt.json
```
