import numpy as np
from rag.vector_store import model, index, documents

def retrieve_context(question):

    q_embed = model.encode([question])

    distances, indices = index.search(np.array(q_embed), 2)

    context = ""

    for i in indices[0]:
        context += documents[i] + "\n"

    return context