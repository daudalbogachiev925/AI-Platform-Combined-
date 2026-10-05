# AI-Platform-Combined

Финальная комбайн-платформа: production-ready AI-система уровня
крупного интегратора 1С. Собирает всё лучшее из проектов 1–34.

## Что внутри
- 5 MCP-серверов (метаданные, SQL, журнал, OData, RAG)
- Router на LLM + LangGraph-агент с self-correction
- RAG по документации 1С и коду
- Skill-система: распознавание счёта, создание документа, генерация отчёта
- FastAPI Gateway
- Prometheus + Evidently для мониторинга
- Docker-compose, GitHub Actions CI, unit-tests

## Архитектура

[User] → [FastAPI] → [Router LLM]
├─→ [MCP: Metadata]
├─→ [MCP: SQL Query]
├─→ [MCP: Journal]
├─→ [MCP: OData]
└─→ [MCP: RAG]
↓
[LangGraph Agent]
↓
[Self-correction]
↓
[Answer]


## Быстрый старт
```bash
cp .env.example .env
docker-compose up -d
make migrate
make ingest
make run

Стек
Python 3.12 · FastAPI · LangGraph · PostgreSQL · pgvector ·
RabbitMQ · Redis · Prometheus · Grafana · Docker · GitHub Actions


**mcp_servers/sql_query_server.py**
```python
from mcp.server import Server
import psycopg2

server = Server("sql-query")

@server.tool()
def run_query(sql: str, limit: int = 100):
    conn = psycopg2.connect("dbname=core user=admin host=db")
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchmany(limit)
    return {"rows": rows, "columns": [d[0] for d in cur.description]}

@server.tool()
def explain(sql: str):
    conn = psycopg2.connect("dbname=core user=admin host=db")
    cur = conn.cursor()
    cur.execute("EXPLAIN ANALYZE " + sql)
    return {"plan": cur.fetchall()}
