import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

metadata = sa.MetaData(schema="tenant")
Base = declarative_base(metadata=metadata)


class Tenant(Base):
    __tablename__ = "tenant"

    id = sa.Column("id", sa.Integer, primary_key=True, nullable=False)
    name = sa.Column("name", sa.String(256), nullable=False, index=True, unique=True)
    schema = sa.Column("schema", sa.String(256), nullable=False, unique=True)
    host = sa.Column("host", sa.String(256), nullable=False, unique=True)

    __table_args__ = ({"schema": "shared"},)


def get_shared_metadata():
    meta = sa.MetaData()
    for table in Base.metadata.tables.values():
        if table.schema != "tenant":
            table.tometadata(meta)
    return meta