from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Literal,Annotated
import pickle
import pandas as pd


# import the model
import joblib
try:
    model = joblib.load("insurance_premium_prediction.pkl")
    print("Model loaded successfully")
except Exception as e:
    print(f"Model loading error: {e}")



app = FastAPI()

tier_1_cities = ['Mumbai','Delhi','Bangalore','Chennai','Kolkata','Hyderabad','Pune']
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]

# pydantic model to validate incomming data

class UserInput(BaseModel):

    age:Annotated[int,Field(...,gt=0,lt=120,description='age of the user')]
    weight:Annotated[float,Field(...,gt=0,description='weight of the user')]
    height:Annotated[float,Field(...,gt=0,lt=2.5,description='height of the user')]
    income_lpa:Annotated[float,Field(...,gt=0,description='income of the user')]
    smoker:Annotated[bool,Field(...,description='if the user smoker')]
    city:Annotated[str,Field(...,description='the city  of the user')]
    occupation:Annotated[Literal['retired', 'freelancer', 'student', 'government_job','business_owner', 'unemployed', 'private_job'],Field(...,description='occuption  of the user')]

    @computed_field
    @property
    def bmi(self)->float:
        return self.weight/(self.height**2)
    
    @computed_field
    @property
    def lifestyle_risk(self) ->str:
        if self.smoker and self.bmi > 30:
            return 'High'
        elif self.smoker and self.bmi > 27:
            return 'Medium'
        else:
            return 'low'
        
    @computed_field
    @property
    def age_group(self)-> str:
        if self.age < 25:
            return 'young'
        elif self.age <45:
            return 'adult'
        elif self.age < 60:
            return 'middle_aged' 
        return 'Senior'
    
    @computed_field
    @property
    def city_tier(self)->int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3

@app.get("/")
def welcome():
    return {"message": "Welcome to the Insurance Premium Prediction API"}


@app.post('/predict')
async def predict(data: UserInput):
    print("Received Data:", data.dict())  # Debugging step
    
    input_df = pd.DataFrame([{
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }])

    prediction = model.predict(input_df)[0]
    return JSONResponse(status_code=200, content={'predicted_category': prediction})
