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
        """Load both OBD codes and complaints"""
        with open('complaints.json') as f:
            self.complaints = json.load(f)['complaints']
        
        # Your existing OBD codes
        self.codes = {
            "P0300": {
                "description": "Random/Multiple Cylinder Misfire",
                "severity": "High",
                "causes": ["Faulty spark plugs", "Vacuum leaks"],
                "fixes": ["Replace spark plugs", "Check intake system"]
            }
        }
    
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
