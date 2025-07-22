def retrieve_contexts(dataset):
    # In a real system, you would query a vector store here
    # For now, we just echo back a fixed context
    def add_context(example):
        example["contexts"] = [
            "Paris is the capital of France.",
            "France is located in Western Europe."
        ]
        return example

    return dataset.map(add_context)
