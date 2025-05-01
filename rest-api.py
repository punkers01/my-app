from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

# Predefined list of valid user IDs
valid_user_ids = {"user123", "alice", "bob", "charlie"}

@app.get("/check_user/{user_id}")
async def check_user(user_id: str):
    if user_id in valid_user_ids:
        return JSONResponse(status_code=200, content={"message": "User found", "user_id": user_id})
    else:
        raise HTTPException(status_code=404, detail="User not found")
