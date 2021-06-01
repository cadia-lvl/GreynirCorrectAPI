#!/usr/bin/env python


from typing import Optional
from fastapi import FastAPI
from fastapi.responses import Response, JSONResponse, HTMLResponse

from reynir_correct import check_single
from reynir_correct import tokenize

__version__ = 0.1


app = FastAPI()


def _err(msg: str) -> JSONResponse:
    return JSONResponse(content={"err": True, "errmsg": msg})


@app.get("/", response_class=HTMLResponse)  # type: ignore
def root() -> str:
    return """
<html>
    <head><title>GreynirCorrect API Server v{0}</title></head>
    <body>
        <h1>GreynirCorrect API Server v{0}</h1>
        <ul><li><a href="/docs">Documentation</a></li></ul>
    </body>
</html>
""".format(
        __version__
    )

@app.get("/spellchecker/tokens")
def tokens(text : str):
    g = tokenize(text)
    out = []
    for tok in g:
        out += [[tok.txt, tok.error_description]]
    return JSONResponse(content=out)
        

@app.get("/spellchecker/full")
def full(text: str, annotations : Optional[bool] = False):
    sent = check_single(text)
    if annotations:
        return JSONResponse(content=[sent.tidy_text, [str(ann) for ann in sent.annotations]])
    else: 
        return JSONResponse(content=sent.tidy_text)
