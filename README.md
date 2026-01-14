# website



```bash
git clone https://github.com/Styler10/website.git
cd website
```

```bash
python -m venv venv
venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

```bash
alembic upgrade head
```

```bash
uvicorn backend.main:app --reload
```
