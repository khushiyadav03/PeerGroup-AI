import pandas as pd
import numpy as np
from faker import Faker
import random

def generate_student_data(n_students=50, seed=42):
    """
    Generates synthetic student data.
    """
    fake = Faker()
    Faker.seed(seed)
    np.random.seed(seed)
    random.seed(seed)

    data = []
    
    learning_styles = ['Visual', 'Auditory', 'Kinesthetic']
    interests = ['Coding', 'Art', 'Sports', 'Music', 'Science']

    for i in range(n_students):
        if i % 10 == 0: print(f"Generating student {i}", flush=True)
        student = {
            'StudentID': fake.uuid4(),
            'Name': fake.name(),
            'Math_Grade': np.random.randint(50, 100),
            'Science_Grade': np.random.randint(50, 100),
            'History_Grade': np.random.randint(50, 100),
            'Learning_Style': random.choice(learning_styles),
            'Personality_Score': np.random.randint(1, 10), # 1 (Introvert) to 10 (Extrovert)
            'Interest': random.choice(interests)
        }
        data.append(student)

    return pd.DataFrame(data)

if __name__ == "__main__":
    df = generate_student_data()
    print(df.head())
    df.to_csv("data/students.csv", index=False)

