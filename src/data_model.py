from pydantic import BaseModel

"""""
Pydantic is a Python library used for data validation and parsing. 
It's particularly useful for defining and validating data models and is often used in the context of data serialization, 
such as when dealing with data sent over APIs or when reading and writing data to and from databases."

"""
from typing import Optional

class InputDataModel(BaseModel):
	age: float
	sex: int
	chest_pain_type: int
	resting_bp: float
	cholestoral: float
	fasting_blood_sugar: float
	restecg: int
	max_hr: float
	exang: int
	oldpeak: float
	slope: int
	num_major_vessels: int
	thal: int
	
class OutputDataModel(BaseModel):
    predicted_value: bool
    predicted_class: str
