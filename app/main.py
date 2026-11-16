from fastapi import FastAPI

app = FastAPI(title="Drill Sergeant")


@app.get("/health")
def health():
    return {"ok": True}