def self_correct(sql, error, run_fn, max_iter=3):
    for _ in range(max_iter):
        try:
            return run_fn(sql)
        except Exception as e:
            sql = fix_sql(sql, str(e))
    raise RuntimeError("Не удалось исправить за 3 попытки")

def fix_sql(sql, err):
    from openai import OpenAI
    c = OpenAI()
    r = c.chat.completions.create(
        model="gpt-4o",
        messages=[{"role":"system","content":"Исправь SQL"},
                  {"role":"user","content":f"SQL: {sql}\nОшибка: {err}"}])
    return r.choices[0].message.content
