import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Check that the key is loaded
if not os.getenv("OPENAI_API_KEY"):
    raise EnvironmentError("OPENAI_API_KEY not found in environment variables.")

from data.processed_dataset import load_dataset
from retrieval.retriever import retrieve_contexts
from generation.generator import generate_answers
from evaluation.ragas_eval import evaluate_with_metrics


def main():
    print("Loading dataset...")
    dataset = load_dataset()

    print("Retrieving contexts...")
    dataset = retrieve_contexts(dataset)

    print("Generating answers...")
    dataset = generate_answers(dataset)

    print("Running Ragas evaluation...")
    results = evaluate_with_metrics(dataset)

    print("\n✅ RAGAS Evaluation Complete:")
    print(results)


if __name__ == "__main__":
    main()
