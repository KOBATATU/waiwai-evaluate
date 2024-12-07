
from fastapi import FastAPI, Header, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import models, database, schemas
from sqlalchemy.future import select
from gcs import read_csv_from_gcs
from evaluate import metrics

app = FastAPI(docs_url=None, redoc_url=None)

@app.post("/evaluate/")
async def evaluate(
    request: schemas.EvaluateRequest,
    session_id: str = Header(...),
    db: AsyncSession = Depends(database.get_db)
):
    
    
    async with db.begin():
        session = await db.execute(select(models.Session).where(models.Session.sessionToken == session_id))
        
        session = session.scalar_one_or_none()
        if session is None:
            raise HTTPException(status_code=404, detail="session not found")

        competition = await db.execute(select(models.Competition).where(models.Competition.id == request.competition_id))
        competition = competition.scalar_one_or_none()
        if competition is None:
            raise HTTPException(status_code=404, detail="competition not found")

        if competition.evaluation_func not in metrics:
            raise HTTPException(status_code=400, detail="competition not evaluation")

        try:
            object_path = f'competitions/{request.competition_id}/submission/{session.userId}/{request.object_path}'
            expect_df = read_csv_from_gcs(object_path)
            
            object_path = f'competitions/{request.competition_id}/answer/answer.csv'
            answer_df = read_csv_from_gcs(object_path)

            public_indices = answer_df.index[answer_df['is_public_score'] == 1].tolist()
            public_answer_df = answer_df.loc[public_indices]
            public_expect_df = expect_df.loc[public_indices]
            public_value = metrics[competition.evaluation_func](public_expect_df['expect'], public_answer_df['answer'])

            private_value = metrics[competition.evaluation_func](expect_df['expect'], answer_df['answer'])
            return {"public_score": public_value, "private_score": private_value}

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")