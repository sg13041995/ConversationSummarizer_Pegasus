from fastapi import FastAPI
import uvicorn
import os
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from TextSummarizer.pipeline.prediction import PredictionPipeline


text:str = "What is Text Summarization?"

app = FastAPI()

# Home page
@app.get("/", tags=["authentication"])
async def index():
    # Redirects to "/docs"
    # "/docs" is fast api ui
    return RedirectResponse(url="/docs")


# Training route
@app.get("/train")
async def training():
    try:
        # os.system can run any command
        # to train the command is => python main.py
        # Run the main.py file
        os.system("python main.py")

        # If training was successful
        return Response("Training successful !!")

    except Exception as e:
        # If training failed
        return Response(f"Error Occurred! {e}")
    
# Prediction route
@app.post("/predict")
async def predict_route(text):
    try:
        # Initializing prediction pipeline object
        obj = PredictionPipeline()

        # Calling the predict method while passing the text to summarize
        text = obj.predict(text)

        # Returning the summarized text
        return text
    except Exception as e:
        raise e
    

if __name__=="__main__":
    # Launching the server at localhost port 8080
    uvicorn.run(app, host="0.0.0.0", port=8080)