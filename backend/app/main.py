from fastapi import FastAPI
from app.services.data_loader import load_locations, load_tags
from app.routes import recommend
from app.routes.testing import router as testing_router
from app.routes.bulk_testing import router as bulk_testing_router



app = FastAPI()

locations = load_locations()
tags = load_tags()

app.include_router(recommend.router, prefix="/api")
app.include_router(testing_router, prefix="/api")
app.include_router(bulk_testing_router, prefix="/api")


@app.get("/health")
def health():
    return {"status": "NearNow backend is running"}

@app.get("/data-check")
def data_check():
    return {
        "locations_loaded": len(locations),
        "tags_loaded": len(tags)
    }
