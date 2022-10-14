from fastapi import FastAPI, Request ,Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse, JSONResponse

#from emp_dao import EmpDao

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
@app.get("/zzang", response_class=HTMLResponse)
async def selects(request: Request):
    return templates.TemplateResponse("zzang.html", {"request": request})


#uvicorn myajax:app --reload