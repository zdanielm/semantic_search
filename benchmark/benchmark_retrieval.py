import numpy as np
import polars as pl
from trulens.core import Feedback
from trulens.core.utils.serial import Lens
from trulens.providers.openai import OpenAI

from utilities.setup import load_config

config = load_config()

def evaluate_retrieval(query, chunk_table, embedding_model, search_function):

    openai = OpenAI(api_key=config['openai_api_key'])


    retrieved_text_df = search_function(query, chunk_table, embedding_model)

    chunk_texts = list(retrieved_text_df['chunk_text'])
    retrieved_text_ids = list(retrieved_text_df['patent_number'])


    f_context_relevance = (
        Feedback(openai.context_relevance)
        .on_input()
        .on(Lens().text)
        .aggregate(np.mean)
    )

    context_relevance = f_context_relevance(
        question=query,
        context=chunk_texts
    )

    return {
        'retrieved_text_ids': retrieved_text_ids,
        'chunk_texts': chunk_texts,
        'context_relevance': context_relevance,
    }
