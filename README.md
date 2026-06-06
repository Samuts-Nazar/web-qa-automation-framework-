# 🧪 Web QA Automation Framework

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.49.0-2EAD33?style=flat-square&logo=playwright&logoColor=white)](https://playwright.dev/)
[![pytest](https://img.shields.io/badge/pytest-8.3.4-0A9EDC?style=flat-square&logo=pytest&logoColor=white)](https://pytest.org/)
[![Allure](https://img.shields.io/badge/Allure-2.13.5-orange?style=flat-square)](https://allurereport.org/)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](https://opensource.org/licenses/MIT)

> **Дипломна робота** | Кваліфікаційний проєкт з автоматизації тестування веб-застосунків на основі патерну Page Object Model із використанням Playwright, pytest та інтеграцією CI/CD.

---

## 📋 Зміст

- [Про проєкт](#-про-проєкт)
- [Стек технологій](#-стек-технологій)
- [Архітектура фреймворку](#-архітектура-фреймворку)
- [Структура проєкту](#-структура-проєкту)
- [Встановлення та запуск](#-встановлення-та-запуск)
- [Запуск тестів](#-запуск-тестів)
- [Звітність](#-звітність)
- [CI/CD Pipeline](#-cicd-pipeline)
- [Патерни та принципи](#-патерни-та-принципи)
- [Автор](#-автор)

---

## 🎯 Про проєкт

Цей репозиторій містить **фреймворк для автоматизованого тестування веб-застосунків**, розроблений у рамках дипломної роботи. Як об'єкт тестування обрано демонстраційний e-commerce застосунок [SauceDemo](https://www.saucedemo.com) — платформу, що широко використовується в індустрії для відпрацювання навичок QA-автоматизації.

**Ключові особливості фреймворку:**

- **Page Object Model (POM)** — чітке розділення логіки тестів та взаємодії з UI
- **Headless-режим** — браузерні тести виконуються без графічного інтерфейсу (швидко та стабільно)
- **Автоматичні скріншоти** при падінні тестів — спрощує діагностику помилок
- **Мульти-рівнева звітність** — Allure Report + HTML-звіт pytest
- **CI/CD інтеграція** — автоматичний запуск тестів через GitHub Actions
- **Маркування тестів** — розділення на `smoke` та `regression` набори

---

## 🛠 Стек технологій

| Інструмент | Версія | Призначення |
|---|---|---|
| **Python** | 3.12+ | Основна мова розробки |
| **Playwright** | 1.49.0 | Керування браузером (Chromium) |
| **pytest** | 8.3.4 | Фреймворк для запуску тестів |
| **pytest-playwright** | 0.6.2 | Інтеграція Playwright з pytest |
| **Allure pytest** | 2.13.5 | Генерація деталізованих звітів |
| **pytest-html** | 4.1.1 | HTML-звіти для тестових сесій |
| **GitHub Actions** | — | CI/CD автоматизація |

---

## 🏗 Архітектура фреймворку

Фреймворк побудований за патерном **Page Object Model**, де кожна сторінка застосунку представлена окремим класом, що інкапсулює всі взаємодії з її елементами.

```
┌─────────────────────────────────────────────────┐
│                  Test Layer                     │
│           tests/ (pytest test cases)            │
└─────────────────────┬───────────────────────────┘
                      │ використовує
┌─────────────────────▼───────────────────────────┐
│               Page Object Layer                 │
│         pages/ (LoginPage, InventoryPage…)      │
└─────────────────────┬───────────────────────────┘
                      │ взаємодіє
┌─────────────────────▼───────────────────────────┐
│             Browser / Playwright                │
│     Chromium (headless) via sync_playwright     │
└─────────────────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────┐
│              Test Infrastructure                │
│  conftest.py: fixtures, hooks, screenshots      │
│  pytest.ini:  markers, base_url, testpaths      │
└─────────────────────────────────────────────────┘
```

### Ключові фікстури (`conftest.py`)

| Фікстура | Scope | Опис |
|---|---|---|
| `browser` | `session` | Одна Chromium-інстанція на всю сесію |
| `page` | `function` | Новий браузерний контекст для кожного тесту |
| `authenticated_page` | `function` | Сторінка з вже виконаним логіном (`standard_user`) |

---

## 📁 Структура проєкту

```
web-qa-automation-framework/
│
├── .github/
│   └── workflows/          # GitHub Actions CI/CD pipeline
│
├── pages/                  # Page Object Model класи
│   └── login_page.py       # Клас сторінки логіну
│
├── tests/                  # Тестові сценарії
│
├── screenshots/            # Скріншоти при падінні тестів (auto-generated)
│
├── conftest.py             # pytest-фікстури та хуки
├── pytest.ini              # Конфігурація pytest (маркери, шляхи)
├── requirements.txt        # Залежності проєкту
└── .gitignore
```

---

## 🚀 Встановлення та запуск

### Передумови

- Python **3.12** або новіший
- Git

### 1. Клонування репозиторію

```bash
git clone https://github.com/Trenerkok/web-qa-automation-framework-.git
cd web-qa-automation-framework-
```

### 2. Створення віртуального середовища

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Встановлення залежностей

```bash
pip install -r requirements.txt
```

### 4. Встановлення браузерів Playwright

```bash
playwright install chromium
```

---

## ▶️ Запуск тестів

### Запуск усіх тестів

```bash
pytest
```

### Запуск лише smoke-тестів

```bash
pytest -m smoke
```

### Запуск лише regression-тестів

```bash
pytest -m regression
```

### Запуск з детальним виводом

```bash
pytest -v
```

### Запуск з генерацією Allure-даних

```bash
pytest --alluredir=allure-results
```

### Запуск з генерацією HTML-звіту

```bash
pytest --html=report.html --self-contained-html
```

---

## 📊 Звітність

### Allure Report

Після запуску тестів з параметром `--alluredir`:

```bash
# Відкрити звіт у браузері
allure serve allure-results
```

Allure надає:
- Детальну хронологію тестового запуску
- Статистику проходження по маркерах та сьютах
- Вбудовані скріншоти при падінні тестів
- Історію запусків та тренди

### HTML-звіт pytest

```bash
pytest --html=report.html --self-contained-html
# Відкрити report.html у браузері
```

### Скріншоти при падінні

Фреймворк автоматично зберігає скріншот у папку `screenshots/` при будь-якому падінні тесту. Назва файлу відповідає ідентифікатору тесту, що полегшує діагностику.

---

## ⚙️ CI/CD Pipeline

Кожен `push` та `pull request` до гілки `main` автоматично запускає повний набір тестів через **GitHub Actions**.

```yaml
# .github/workflows/ci.yml
# Тригери: push / pull_request → main
# Кроки:
#   1. Checkout коду
#   2. Налаштування Python 3.12
#   3. pip install -r requirements.txt
#   4. playwright install chromium
#   5. pytest (headless Chromium)
#   6. Публікація Allure / HTML звіту як артефакту
```

Результати запусків доступні у вкладці **Actions** репозиторію.

---

## 🧩 Патерни та принципи

### Page Object Model (POM)

Кожна сторінка — окремий Python-клас. Тести взаємодіють лише з методами класу, а не з локаторами напряму. Це забезпечує:
- **Повторне використання** коду між тестами
- **Легку підтримку** при зміні UI (правити лише один клас)
- **Читабельність** тестів на рівні бізнес-логіки

### Fixture-based setup (pytest)

Використання `conftest.py` із scope-контролем (`session` / `function`) мінімізує накладні витрати на запуск браузера та забезпечує ізоляцію між тестами.

### Fail-fast Screenshots

Хук `pytest_runtest_makereport` автоматично захоплює стан екрану при провалі тесту — без жодного додаткового коду в самих тестах.

### Тест-маркування

Набори `smoke` і `regression` дозволяють гнучко вибирати обсяг тестування залежно від контексту (швидка перевірка після деплою vs. повний регресійний запуск).

---

## 📄 Ліцензія

Цей проєкт розповсюджується під ліцензією [MIT](https://opensource.org/licenses/MIT).
