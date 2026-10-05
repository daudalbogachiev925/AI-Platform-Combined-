# MCP-протокол

Model Context Protocol — способ дать LLM доступ к инструментам.

## Серверы
| Сервер | Назначение |
|--------|-----------|
| metadata | Схема метаданных 1С |
| sql-query | Выполнение SQL |
| journal | Журнал документов |
| odata | OData-запросы |
| rag | Поиск по документации |

## Формат вызова
```json
{"tool": "sql-query.run_query", "args": {"sql": "SELECT ...", "limit": 100}}
