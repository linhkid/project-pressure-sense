# Project Pressure-Sense

## Investigating AI Systems' Response to Pressure: Performance and Ethical Considerations

This repository is part of a final project for the [AI Alignment course](https://aisafetyfundamentals.com/) from AI Safety Fundamentals by Bluedot Impact. The project aims to investigate how AI systems, particularly Large Language Models (LLMs), understand and respond to different types of pressure, exploring both performance and ethical implications.

## Project Overview

We extended the work from the [technical report](https://www.apolloresearch.ai/s/deception_under_pressure.pdf) "Large Language Models can Strategically Deceive their Users when Put Under Pressure." Our focus is on a broader sense of emotional support, casual conversation, and discussion.

## Installation

To upload prompts to the OpenAI Playground, install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To upload a prompt to the OpenAI Playground:

```bash
python request_playground_json_openai.py
```

To evaluate conversations using LLM as a judge (Claude 3.5 Sonnet from Anthropic):

```bash
python upload_to_claude_judge.py
```

## Summary of Findings

We evaluated several models (GPT4o, GPT4-0613, Gemini 1.5 Pro, and Llama 3.1 8B) across three scenarios, with and without reasoning capabilities.

### Performance Across Scenarios

![Average Scores of Models Across Scenarios (With Reasoning)](https://github.com/linhkid/project-pressure-sense/blob/main/data/chart/model_comparison_with_reasoning.png)

![Average Scores of Models Across Scenarios (Without Reasoning)](https://github.com/linhkid/project-pressure-sense/blob/main/data/chart/model_comparison_without_reasoning.png)

- **With Reasoning**: GPT4o and Gemini 1.5 Pro performed consistently well.
- **Without Reasoning**: Performance varied more, with Gemini 1.5 Pro showing the most consistent high scores.

### Attribute Performance

![Average Scores Across All Models by Scenario (With Reasoning)](https://github.com/linhkid/project-pressure-sense/blob/main/data/chart/average_scores_with_reasoning.png)

![Average Scores Across All Models by Scenario (Without Reasoning)](https://github.com/linhkid/project-pressure-sense/blob/main/data/chart/average_scores_without_reasoning.png)

- **Pressure Handling**: Generally good, slightly better in Scenarios 1 and 3.
- **Alignment**: High in Scenario 1, lower in Scenarios 2 and 3, especially without reasoning.
- **Truthfulness**: Consistently high across all scenarios.
- **Coherence**: Generally high with some variation, particularly without reasoning.

### Key Observations

1. **Reasoning Importance**: Models with reasoning capabilities generally performed better.
2. **Scenario Difficulty**: Scenario 2 (emotionally volatile client) was most challenging.
3. **Model Differences**: GPT4o and Gemini 1.5 Pro consistently outperformed others.
4. **Ethical Considerations**: High truthfulness maintained, but alignment scores in Scenarios 2 and 3 suggest areas for improvement.

These findings highlight the need for continued research in AI systems' ability to handle pressure and maintain ethical alignment in challenging scenarios.
