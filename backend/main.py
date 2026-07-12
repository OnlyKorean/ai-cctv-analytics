from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Supabase
supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

@app.get("/api/stats")
def get_stats():
    data = supabase.table("statistics").select("*").execute()
    return data.data[0] if data.data else {"total_in": 0, "total_out": 0, "current_occupancy": 0}

@app.post("/api/track")
def save_track(tracker_id: int, event_type: str):
    supabase.table("events").insert({
        "tracker_id": tracker_id,
        "event_type": event_type
    }).execute()
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
