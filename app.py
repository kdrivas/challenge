from collections import Counter
from fastapi import FastAPI, Request, status, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/', status_code=status.HTTP_201_CREATED)
async def home(request: Request):
  return templates.TemplateResponse('index.html', {'request': request})

@app.post('/', response_class=HTMLResponse, status_code=status.HTTP_201_CREATED)
async def get_max_score(request: Request, word: str = Form(...)):
  # Uppercasing
  word = word.upper()

  # Generate a mapping dictionary with {letter: value}
  mapper = { e[0]:26-ix for ix, e in enumerate(Counter(word).most_common()) }

  # Convert the sequence of letter in a sequence of numbers and sum the sequence
  total = sum(map(lambda x: mapper[x], word))

  return templates.TemplateResponse('result.html', {'request': request, 'result': total})
