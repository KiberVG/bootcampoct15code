from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from sqlmodel import Field, Session, SQLModel, create_engine, select

# Database tables
class TweetBase(SQLModel):
    username: str
    content: str
    likes: int
    timestamp: str

class Tweet(TweetBase, table=True):
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
    

@app.get("/tweets")
async def get_tweets(session: SessionDep):
    return session.exec(select(Tweet)).all()

@app.post("/tweets/new", response_model=Tweet)
async def post_tweets(tweet: TweetBase, session: SessionDep):
    db_tweet = Tweet.model_validate(tweet)
    session.add(db_tweet)
    session.commit()
    session.refresh(db_tweet)
    return db_tweet

@app.delete("/tweets/{tweet_id}")
def delete_tweet(tweet_id: int, session: SessionDep):
    tweet = session.get(Tweet, tweet_id)
    if not tweet:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(tweet)
    session.commit()
    return {"ok": True}