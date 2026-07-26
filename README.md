# Автотесты для automationexercise.com

Учебный проект: UI-тесты (Selenium) и API-тесты (requests + pytest).
Отчёты — Allure. Для CI есть Jenkinsfile.

## Установка

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
```

Нужен Chrome. Allure CLI — если хотите смотреть отчёт локально.

## Запуск

```powershell
pytest                  # всё вместе
pytest tests/api -m api # только API
pytest tests/ui -m ui   # только UI
```

UI-тесты идут долго (около 20 мин). Если много падений — нужно настроить VPN, сайт иногда блокирует автоматизацию.

Allure после прогона:

```powershell
allure serve reports/allure-results
```

## Папки

- `pages/` — страницы для UI
- `api/` — запросы к API
- `tests/ui/`, `tests/api/` — сами тесты
- `config/` — настройки из `.env`

## Jenkins

В репозитории лежит `Jenkinsfile`. необходимо создать Pipeline Job, указать Git и путь к файлу.

## Настройки (.env)

См. `.env.example` — там BASE_URL и HEADLESS.

