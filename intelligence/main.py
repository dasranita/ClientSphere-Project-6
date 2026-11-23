from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
app=FastAPI(title="ClientSphere Sales Intelligence")
class Lead(BaseModel):
    name:str
    email:str|None=None
    company:str|None=None
    engaged:bool=False
    budget:float=Field(default=0,ge=0)
class Opportunity(BaseModel):
    amount:float=Field(ge=0)
    probability:float=Field(ge=0,le=1)
@app.get('/health')
def health():return {'ok':True}
@app.post('/score')
def score(lead:Lead):
    factors={'email':15 if lead.email else 0,'company':20 if lead.company else 0,'engaged':35 if lead.engaged else 0,'budget':30 if lead.budget>=1000 else 0}
    return {'score':sum(factors.values()),'factors':factors}
@app.post('/forecast')
def forecast(items:List[Opportunity]):return {'weighted_forecast':round(sum(x.amount*x.probability for x in items),2),'count':len(items)}
