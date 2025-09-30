from fastapi import FastAPI, HTTPException
from sentientresearchagent import SentientAgent

app = FastAPI()


@app.get("/")
async def get_story():
    try:
        agent = SentientAgent.create()
        story = await agent.run("Give me a creative story starter in 2 sentences")
        return {"story": story}
    except Exception as exc:
        # Surface a clean error to the client
        raise HTTPException(status_code=500, detail=str(exc))


