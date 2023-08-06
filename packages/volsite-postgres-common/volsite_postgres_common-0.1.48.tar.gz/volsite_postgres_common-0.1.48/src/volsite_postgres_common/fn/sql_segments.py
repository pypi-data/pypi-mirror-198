
from volworld_common.api.CA import CA
from volsite_postgres_common.db.CFn import CFn
from volsite_postgres_common.fn.function import Arg


@deprcated(version='0.1.48', reason="You should use SQL.*")
def sql__input_j_2_iid(att: str) -> str:
    return f"({Arg.input}->>'{att}')::TEXT"

@deprcated(version='0.1.48', reason="You should use SQL.*")
def sql__input_j_2_uuid(att: str) -> str:
    return f"({Arg.input}->>'{att}')::UUID"

@deprcated(version='0.1.48', reason="You should use SQL.*")
def sql__input_j_2_bint_id(att: str) -> str:
    return f"{CFn.id_2_bigint}( ({Arg.input}->>'{att}')::TEXT )"


@deprcated(version='0.1.48', reason="You should use SQL.*")
def sql__input_j_2_int_id(att: str) -> str:
    return f"{CFn.id_2_int}( ({Arg.input}->>'{att}')::TEXT )"


@deprcated(version='0.1.48', reason="You should use SQL.*")
def sql__2_id(*att: str) -> str:
    return f"{CFn.bigint_2_id}({'.'.join(att)})"


@deprcated(version='0.1.48', reason="You should use SQL._2_bint")
def sql__2_bint(*att: str) -> str:
    return f"{CFn.id_2_bigint}({'.'.join(att)})"


@deprcated(version='0.1.48', reason="You should use SQL.order_by_cols")
def sql__order_by_cols(col_dict: dict, def_col: str) -> str:
    res = f"CASE ({Arg.input}->>'{CA.SortBy}')::TEXT"
    for arg in col_dict.keys():
        res = f"{res}\n          WHEN '{arg}' THEN {col_dict[arg]}"
    res = f"{res}\n          ELSE {def_col}"  # ELSE NULL
    res = f"{res}\nEND"
    return res


@deprcated(version='0.1.48', reason="You should use SQL.order_by")
def sql__order_by(col_dict: dict, def_col: str) -> str:
    return (
        f" CASE WHEN ({Arg.input}->>'{CA.SortDirection}')::TEXT = '{CA.Ascending}' THEN "
        f"      {sql__order_by_cols(col_dict, def_col)}"
        f" ELSE"
        f"      NULL"
        f" END"
        f" {CA.Ascending},"
        f""
        f" CASE WHEN ({Arg.input}->>'{CA.SortDirection}')::TEXT = '{CA.Descending}' THEN "
        f"      {sql__order_by_cols(col_dict, def_col)}"
        f" ELSE"
        f"      NULL"
        f" END"
        f" {CA.Descending}"
    )

class SQL:

    @staticmethod
    def input_j_2_iid(att: str) -> str:
        return f"({Arg.input}->>'{att}')::TEXT"

    @staticmethod
    def input_j_2_uuid(att: str) -> str:
        return f"({Arg.input}->>'{att}')::UUID"

    @staticmethod
    def input_j_2_bint_id(att: str) -> str:
        return f"{CFn.id_2_bigint}( ({Arg.input}->>'{att}')::TEXT )"

    @staticmethod
    def input_j_2_int_id(att: str) -> str:
        return f"{CFn.id_2_int}( ({Arg.input}->>'{att}')::TEXT )"

    @staticmethod
    def _2_id(*att: str) -> str:
        return f"{CFn.bigint_2_id}({'.'.join(att)})"

    @staticmethod
    def _2_bint(*att: str) -> str:
        return f"{CFn.id_2_bigint}({'.'.join(att)})"
    @staticmethod
    def jsonb_agg_or_empty(table_column_id: str) -> str:
        return f"{BFn.coalesce}( {BFn.jsonb_agg} ({table_column_id}), '[]'::jsonb )"

    @staticmethod
    def jsonb_object_agg_or_empty(key: str, value: str) -> str:
        return f"{BFn.coalesce}( {BFn.jsonb_object_agg} ({key}, {value}), '{{}}'::jsonb )"

    @staticmethod
    def order_by(col_dict: dict, def_col: str) -> str:
        return (
            f" CASE WHEN ({Arg.input}->>'{CA.SortDirection}')::TEXT = '{CA.Ascending}' THEN "
            f"      {SQL.order_by_cols(col_dict, def_col)}"
            f" ELSE"
            f"      NULL"
            f" END"
            f" {CA.Ascending},"
            f""
            f" CASE WHEN ({Arg.input}->>'{CA.SortDirection}')::TEXT = '{CA.Descending}' THEN "
            f"      {SQL.order_by_cols(col_dict, def_col)}"
            f" ELSE"
            f"      NULL"
            f" END"
            f" {CA.Descending}"
        )

    @staticmethod
    def order_by_cols(col_dict: dict, def_col: str) -> str:
        res = f"CASE ({Arg.input}->>'{CA.SortBy}')::TEXT"
        for arg in col_dict.keys():
            res = f"{res}\n          WHEN '{arg}' THEN {col_dict[arg]}"
        res = f"{res}\n          ELSE {def_col}"  # ELSE NULL
        res = f"{res}\nEND"
        return res