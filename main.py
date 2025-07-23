from dotenv import load_dotenv
import os

from data.processed_dataset import load_dataset
from generation.generator import generate_answers
from evaluation.ragas_eval import evaluate_with_metrics

load_dotenv()

def main():
    dataset = load_dataset()

    print("🤖 Generating answers via chatbot...")
    dataset = generate_answers(dataset)

    print("📊 Running Ragas evaluation...")
    results_df = evaluate_with_metrics(dataset)
    print("\n✅ Ragas Results:")
    print(results_df.to_markdown(index=False))


if __name__ == "__main__":
    main()
