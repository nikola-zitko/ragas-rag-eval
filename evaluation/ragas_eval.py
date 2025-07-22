from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall
from ragas import evaluate

def evaluate_with_metrics(dataset):
    return evaluate(
        dataset,
        metrics=[faithfulness, answer_relevancy, context_precision, context_recall]
    )
