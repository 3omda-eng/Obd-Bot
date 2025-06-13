import json
import numpy as np
from sentence_transformers import SentenceTransformer
from typing import Dict, List, Tuple, Optional

class OBDDatabase:
    def __init__(self):
        """Initialize with OBD codes and AI complaint matching"""
        self.model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
        self._load_data()
        self._embed_complaints()

    def _load_data(self):
        """Load OBD codes and Egyptian complaints from external files"""
        with open('complaints.json', encoding='utf-8') as f:
            self.complaints = json.load(f)['complaints']

        with open('codes.json', encoding='utf-8') as f:
            self.codes = json.load(f)['codes']

    def _embed_complaints(self):
        """Generate AI embeddings for all complaints"""
        texts = [f"{c['egyptian']} {c['english']}" for c in self.complaints]
        self.complaint_embeddings = self.model.encode(texts)

    def find_closest_complaint(self, text: str) -> Tuple[Dict, float]:
        """Find most similar complaint using AI"""
        query_embed = self.model.encode(text)
        similarities = np.dot(self.complaint_embeddings, query_embed) / (
            np.linalg.norm(self.complaint_embeddings, axis=1) * np.linalg.norm(query_embed)
        )
        best_idx = np.argmax(similarities)
        return self.complaints[best_idx], float(similarities[best_idx])

    def lookup_code(self, code: str) -> Optional[Dict]:
        """Standard OBD code lookup"""
        return self.codes.get(code.upper())
