from fastapi import FastAPI, UploadFile, Form
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Sales Insight API running"}

@app.post("/analyze")
async def analyze(file: UploadFile, email: str = Form(...)):
    
    df = pd.read_csv(file.file)

    total_sales = df["Revenue"].sum()

    summary = f"""
    Sales Summary

    Total Revenue: {total_sales}
    Total Records: {len(df)}

    Electronics appear to be a major contributor.
    """

    return {
        "email": email,
        "summary": summary
    }