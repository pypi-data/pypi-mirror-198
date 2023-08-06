from sqlalchemy import create_engine, MetaData, schema


class DB2Mermaid:

    def __init__(self):
        self.user = "user"
        self.password = "password"
        self.host = "host"
        self.port = "3306"
        self.db_name = "db_name"

    def init_db(self, user, password, host, port, db_name):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.db_name = db_name
        self.db_url = f"mysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"
        print("db_url: ", self.db_url)
        engine = create_engine(self.db_url)
        self.meta = MetaData()
        self.meta.reflect(bind=engine)

    def _write_texts(self, lines: list[str]):
        f = open('er.md', 'a', encoding='UTF-8')
        f.writelines(lines)
        f.close()

    def _init_text(self):
        self._write_texts(["```mermaid\n", "erDiagram\n"])

    def _close_text(self):
        self._write_texts(["```"])

    def create_row_per_column(self, column_data: schema.Column) -> str:
        """_summary_

        Args:
            column_data (sqlalchemy.schema.Column): Column data which contains name, type, autoincrement,
            default, nullable, primary_key, foreign_key, index, comment

        Returns:
            str: string of column data for mermaid erDiagram row
        """

        if "COLLATE" in str(column_data.type):
            column_data.type = str(column_data.type).split(" ")[0]
        if "DECIMAL" in str(column_data.type):
            # avoid mermaid incorrect format in DECIMAL
            column_data.type = str(column_data.type).replace(', ', '_')
        er_row = f"        {column_data.type} {column_data.name}"
        if column_data.primary_key:
            er_row += " PK"
            return er_row + "\n"
        elif column_data.foreign_keys:
            er_row += " FK"
            return er_row + "\n"
        else:
            return er_row + "\n"

    def generate(self):
        self._init_text()

        for n, t in self.meta.tables.items():
            texts: list[str] = []
            texts.append("    " + n + "{\n")
            print("table name🌟", n)
            for c in t.columns.values():
                texts.append(self.create_row_per_column(c))
            texts.append("}\n")
            self._write_texts(texts)

        self._close_text()


if __name__ == "__main__":
    d = DB2Mermaid()
    d.init_db("root", "pass", "127.0.0.1", "3308", "sakila")
    d.generate()
