from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient

client = MongoClient('mongodb+srv://which-img:cialabsintern@atlascluster.mytwvuv.mongodb.net/')
db = client['which-img']
collection = db['feedback']

app = FastAPI()

class Feedback(BaseModel):
    modelName : str
    image: str
    result: str


@app.get("/")
def read_root():
    return {"message": "This is home"}

@app.post("/feedback/")
async def create_feedback(feedback: Feedback):
    feedback_id = collection.insert_one(feedback.dict()).inserted_id
    return {"message": "Feedback submitted successfully", "feedback_id": str(feedback_id)}
