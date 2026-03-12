import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

documents = [

"""
Table students
columns: id, name, age, marks, department
""",

"""
Table departments
columns: dept_code, dept_name, hod, building
relationship:
students.department = departments.dept_code
"""
]

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(documents)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))