# API Testing

API-тесты для проекта `qa-portfolio`.

Репозиторий показывает базовый подход к API testing:

- проверка HTTP status code;
- проверка response body;
- проверка `Content-Type`;
- проверка HTML/static resources;
- проверка негативного сценария `404`;
- запуск тестов локально и через GitHub Actions.

## Что проверяется

| Endpoint | Проверка |
| --- | --- |
| `GET /health` | сервис доступен и возвращает `{ "status": "OK" }` |
| `GET /about` | endpoint возвращает текст профиля |
| `GET /` | главная страница возвращает HTML портфолио |
| `GET /css/style.css` | статический CSS-файл доступен |
| `GET /unknown-route` | неизвестный маршрут возвращает `404` |

## Локальный запуск

Сначала запусти сайт `qa-portfolio`:

```bash
cd ../qa-portfolio
npm install
npm start
```

Затем в этом репозитории запусти тесты:

```bash
npm test
```

По умолчанию тесты используют:

```text
http://localhost:3000
```

Можно указать другой адрес через `BASE_URL`:

```bash
BASE_URL=http://localhost:3000 npm test
```

Для PowerShell:

```powershell
$env:BASE_URL="http://localhost:3000"; npm test
```

## CI

GitHub Actions workflow:

1. клонирует репозиторий `qa-portfolio`;
2. устанавливает зависимости сайта;
3. запускает Express-приложение;
4. запускает API-тесты из этого репозитория.

Это позволяет хранить API-тесты отдельно от сайта и показывать их как самостоятельный QA-проект.
