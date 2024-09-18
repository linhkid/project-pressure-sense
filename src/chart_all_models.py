import matplotlib.pyplot as plt
import numpy as np
import argparse
import json
import os
from utils.config_utils import CONFIG

def plot_radar_chart(data, attributes, title, output_file=None):
    # Number of variables
    num_vars = len(attributes)

    # Compute the angle for each attribute
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]  # Complete the circle

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

    # Custom color cycle
    colors = ['#0000FF', '#FF0000', '#FFFF00', '#008000', '#800080', '#FFA500', '#00FFFF', '#FF00FF']

    # Plot each model
    for (model, scores), color in zip(data.items(), colors):
        values = scores + scores[:1]  # Complete the polygon
        ax.plot(angles, values, linewidth=2, linestyle='solid', label=model, color=color)
        ax.fill(angles, values, alpha=0.25, color=color)

    # Set the attributes
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(attributes)

    # Set y-axis limits
    ax.set_ylim(0, 5)
    ax.set_yticks(range(1, 6))

    # Add grid
    ax.grid(True, linestyle='--', alpha=0.7)

    # Add legend
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

    # Add title
    plt.title(title, y=1.08, fontsize=16, fontweight='bold')

    # Show or save the plot
    plt.tight_layout()
    if output_file:
        plt.savefig(output_file, bbox_inches='tight', dpi=300)
        print(f"Chart saved as {output_file}")
    else:
        plt.show()

def plot_bar_chart(data, attributes, reasoning, output_file=None):
    # Calculate average scores for each scenario and attribute
    avg_scores = {}
    for scenario, scenario_data in data.items():
        avg_scores[scenario] = [np.mean([model_data[i] for model_data in scenario_data.values()]) for i in range(len(attributes))]

    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 6))

    # More aesthetic color palette
    colors = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f', '#edc948']

    # Plot bars
    bar_width = 0.25
    index = np.arange(len(attributes))
    for i, (scenario, scores) in enumerate(avg_scores.items()):
        ax.bar(index + i * bar_width, scores, bar_width, label=f'Scenario {scenario}', color=colors[i], alpha=0.8)

    # Customize the plot
    ax.set_xlabel('Attributes', fontweight='bold', fontsize=12)
    ax.set_ylabel('Average Score', fontweight='bold', fontsize=12)
    ax.set_title(f'Average Scores Across All Models by Scenario\n({("With" if reasoning else "Without")} Reasoning)', fontweight='bold', fontsize=14)
    ax.set_xticks(index + bar_width)
    ax.set_xticklabels(attributes, rotation=0, ha='center', fontsize=10)
    ax.legend(fontsize=10)

    # Add value labels on top of each bar
    for i, (scenario, scores) in enumerate(avg_scores.items()):
        for j, score in enumerate(scores):
            ax.text(j + i * bar_width, score, f'{score:.2f}', ha='center', va='bottom', fontsize=9)

    # Set y-axis limits and add horizontal grid lines
    ax.set_ylim(0, 5.5)
    ax.yaxis.grid(True, linestyle='--', alpha=0.7)
    ax.set_axisbelow(True)

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Adjust layout and display
    plt.tight_layout()
    if output_file:
        plt.savefig(output_file, bbox_inches='tight', dpi=300)
        print(f"Bar chart saved as {output_file}")
    else:
        plt.show()


def plot_model_comparison(data, reasoning, output_file=None):
    # Calculate average scores for each model across attributes
    avg_scores = {}
    for scenario, scenario_data in data.items():
        for model, scores in scenario_data.items():
            if model not in avg_scores:
                avg_scores[model] = {}
            avg_scores[model][scenario] = np.mean(scores)

    # Create the plot
    fig, ax = plt.subplots(figsize=(14, 8))

    # More aesthetic color palette
    colors = plt.cm.get_cmap('tab10')(np.linspace(0, 1, len(avg_scores)))

    # Plot bars
    bar_width = 0.15
    index = np.arange(len(data))
    for i, (model, scores) in enumerate(avg_scores.items()):
        scenario_scores = [scores.get(scenario, 0) for scenario in data.keys()]
        bars = ax.bar(index + i * bar_width, scenario_scores, bar_width, color=colors[i], alpha=0.8)

        # Add model name on top of each bar
        for j, bar in enumerate(bars):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, height, model,
                    ha='center', va='bottom', rotation=90,
                    fontsize=9, fontweight='bold')

    # Customize the plot
    ax.set_xlabel('Scenarios', fontweight='bold', fontsize=12)
    ax.set_ylabel('Average Score', fontweight='bold', fontsize=12)
    ax.set_title(f'Average Scores of Models Across Scenarios\n({("With" if reasoning else "Without")} Reasoning)',
                 fontweight='bold', fontsize=14)
    ax.set_xticks(index + bar_width * (len(avg_scores) - 1) / 2)
    ax.set_xticklabels([f'Scenario {s}' for s in data.keys()], rotation=0, ha='center', fontsize=10)

    # Set y-axis limits and add horizontal grid lines
    ax.set_ylim(0, 5.5)
    ax.yaxis.grid(True, linestyle='--', alpha=0.7)
    ax.set_axisbelow(True)

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Add value labels inside each bar
    for i, (model, scores) in enumerate(avg_scores.items()):
        for j, scenario in enumerate(data.keys()):
            score = scores.get(scenario, 0)
            ax.text(j + i * bar_width, score / 2, f'{score:.2f}',
                    ha='center', va='center', fontsize=9, fontweight='bold', color='white')

    # Adjust layout and display
    plt.tight_layout()
    if output_file:
        plt.savefig(output_file, bbox_inches='tight', dpi=300)
        print(f"Model comparison chart saved as {output_file}")
    else:
        plt.show()

def load_data(scenario, reasoning):
    reasoning_str = "with_reasoning" if reasoning else "without_reasoning"
    data_file = f"scenario_{scenario}_{reasoning_str}.json"
    data_path = os.path.join(CONFIG['data_dir'], data_file)
    with open(data_path, 'r') as file:
        return json.load(file)

def main(reasoning):
    attributes = ['Pressure', 'Alignment', 'Truthfulness', 'Coherence']
    all_data = {}

    # Load data for all scenarios
    for scenario in ['1', '2', '3']:
        try:
            all_data[scenario] = load_data(scenario, reasoning)
        except FileNotFoundError:
            print(f"Warning: Data file for scenario {scenario} not found. Skipping.")

    # Plot attribute comparison bar chart
    output_file_attr = f"data/chart/attribute_comparison_{'with' if reasoning else 'without'}_reasoning.png"
    plot_bar_chart(all_data, attributes, reasoning, output_file_attr)

    # Plot model comparison bar chart
    output_file_model = f"data/chart/model_comparison_{'with' if reasoning else 'without'}_reasoning.png"
    plot_model_comparison(all_data, reasoning, output_file_model)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate charts for model comparisons.")
    parser.add_argument("--reasoning", action="store_true", help="Include reasoning in the output")

    args = parser.parse_args()

    main(args.reasoning)

# def load_data(file_path):
#     with open(file_path, 'r') as file:
#         return json.load(file)
#
# def main(scenario, reasoning):
#     # Attributes (these remain constant)
#     attributes = ['Pressure', 'Alignment', 'Truthfulness', 'Coherence']
#
#     # Construct the data file path
#     reasoning_str = "with_reasoning" if reasoning else "without_reasoning"
#     data_file = f"scenario_{scenario}_{reasoning_str}.json"
#     data_path = os.path.join(CONFIG['data_dir'], data_file)
#
#     # Load data from JSON file
#     try:
#         data = load_data(data_path)
#     except FileNotFoundError:
#         print(f"Error: Data file '{data_path}' not found.")
#         return
#     except json.JSONDecodeError:
#         print(f"Error: Invalid JSON in file '{data_path}'.")
#         return
#
#     # Generate title
#     title = f"Model Comparison: {'With' if reasoning else 'Without'} Reasoning, Scenario {scenario}"
#     output_file = f"data/chart/scenario_{scenario}_{reasoning_str}_chart.png"
#
#     # Plot the chart
#     plot_radar_chart(data, attributes, title, output_file)
#
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Generate a radar chart for model comparisons.")
#     parser.add_argument("scenario", choices=['1', '2', '3'], help="Scenario number (1, 2, or 3)")
#     parser.add_argument("--reasoning", action="store_true", help="Include reasoning in the output")
#
#     args = parser.parse_args()
#
#     main(args.scenario, args.reasoning)