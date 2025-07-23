def generate_answers(dataset):
    # In a real system, you'd call an LLM here
    # We'll just generate a canned answer for now
    def add_answer(example):
        example["answer"] = "Paris is not the capital city of France."
        return example

    return dataset.map(add_answer)
