from playhouse.postgres_ext import (
    AutoField,
    ForeignKeyField,
    Model,
    PostgresqlExtDatabase,
    TextField,
    TSVectorField,
)
from pgvector.peewee import VectorField
from utilities.setup import load_config

database_config = load_config()

database_driver = PostgresqlExtDatabase(
    database_config['db_name'],
    host=database_config['db_host'],
    port=database_config['db_port'],
    user=database_config['db_user'],
    password=database_config['db_password']
)

def create_tables():
    """
    Create all tables in the database, if they don't already exist.

    This is a utility function to simplify the process of creating all the tables
    at once.

    The tables that are created are those defined by the `Patent` model and its
    various chunking/embedding methods.
    """
    with database_driver:
        Patent.create_table()
        minilm_noverlap.create_table()
        minilm_recursive.create_table()
        minilm_sliding.create_table()
        arctic_noverlap.create_table()
        arctic_recursive.create_table()
        arctic_sliding.create_table()


class BaseModel(Model):
    """
    Base class for all models, specifying the database driver
    """
    class Meta:
        database = database_driver

# Main class
class Patent(BaseModel):
    """
    Main class, storing data
    """
    patent_number = TextField()
    section = TextField()
    raw_text = TextField()
    search_vector = TSVectorField(null=True)

    class Meta:
        table_name = 'patents'

# Chunk tables (separate tables for ease of evaluation)
class minilm_noverlap(BaseModel):
    """
    Text chunks, embedded with MiniLM and chunked with no overlap method
    """
    id = AutoField()
    patent_number = ForeignKeyField(Patent)
    chunk_text = TextField()
    embedding = VectorField(dimensions=384)

    class Meta:
        table_name = 'minilm_noverlap'

class minilm_recursive(BaseModel):
    """
    Text chunks, embedded with MiniLM and chunked with recursive method
    """
    id = AutoField()
    patent_number = ForeignKeyField(Patent)
    chunk_text = TextField()
    embedding = VectorField(dimensions=384)

    class Meta:
        table_name = 'minilm_recursive'

class minilm_sliding(BaseModel):
    """
    Text chunks, embedded with MiniLM and chunked with sliding window method
    """
    id = AutoField()
    patent_number = ForeignKeyField(Patent)
    chunk_text = TextField()
    embedding = VectorField(dimensions=384)

    class Meta:
        table_name = 'minilm_sliding'

class arctic_noverlap(BaseModel):
    """
    Text chunks, embedded with Arctic Embed M and chunked with no overlap method
    """
    id = AutoField()
    patent_number = ForeignKeyField(Patent)
    chunk_text = TextField()
    embedding = VectorField(dimensions=768)

    class Meta:
        table_name = 'arctic_noverlap'

class arctic_recursive(BaseModel):
    """
    Text chunks, embedded with Arctic Embed M and chunked with recursive method
    """
    id = AutoField()
    patent_number = ForeignKeyField(Patent)
    chunk_text = TextField()
    embedding = VectorField(dimensions=768)

    class Meta:
        table_name = 'arctic_recursive'

class arctic_sliding(BaseModel):
    """
    Text chunks, embedded with Arctic Embed M and chunked with sliding window method
    """
    id = AutoField()
    patent_number = ForeignKeyField(Patent)
    chunk_text = TextField()
    embedding = VectorField(dimensions=768)

    class Meta:
        table_name = 'arctic_sliding'
