from fastapi import FastAPI

# objeto app, instanciando pelo fastapi.
app = FastAPI(
    title = "Pamps",
    versin = "0.1.0",
    description = "Pamps is a posting app"
)

@app.get('/')
async def index():
    return {"first":"API"}

@app.get('/home')
async def index():
    return {"Home":"Construindo uma API do ZERO"}
