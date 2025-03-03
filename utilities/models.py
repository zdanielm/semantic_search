from playhouse.postgres_ext import *
from utilities.setup import load_config

#db_config = load_config()

#da_driver = PostgresqlExtDatabase(db_config['database'], host=db_config['host'], port=db_config['port'], user=db_config['user'], password=db_config['password'])

# Main class
class Patent(Model):
    """
    Main class, storing data
    """
    patent_number = TextField()
    section = TextField()
    raw_text = TextField()
    search_vector = TSVectorField(null=True)

    class Meta:
        database = db

# Chunk tables (separate tables for ease of evaluation)
class minilm_noverlap(Model):
    """
    Text chunks, embedded with MiniLM and chunked with no overlap method
    """
    id = AutoField()
    patent_number = ForeignKeyField(Patent)
    chunk_text = TextField()

    class Meta:
        database = db

class minilm_recursive(Model):
    """
    Text chunks, embedded with MiniLM and chunked with recursive method
    """
    id = AutoField()
    patent_number = ForeignKeyField(Patent)
    chunk_text = TextField()

    class Meta:
        database = db

class minilm_sliding(Model):
    """
    Text chunks, embedded with MiniLM and chunked with sliding window method
    """
    id = AutoField()
    patent_number = ForeignKeyField(Patent)
    chunk_text = TextField()

    class Meta:
        database = db

class arctic_noverlap(Model):
    """
    Text chunks, embedded with Arctic Embed M and chunked with no overlap method
    """
    id = AutoField()
    patent_number = ForeignKeyField(Patent)
    chunk_text = TextField()

    class Meta:
        database = db

class arctic_recursive(Model):
    """
    Text chunks, embedded with Arctic Embed M and chunked with recursive method
    """
    id = AutoField()
    patent_number = ForeignKeyField(Patent)
    chunk_text = TextField()

    class Meta:
        database = db

class arctic_sliding(Model):
    """
    Text chunks, embedded with Arctic Embed M and chunked with sliding window method
    """
    id = AutoField()
    patent_number = ForeignKeyField()
    chunk_text = TextField()

    class Meta:
        database = db
