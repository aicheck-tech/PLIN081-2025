from fastapi import FastAPI, Query

from reviews.text_utils import is_anagram, pluralize, reverse

app = FastAPI()

@app.post("/anagram")
def check_anagram(word1: str = Query(...), word2: str = Query(...)):
    return {"originals": [word1, word2], "is_anagram": is_anagram(word1, word2)}


@app.post("/reverse")
def reverse_case(word: str = Query(...)):
    return {"original": word, "reversed": reverse(word)}


@app.post("/pluralize")
def word_frequency(word: str = Query(...)):
    return {"original": word, "plural": pluralize(word)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
