# Project Pressure-Sense
## Project Pressure-Sense: Investigating how AI systems understand and respond to pressure, both in terms of performance and ethical considerations.

This repository is part of my final project under [AI Alignment course](https://aisafetyfundamentals.com/) from AI Safety Fundamentals by Bluedot Impact. 

The project aims to investigate how AI systems, particularly Large Language Models (LLMs), understand and respond to different types of pressure. The project will explore both the performance and ethical implications of AI behaviours under pressure, focusing on identifying potential vulnerabilities

This repository includes prompts and evaluated model completions extended from the work of [technical report](https://www.apolloresearch.ai/s/deception_under_pressure.pdf) "Large Language Models can Strategically Deceive their Users when Put Under Pressure.", in which the authors deployed GPT-4 as an autonomous stock trading agent in a simulated environment. When the model obtained an insider trading tip, it acted on the tip despite knowing it was disapproved by company management. When reporting to its manager, the model hid the real reasons behind its trading decision.

In the scope of this research, however, I would like to focus on a broader sense of emotional support or chit-chatting and discussing. 

## Install

If you want to upload prompts to the OpenAI Playground, you will need to install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To upload a prompt (`prompts/scenario_*/*.json`) to the OpenAI Playground, run:

```bash
python request_playground_json_openai.py
```

To evaluate the conversation using LLM as a judge (in here I'm using Claude 3.5 Sonnet from Anthropic), run:

```bash
python upload_to_claude_judge.py
```
