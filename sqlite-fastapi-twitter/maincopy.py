from fastapi import FastAPI, Depends, HTTPException, Path, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from sqlmodel import Field, Session, SQLModel, create_engine, select

# Database tables
# BaseModel -> SQLModel -> TweetBase
class TweetBase(SQLModel): # SQLModel also happens to be a BaseModel, user passes in TweetBase
    username: str = Field(description="The person who created the tweet")
    content: str = Field(max_length=300, description="The content of the tweet must be under 300 characters")
    likes: int = Field(default=0, ge=0, description="The number of likes of the tweet will initially be set to 0")
    timestamp: str = Field(description="The time and date of the tweet's creation")

class Tweet(TweetBase, table=True): # I return Tweet
    id: int | None = Field(default=None, primary_key=True) # Field can let you specify certain things about the columns


# Setting up to connect to the database
# This stuff is just required for the engine to run
sqlite_database_name = "twitter.db"
sqlite_url = f"sqlite:///{sqlite_database_name}"

# Allowing connections from multiple threads
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
# Creating the session, the session communicates with the database
def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    
# Django -> backend ----> HTML CSSS

# One backend, one frontend, running on two different servers, they're commmunicating with eachother
# Front developers -> frontend, backend developers -> backend 

@app.get("/tweets")
async def get_tweets(
    session: SessionDep, 
    limit: Annotated[int|None, Query(gt=0, description="The number of results you would like to return")] = None
    ):
    if not limit:
        return session.exec(select(Tweet)).all()
    else:
        return session.exec(select(Tweet)).fetchmany(limit)

@app.post("/tweets/new", response_model=Tweet)
async def post_tweets(tweet: TweetBase, session: SessionDep):
    db_tweet = Tweet.model_validate(tweet) # creates an ID 
    session.add(db_tweet)
    session.commit()
    session.refresh(db_tweet)
    return db_tweet

@app.delete("/tweets/{tweet_id}")
def delete_tweet(tweet_id: Annotated[int, Path(ge=0)], session: SessionDep):
    tweet = session.get(Tweet, tweet_id)
    if not tweet:
        raise HTTPException(status_code=404, detail="Tweet not found")
    session.delete(tweet)
    session.commit()
    return {"ok": True}
