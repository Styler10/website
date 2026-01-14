# website



```bash
git clone https://github.com/Styler10/website.git
cd website

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

alembic upgrade head

uvicorn backend.main:app --reload
