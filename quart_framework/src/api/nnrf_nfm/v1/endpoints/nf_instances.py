from app import app, request
from quart import jsonify
from src.crud.crud_nf_instance import *


@app.put("/nnrf-nfm/v1/nf-instances/<nfInstanceId>")
async def nf_register(nfInstanceId):
    return jsonify(create_nf_instance(nf_profile=await request.get_json(), nfInstanceId=nfInstanceId))

@app.delete("/nnrf-nfm/v1/nf-instances/<nfInstanceId>")
async def nf_deregister(nfInstanceId):
    return jsonify(delete_nf_instance(nfInstanceId=nfInstanceId))

@app.get("/nnrf-nfm/v1/nf-instances/<nfInstanceId>")
async def nf_read(nfInstanceId):
    nf_prf = get_nf_instance(nfInstanceId= nfInstanceId)
    if nf_prf != None:
        nf_prf["_id"] = str(nf_prf["_id"])
        return nf_prf
    return None

@app.patch("/nnrf-nfm/v1/nf-instances/<nfInstanceId>")
async def nf_update(nfInstanceId):
    return jsonify(modify_nf_instance(nfInstanceId=nfInstanceId, update_values=await request.get_json()))

@app.get("/nnrf-nfm/v1/nf-instances")
async def nf_discovery():
    