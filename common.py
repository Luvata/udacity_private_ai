import torch


def get_parallel_db(db, remove_idx):
    """
    Return a parallel database which exclude a data point at remove_idx
    If remove_idx >= len(db), result will be the original db
    :param db: torch.tensor, database
    :param remove_idx: int,
    :return: torch.tensor, parallel database
    """
    return torch.cat((db[:remove_idx], db[remove_idx+1:]))


def get_parallel_dbs(db):
    """
    Return all parallel databases of given database
    :param db: torch.tensor, given database
    :return: List[torch.tensor], contains len(db) parallel databases
    """
    dbs = []
    for remove_idx in range(len(db)):
        dbs.append(get_parallel_db(db, remove_idx))
    return dbs


def create_db_and_parallels(num_entries):
    """
    Return an original database and its num_entries parallel databases
    :param num_entries: int, the population size
    :return: (torch.tensor, List[torch.tensor]) origin database & all parallel databases
    """
    db = torch.rand(num_entries) > 0.5
    pdbs = get_parallel_dbs(db)
    return db, pdbs


def get_sensitivity(query, n_entries=1000):
    """
    Calculate sensitivity of a query
    :param query: a function (db: torch.tensor) -> scalar: FloatTensor
    :param n_entries: population size
    :return: sensitivity, the maximum changes of the given query when remove one individual from the database
    """
    db, pdbs = create_db_and_parallels(n_entries)
    full_db_result = query(db)
    sensitivity = 0
    for pdb in pdbs:
        pdb_result = query(pdb)
        db_distance = torch.abs(full_db_result - pdb_result).item()
        if db_distance > sensitivity:
            sensitivity = db_distance
    return sensitivity
