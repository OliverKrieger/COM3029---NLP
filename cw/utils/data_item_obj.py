class DataItem:
    def __init__(self, tokens, pos, ner):
        self.tokens:list[str] = tokens
        self.pos:list[str] = pos
        self.ner:list[str] = ner

    def get_as_tuple(self) -> tuple:
        return (self.tokens, self.pos, self.ner)
    
    def get_as_tuple_list(self) -> list[tuple]:
        tuple_list = []
        for idx in range(len(self.tokens)-1):
            tuple_list.append((self.tokens[idx], self.pos[idx], self.ner[idx]))
        return tuple_list
    