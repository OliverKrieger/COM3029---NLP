if __name__ == "__main__":
    def data_to_lower(data:list[list[str]]) -> list[list[str]]:
        return [[token.lower() for token in tokens] for tokens in data]

    def load_dataset() -> dict:
        from datasets import load_dataset # Import dataset import function for hugging face
        dataset = load_dataset("surrey-nlp/PLOD-CW") # import the coursework dataset from
        from data_item_obj import DataItem

        train_tokens = dataset["train"]["tokens"]
        train_pos_tags = dataset["train"]["pos_tags"]
        train_ner_tags = dataset["train"]["ner_tags"]

        validation_tokens = dataset["validation"]["tokens"]
        validation_pos_tags = dataset["validation"]["pos_tags"]
        validation_ner_tags = dataset["validation"]["ner_tags"]

        test_tokens = dataset["test"]["tokens"]
        test_pos_tags = dataset["test"]["pos_tags"]
        test_ner_tags = dataset["test"]["ner_tags"]

        train_tokens = data_to_lower(train_tokens)
        validation_tokens = data_to_lower(validation_tokens)
        test_tokens = data_to_lower(test_tokens)

        train_data:list[DataItem] = []
        for idx in range(len(train_tokens)):
            train_data.append(DataItem(train_tokens[idx], train_pos_tags[idx], train_ner_tags[idx]))

        validation_data:list[DataItem] = []
        for idx in range(len(validation_tokens)):
            train_data.append(DataItem(validation_tokens[idx], validation_pos_tags[idx], validation_ner_tags[idx]))

        test_data:list[DataItem] = []
        for idx in range(len(test_tokens)):
            train_data.append(DataItem(test_tokens[idx], test_pos_tags[idx], test_ner_tags[idx]))


        return {"train_data":train_data, "validation_data": validation_data, "test_data": test_data}