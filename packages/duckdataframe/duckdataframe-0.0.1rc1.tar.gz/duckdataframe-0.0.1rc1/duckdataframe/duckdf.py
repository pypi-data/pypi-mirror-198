from typing import Optional, Union

import duckdb
import numpy as np
import pandas as pd

db = duckdb.connect("tempdb1234.db")


class DuckIndexer:
    def __init__(self, df: "DuckDF"):
        self.df = df

    def __getitem__(self, item):
        df = self.df.df
        return_as_series = False
        returend_series_col = None

        # print(type(item))
        # print(item)
        if isinstance(item, slice):
            item = (item, None)
        elif isinstance(item, tuple):
            if len(item) < 2:
                item = (*item, *[None for _ in range(2 - len(item))])
            elif len(item) > 2:
                raise IndexError("Too many indexers")
        else:
            item = (item, None)

        if isinstance(item, tuple):
            mask, columns = item
            # print(mask, columns)

            if columns is None:
                pass
            elif type(columns) == str:
                return_as_series = True
                returend_series_col = columns
                columns = [columns]
            elif type(columns) == list:
                pass
            elif isinstance(columns, slice):
                begin, end = columns.start, columns.stop

                assert type(begin) in [str, type(None)]
                assert type(end) in [str, type(None)]

                if type(begin) == str:
                    begin = df.columns.index(begin)
                else:
                    begin = 0

                if type(end) == str:
                    end = df.columns.index(end) + 1
                else:
                    end = None

                columns = df.columns[begin:end]
            else:
                raise IndexError(f"Unsupported column indexer: {columns}")

            filtered_df = df

            if mask is not None:
                if type(mask) == DuckSeries:
                    assert mask.parent.shape == df.shape
                    assert mask.filter is not None

                    filtered_df = mask.parent.filter(mask.filter)

            if columns is not None:
                filtered_df = filtered_df.project(",".join(columns))

            if return_as_series:
                return DuckDF(filtered_df)[returend_series_col]
            return DuckDF(filtered_df)
        else:
            return None


    def __setitem__(self, item, value):
        df = self.df.df

        # print(type(item))
        # print(item)
        if isinstance(item, slice):
            item = (item, None)
        elif isinstance(item, tuple):
            if len(item) < 2:
                item = (*item, *[None for _ in range(2 - len(item))])
            elif len(item) > 2:
                raise IndexError("Too many indexers")
        else:
            item = (item, None)

        if isinstance(item, tuple):
            mask, columns = item
            # print(mask, columns)

            df_columns_lower = [c.lower() for c in df.columns]

            if columns is None:
                pass
            elif type(columns) == str:
                columns = [columns]
            elif type(columns) == list:
                pass
            elif isinstance(columns, slice):
                begin, end = columns.start, columns.stop

                assert type(begin) in [str, type(None)]
                assert type(end) in [str, type(None)]

                if type(begin) == str:
                    begin = df_columns_lower.index(begin.lower())
                else:
                    begin = 0

                if type(end) == str:
                    end = df_columns_lower.index(end.lower()) + 1
                else:
                    end = None

                columns = df_columns_lower[begin:end]
            else:
                raise IndexError(f"Unsupported column indexer: {columns}")

            filtered_df = df.project("*, ROW_NUMBER() OVER () AS row_number")

            if mask is not None:
                if type(mask) == DuckSeries:
                    assert mask.parent.shape == df.shape
                    assert mask.filter is not None

                    filtered_df = (
                        mask.parent
                        .project("*, ROW_NUMBER() OVER () AS row_number")
                        .project(f"*, CASE WHEN ({mask.filter}) THEN row_number() OVER (PARTITION BY ({mask.filter})) ELSE NULL END AS mask_row_number")
                        .order("row_number")
                    )
                elif type(mask) == slice:
                    # TODO properly implement slice masks, for now we just use all rows
                    filtered_df = filtered_df.project("*, row_number AS mask_row_number")

            if columns is None:
                columns = df.columns

            columns = [col.lower() for col in columns]

            projections = []

            if type(value) in (DuckDF, DuckSeries):
                if type(value) == DuckDF:
                    assert value.shape == filtered_df.filter("mask_row_number IS NOT NULL").project(",".join(columns)).shape

                    assigned_sql = value.df.sql_query()
                    main_to_assigned_col_mapping = dict(zip(columns, value.df.columns))
                elif type(value) == DuckSeries:
                    values = value.compute()
                    assert values.shape[0] == filtered_df.filter("mask_row_number IS NOT NULL").shape[0]

                    assigned_sql = values.sql_query()
                    main_to_assigned_col_mapping = {c: values.columns[0] for c in columns}
                else:
                    raise NotImplementedError()

                for col in df_columns_lower:
                    if col in columns:
                        mapped_col_name = main_to_assigned_col_mapping[col]
                        projections.append(f"CASE WHEN main.mask_row_number IS NOT NULL THEN value_df.{mapped_col_name} ELSE main.{col} END AS {col}")
                    else:
                        projections.append(f"main.{col} AS {col}")

                query = f"""
                    SELECT {','.join(projections)}
                    FROM 
                        ({filtered_df.sql_query()}) AS main
                        LEFT JOIN
                        (
                            SELECT row_number() OVER () AS row_number, *
                            FROM ({assigned_sql})
                        ) AS value_df 
                        ON 
                            (main.mask_row_number = value_df.row_number)
                    ORDER BY
                        main.row_number
                """

                # print(query)

                mutated_df = db.sql(query)

            # elif type(value) == DuckSeries:
            #     values = value.compute()
            #     assert values.shape[0] == filtered_df.filter("mask_row_number IS NOT NULL").shape[0]
            #
            #     series_col_name = values.columns[0]
            #     series_sql = values.sql_query()
            #
            #     for col in df_columns_lower:
            #         if col in columns:
            #             projections.append(f"CASE WHEN main.mask_row_number IS NOT NULL THEN value_series.{series_col_name} ELSE main.{col} END AS {col}")
            #         else:
            #             projections.append(f"main.{col} AS {col}")
            #
            #     query = f"""
            #         SELECT {','.join(projections)}
            #         FROM
            #             ({filtered_df.sql_query()}) AS main
            #             LEFT JOIN
            #             (
            #                 SELECT row_number() OVER () AS row_number, {series_col_name}
            #                 FROM ({series_sql})
            #             ) AS value_series
            #             ON
            #                 (main.mask_row_number = value_series.row_number)
            #         ORDER BY
            #             main.row_number
            #     """
            #
            #     # print(query)
            #
            #     mutated_df = db.sql(query)

            elif type(value) in (pd.Series, list) or isinstance(value, np.ndarray):
                for col in df_columns_lower:
                    if col in columns:
                        projections.append(f"""
                            CASE WHEN mask_row_number IS NOT NULL THEN {value} ELSE {col} END AS {col}
                        """)
                    else:
                        projections.append(col)

                mutated_df = filtered_df.project(",".join(projections))

            self.df.df = mutated_df
        else:
            return None


class DuckSeries:
    def __init__(self, parent: duckdb.DuckDBPyRelation, col: str, filter: str = None):
        self.parent = parent
        self.col = col
        self.filter = filter

    @property
    def shape(self):
        return self.compute().shape

    @property
    def _col_or_expr(self):
        if self.filter:
            return self.filter
        return self.col

    def _comp(self, op: str, other) -> "DuckSeries":
        if type(other) == DuckSeries:
            other = other.col
        elif type(other) == str:
            escaped = other.replace("'", "\\'")
            other = f"'{escaped}'"

        return DuckSeries(self.parent, self.col, f"({self._col_or_expr}) {op} {other}")

    def __gt__(self, other):
        return self._comp(">", other)

    def __ge__(self, other):
        return self._comp(">=", other)

    def __lt__(self, other):
        return self._comp("<", other)

    def __le__(self, other):
        return self._comp("<=", other)

    def __eq__(self, other):
        return self._comp("=", other)

    def __ne__(self, other):
        return self._comp("!=", other)

    def __and__(self, other):
        return self._comp("AND", other)

    def __or__(self, other):
        return self._comp("OR", other)

    def __add__(self, other):
        return self._comp("+", other)

    def __sub__(self, other):
        return self._comp("-", other)

    def __truediv__(self, other):
        return self._comp("/", other)

    def __mul__(self, other):
        return self._comp("*", other)

    def __invert__(self):
        return DuckSeries(self.parent, self.col, f"NOT ({self._col_or_expr})")

    def isin(self, other):
        if type(other) == DuckSeries:
            other_sql = other.compute().sql_query()
            return DuckSeries(self.parent, self.col, f"({self._col_or_expr}) IN ({other_sql})")
        elif type(other) in (pd.Series, list) or isinstance(other, np.ndarray):
            wrapped = pd.DataFrame({"isin_col": other})
            wrapped_id = "temp_" + str(id(wrapped))
            db.register(wrapped_id, wrapped)
            return DuckSeries(self.parent, self.col,
                              f"({self._col_or_expr}) IN (SELECT isin_col FROM {wrapped_id})")
        raise NotImplementedError(
            "isin only supports other DuckSeries objects, lists, pandas Series or numpy arrays")

    def isna(self, other):
        return DuckSeries(self.parent, self.col, f"({self._col_or_expr}) IS NULL")

    def compute(self) -> duckdb.DuckDBPyRelation:
        return self.parent.project(f"({self._col_or_expr}) AS {self.col}")

    def copy(self) -> "DuckSeries":
        return DuckSeries(self.parent, self.col, self.filter)

    def __str__(self):
        return self.compute().__str__()

    def __repr__(self):
        return self.compute().__repr__()


class DuckDF:
    def __init__(self, df: duckdb.DuckDBPyRelation):
        self.df = df

    @property
    def loc(self):
        return DuckIndexer(self)

    def assign(self, **cols):
        curr_cols = list(self.df.columns)

        projections = []
        joins = []
        all_cols_order = list(curr_cols)

        for col, value in cols.items():
            if col in curr_cols:
                curr_cols.remove(col)
            else:
                all_cols_order.append(col)

            if type(value) == DuckSeries:
                projections.append(f"({value._col_or_expr}) AS {col}")
            elif type(value) == str:
                escaped = value.replace("'", "\\'")
                projections.append(f"'{escaped}' AS {col}")
            elif hasattr(value, "__len__"):
                if len(value) != self.df.shape[0]:
                    raise RuntimeError(
                        f"Length mismatch between dataframe and assigned column: {len(value)} != {self.df.shape[0]}")

                wrapped = pd.DataFrame({col: value})
                wrapped_id = "temp_" + str(id(wrapped))
                db.register(wrapped_id, wrapped)

                joins.append(
                    f"(SELECT row_number() OVER () AS row_number, {col} FROM {wrapped_id}) ON (main.row_number = {wrapped_id}.row_number)")
            else:
                projections.append(f"{value} AS {col}")
        main_table_query = self.df.sql_query()

        use_comma = bool(curr_cols) or bool(projections)

        q = f"""
            SELECT {','.join(all_cols_order)} 
            FROM (
                SELECT {','.join(curr_cols + projections)} {"," if use_comma else ""} row_number() OVER () AS row_number 
                FROM ({main_table_query})
            ) AS main
        """

        if joins:
            q += " LEFT JOIN " + " LEFT JOIN ".join(joins)

        # print(q)

        return DuckDF(db.sql(q))

    def __setitem__(self, key: str, value):
        self.df = self.assign(**{key: value}).df

    def __str__(self):
        return self.df.__str__()

    def __repr__(self):
        return self.df.__repr__()

    def __getitem__(self, item):
        if type(item) == str:
            return DuckSeries(self.df, item)

        raise NotImplementedError()

    @property
    def shape(self):
        return self.df.shape

    def astype(self):
        pass

    def limit(self, n_rows, offset=0):
        return DuckDF(self.df.limit(n_rows, offset))

    def copy(self) -> "DuckDF":
        return DuckDF(self.df)

    def abs(self) -> "DuckDF":
        return self._project_all_cols("ABS")

    def _project_all_cols(self, fun_name: str) -> "DuckDF":
        projections = []
        for col in self.df.columns:
            projections.append(f"{fun_name}({col}) AS {col}")

        return DuckDF(self.df.project(",".join(projections)))

    def to_pandas(self, *, date_as_object: bool = False) -> pd.DataFrame:
        return self.df.to_df(date_as_object=date_as_object)

    def to_csv(
        self, file_name: str, *, sep: Optional[str] = None, na_rep: Optional[str] = None,
        header: Optional[bool] = None, quotechar: Optional[str] = None,
        escapechar: Optional[str] = None,
        date_format: Optional[str] = None, timestamp_format: Optional[str] = None,
        quoting: Union[str, int, None] = None,
        encoding: Optional[str] = None, compression: Optional[str] = None
    ) -> None:
        self.df.to_csv(
            file_name=file_name,
            sep=sep,
            na_rep=na_rep,
            header=header,
            quotechar=quotechar,
            escapechar=escapechar,
            date_format=date_format,
            timestamp_format=timestamp_format,
            quoting=quoting,
            encoding=encoding,
            compression=compression,
        )

    def to_parquet(self, file_name: str, compression: Optional[str]) -> None:
        self.df.to_parquet(file_name=file_name, compression=compression)

    def to_table(self, table_name: Optional[str] = None) -> "DuckDF":
        if table_name is None:
            table_name = f"generated_table_{id(self.df)}"

        self.df.to_table(table_name)
        return DuckDF(db.table(table_name))

    @staticmethod
    def read_parquet(path: str) -> "DuckDF":
        return DuckDF(db.read_parquet(path))


df = DuckDF.read_parquet("../medium_embeddings.parquet").limit(1000)
# df = df.limit(1000)

# df.loc[:, "dim_1"] = 1

import code;

code.interact(local=locals())

"""
SELECT 
    dim_1, 
    row_number, 
    CASE 
        WHEN dim_1 > 0 
        THEN row_number() OVER (PARTITION BY dim_1 > 0) 
        ELSE NULL 
    END AS part_num 
FROM 
    (
        SELECT 
            row_number() OVER () AS row_number, * 
        FROM 
            test
    )     
ORDER BY row_number

"""

"""
SELECT
    ingredient_ID,ingredient_name,value_series.ingredient_id AS dim_1,dim_2,dim_3,dim_4,dim_5,dim_6,dim_7,dim_8,dim_9,dim_10,dim_11,dim_12,dim_13,dim_14,dim_15,dim_16
                    FROM 
                        (SELECT *, row_number AS mask_row_number FROM (SELECT *, row_number() OVER () AS row_number FROM (SELECT * FROM parquet_scan('medium_embeddings.parquet', (binary_as_string = false), (file_row_number = false), (filename = false), (hive_partitioning = false), (union_by_name = false)) LIMIT 1000) AS parquet_5b95be6db18d8729) AS parquet_5b95be6db18d8729) AS main
                        LEFT JOIN
                        (
                            SELECT row_number() OVER () AS row_number, ingredient_id 
                            FROM SELECT ingredient_id AS ingredient_id FROM (SELECT * FROM parquet_scan('medium_embeddings.parquet', (binary_as_string = false), (file_row_number = false), (filename = false), (hive_partitioning = false), (union_by_name = false)) LIMIT 1000) AS parquet_5b95be6db18d8729
                        ) AS value_series 
                        ON 
                            (main.mask_row_number = value_series.row_number)
"""