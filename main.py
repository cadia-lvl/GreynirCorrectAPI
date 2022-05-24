#!/usr/bin/env python


from typing import Optional
from fastapi import FastAPI
from fastapi.responses import Response, JSONResponse, HTMLResponse

from pydantic import BaseModel
from typing import Optional

from reynir_correct import check
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

class SpellcheckInput(BaseModel):
    type: Optional[str] = "text"
    content: str

@app.post("/spellchecker")
def spellcheck(text: SpellcheckInput):
    g = list(check(text.content))[0]
    resp = []
    for sentence in g.sentences():
        texts = []
        for token in sentence.tokens:
            texts.append({'content':token.txt})
    
        annotation = []
        for ann in sentence.annotations:
            ann = str(ann)
            start = int(ann[:3])
            end = int(ann[4:7])+1
            annotation.append({"start": start, "end":end, "features":{"correction":ann[9:]}})
        resp.append({'type': 'texts', 'texts': texts,"annotations":{"corrections":annotation}})
    return JSONResponse(content={"response":{"type":"texts", 'texts':resp}})

