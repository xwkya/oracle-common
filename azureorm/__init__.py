from .ORMWrapper import ORMWrapper

def setup(server_name, db_name, db_port) -> ORMWrapper:
    return ORMWrapper(server_name=server_name, db_name=db_name, db_port=db_port)