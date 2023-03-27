import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="static/html")
app.mount("/static", StaticFiles(directory="static"))

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/resume")
def get_resume():
    return FileResponse(
        "static/docs/RafaelMoret_CV.pdf", 
        content_disposition_type="inline", 
        filename="RafaelMoret.pdf"
    )

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return FileResponse("static/images/favicon.ico")

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", reload=True)