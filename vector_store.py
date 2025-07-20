import faiss
import numpy as np

index = None
texts = []

def build_index(embedded_texts, original_texts):
    global index, texts
    texts = original_texts
    dimension = len(embedded_texts[0])
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embedded_texts).astype("float32"))

def search(query_embedding, k=3):
    D, I = index.search(np.array([query_embedding]).astype("float32"), k)
    return [texts[i] for i in I[0]]
