# Архитектура AI-Platform-Combined

## Слои
1. **API Gateway** — FastAPI, аутентификация, rate limit
2. **Router** — LLM-классификация запроса
3. **MCP-серверы** — 5 серверов под разные задачи
4. **Agent** — LangGraph, self-correction, tool use
5. **Storage** — PostgreSQL + pgvector + Redis
6. **Monitoring** — Prometheus + Grafana + Evidently

## Поток запроса
1. Пользователь → POST /chat
2. Router определяет intent
3. Agent вызывает MCP-инструменты
4. Self-correction правит SQL/ошибки
5. Ответ + источники (RAG) → пользователю

## Мониторинг дрифта
Evidently считает PSI по эмбеддингам раз в час.
