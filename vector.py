import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

class RAGRetriever:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self.employee_texts = self.df.apply(self._convert_to_text, axis=1).tolist()
        self._build_index()

    def _convert_to_text(self, row):
        return f"{row['name']} has {row['experience_years']} years experience, skilled in {', '.join(eval(row['skills']))}, worked on {', '.join(eval(row['past_projects']))}, currently {row['availability']}."

    def _build_index(self):
        embeddings = self.model.encode(self.employee_texts)
        self.dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(np.array(embeddings))

    def search(self, query, top_k=5):
        query_vec = self.model.encode([query])
        D, I = self.index.search(np.array(query_vec), top_k)
        return [self.df.iloc[i] for i in I[0]]
