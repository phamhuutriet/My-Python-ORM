class EntEdge:
    def __init__(self, edge_name: str, edge_type, is_list: bool = False) -> None:
        self.edge_name = edge_name
        self.edge_type = edge_type
        self.is_list = is_list
