[README.md](https://github.com/user-attachments/files/32572489/README.md)
# AI Tutor Learning Project

A Python/Jupyter-based project package containing programming-question datasets and an AI Tutor evaluation visualization method.

## Project contents

```text
AI_Tutor_Learning_Project/
├── data/
│   ├── programming_questions_solutions.csv
│   └── python_project_dataset.csv
├── src/
│   └── visualizer_snippet.py
├── requirements.txt
└── README.md
```

## Dataset information

The two supplied CSV files each contain 500 rows and 7 columns:

- `Question`
- `Difficulty Level`
- `Programming Language`
- `AI-Generated Solution`
- `Time Complexity`
- `Explanation`
- `Topic`

The files are preserved as provided. They appear to contain the same sample records; compare them before deciding whether both need to remain in the final repository.

## Visualization method

The supplied `visualize_accuracy()` method creates a four-panel performance report:

1. Keyword accuracy per question, grouped by difficulty.
2. Overall keyword-accuracy distribution.
3. Keyword coverage heatmap.
4. Average accuracy by difficulty level.

By default, it saves the plot as `accuracy_report.png` and displays it.

## Requirements

Install the common plotting and data-analysis dependencies:

```bash
pip install -r requirements.txt
```

## Important integration note

`src/visualizer_snippet.py` contains the visualization method exactly as supplied in the conversation. It is a method excerpt, not a self-contained runnable application. The original project must also define:

- `pandas` imported as `pd`
- The remaining methods of `AITutorEvaluator`
- `self.results` with the columns `Keyword Accuracy`, `Difficulty`, and `Response`
- `TEST_CASES` containing `expected_keywords`

The snippet does not include the tutor-generation logic, the evaluator's other methods, or a notebook entry point. Those components have not been fabricated here.

## Running

After integrating the method into the complete evaluator and preparing its required data, call:

```python
evaluator.visualize_accuracy()
```

This creates and displays the accuracy report.

## Suggested GitHub repository name

`AI-Tutor-Learning-Project`
