# RecipeBook – Django REST API (TDD-Projekt) / Django REST API (TDD Project)

Ein kleines Lernprojekt für ein Rezeptbuch-Backend mit **Django** und **Django REST Framework**, komplett **testgetrieben (TDD)** entwickelt.  
A small learning project for a recipe book backend built with **Django** and **Django REST Framework**, developed using **Test-Driven Development (TDD)**.

---

## 🇩🇪 Überblick

- Backend-API für Rezepte (Modell `Recipe` mit:
  - `title`, `description`, `created_at`, `author (ForeignKey auf User)`)
- Implementierung mit **Django REST Framework** (`ModelViewSet`, `Serializer`, `Router`)
- Authentifizierung:
  - zunächst offen / read-only
  - danach **TokenAuthentication** + `IsAuthenticatedOrReadOnly`
  - später Umstellung auf **`IsAuthenticated`** (alle Endpunkte nur mit Login)
- **TDD-Ansatz**:
  1. Test schreiben (z.B. `GET /recipes-list/` → 200 OK)
  2. Test ausführen → *FAIL* (gewollt)
  3. Minimalen Code schreiben (Model, Serializer, ViewSet, URLs, Settings)
  4. Test wiederholen → *PASS*
  5. Nächsten Test schreiben (z.B. POST, Auth, Detail etc.)

- Tests:
  - Integrationstests mit **Django REST Framework `APITestCase`**
  - GET- und POST-Requests auf `/recipes-list/` und `/recipes-list/<id>/`
  - **Happy Path** (mit gültigem Token, 200/201)
  - **Unhappy Path** (ohne Authentifizierung → 401 Unauthorized)
  - Gemeinsame `BaseRecipeAPITestCase` mit `setUp`, `authenticate()` und `create_recipe()`
  - Test für `__str__` des `Recipe`-Modells
- Test-Setup:
  - **pytest** + **pytest-django**
  - **pytest-cov** für Testabdeckung (Coverage ~99–100 %)

---

## 🇩🇪 Installation

```bash
git clone <REPO_URL>
cd RecipeBook

python -m venv venv
venv\Scripts\activate  # oder: source venv/bin/activate (Linux/macOS)

pip install -r requirements.txt
python manage.py migrate
python.manage.py createsuperuser
python manage.py runserver
```

Die API ist erreichbar unter: `http://127.0.0.1:8000/`

---

## 🇬🇧 Overview

- Backend REST API for recipes (`Recipe` model with:
  - `title`, `description`, `created_at`, `author (ForeignKey to User)`)
- Built with **Django REST Framework** (`ModelViewSet`, serializer, router)
- Authentication:
  - initially open / read-only
  - then **TokenAuthentication** + `IsAuthenticatedOrReadOnly`
  - later switched to **`IsAuthenticated`** (all endpoints require login)
- **TDD workflow**:
  1. Write a test (e.g. `GET /recipes-list/` → 200 OK)
  2. Run test → *FAIL* (as expected)
  3. Implement minimal code (model, serializer, viewset, URLs, settings)
  4. Run test again → *PASS*
  5. Add more tests (POST, auth, detail, happy/unhappy paths, …)

- Tests:
  - Integration tests using **Django REST Framework `APITestCase`**
  - GET and POST requests to `/recipes-list/` and `/recipes-list/<id>/`
  - **Happy path** (authenticated → 200/201)
  - **Unhappy path** (no auth → 401 Unauthorized)
  - Shared `BaseRecipeAPITestCase` with `setUp`, `authenticate()` and `create_recipe()`
  - Test for `Recipe.__str__` returning the title
- Test setup:
  - **pytest** + **pytest-django**
  - **pytest-cov** for coverage (around 99–100 %)

---

## 🧱 Tech Stack / Tech-Stack

- Python 3.x  
- Django 6.x  
- Django REST Framework  
- `djangorestframework-authtoken` (TokenAuthentication)  
- pytest, pytest-django, pytest-cov  

---

## ⚙️ Installation & Start / Installation & Run

🇩🇪 **Schritte:**

```bash
git clone <REPO_URL>
cd RecipeBook

python -m venv venv
venv\Scripts\activate  # oder: source venv/bin/activate (Linux/macOS)

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Die API ist erreichbar unter: `http://127.0.0.1:8000/`

---

🇬🇧 **Steps:**

```bash
git clone <REPO_URL>
cd RecipeBook

python -m venv venv
venv\Scripts\activate  # or: source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

API base URL: `http://127.0.0.1:8000/`

---

## 🔗 Wichtige Endpunkte / Key Endpoints

- `POST /api-token-auth/`  
  - 🇩🇪: Token für einen User holen (Login)  
  - 🇬🇧: Obtain auth token for a user (login)

- `GET /recipes-list/`  
  - 🇩🇪: Alle Rezepte auflisten (Login erforderlich bei `IsAuthenticated`)  
  - 🇬🇧: List all recipes (auth required when `IsAuthenticated` is enabled)

- `POST /recipes-list/`  
  - 🇩🇪: Neues Rezept erstellen (mit Token + `author`-ID)  
  - 🇬🇧: Create a new recipe (with token + `author` ID)

- `GET /recipes-list/<id>/`  
  - 🇩🇪: Details zu einem Rezept  
  - 🇬🇧: Retrieve recipe details

- `PUT/PATCH/DELETE /recipes-list/<id>/`  
  - 🇩🇪: Rezept bearbeiten oder löschen  
  - 🇬🇧: Update or delete a recipe

**Auth-Header / Auth header:**

```http
Authorization: Token <YOUR_TOKEN>
```

---

## 🧪 Tests & Coverage / Tests & Coverage

🇩🇪 **Tests ausführen:**

```bash
# Django Test Runner
python manage.py test

# pytest
pytest

# pytest mit Coverage
pytest --cov=recipes_app --cov-report=term-missing
```

🇬🇧 **Run tests:**

```bash
# Django test runner
python manage.py test

# pytest
pytest

# pytest with coverage
pytest --cov=recipes_app --cov-report=term-missing
```


