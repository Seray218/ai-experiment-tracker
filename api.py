from fastapi import FastAPI,HTTPException
from pydantic import BaseModel, ConfigDict, Field
from typing import Literal, Optional,List
from uuid import UUID,uuid4

api=FastAPI()

class ExperimentCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    model_name:str=Field(min_length=2)
    dataset:str=Field(min_length=2)
    accuracy:Optional[float]=Field(default=None,ge=0.0,le=1.0)
    status:Literal["pending", "running", "completed", "failed"] = "pending"


class Experiment(ExperimentCreate):
    id:UUID=Field(default_factory=uuid4)

class ExperimentUpdate(BaseModel):
    model_name:Optional[str]=Field(default=None,min_length=2)
    dataset:Optional[str]=Field(default=None,min_length=2)
    accuracy:Optional[float]=Field(default=None,ge=0.0,le=1.0)
    status:Optional[Literal["pending", "running", "completed", "failed"]]=None

experiments=[]

@api.post("/experiments/",response_model=Experiment)
def add_experiment(experiment:ExperimentCreate):
    new_experiment = Experiment(**experiment.model_dump())
    experiments.append(new_experiment)
    return new_experiment


@api.get("/experiments/",response_model=List[Experiment])
def get_experiments():
    return experiments

@api.get("/experiments/{experiment_id}",response_model=Experiment)
def get_experiment(experiment_id:UUID):
    for experiment in experiments:
        if experiment.id==experiment_id:
            return experiment
    raise HTTPException(status_code=404,detail="Experiment not found")

@api.patch("/experiments/{experiment_id}",response_model=Experiment)
def update_experiment(experiment_id:UUID,experiment_update:ExperimentUpdate):
    for idx,experiment in enumerate(experiments):
        if experiment.id==experiment_id:
            updated_experiment=experiment.model_copy(update=experiment_update.model_dump(exclude_unset=True))
            experiments[idx]=updated_experiment
            return updated_experiment
    raise HTTPException(status_code=404,detail="Experiment not found")

@api.delete("/experiments/{experiment_id}",response_model=Experiment)
def delete_experiment(experiment_id:UUID):
    for idx,experiment in enumerate(experiments):
        if experiment.id==experiment_id:
            return experiments.pop(idx)
    raise HTTPException(status_code=404,detail="Experiment not found")

if __name__=="__main__":
    import uvicorn
    uvicorn.run(api,host="0.0.0.0",port=8000)