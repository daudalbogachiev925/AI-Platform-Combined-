from openai import OpenAI
client = OpenAI()

ROUTES = {
    "sql":    "Сгенерируй SQL-запрос...",
    "rag":    "Ответь по документации...",
    "doc":    "Создай документ 1С...",
    "report": "Сформируй отчёт...",
}

def route(user_msg: str) -> str:
    prompt = f"Классифицируй: {user_msg}\nКатегории: sql, rag, doc, report"
    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}])
    return r.choices[0].message.content.strip()
