from ragas import evaluate
from ragas.metrics import (
    answer_relevancy,
    context_precision,
    context_recall,
    faithfulness,
)
import pandas as pd

# List of metrics in desired order
METRICS = [faithfulness, answer_relevancy, context_precision, context_recall]

def evaluate_with_metrics(dataset):
    result = evaluate(dataset, metrics=METRICS)

    # Convert overall scores to a DataFrame
    df = pd.DataFrame([
        {
            "metric": metric.name,
            "score": result[metric.name][0],
        }
        for metric in METRICS
    ])

    return df  # ✅ This must be returned