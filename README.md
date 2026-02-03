# fastapi commerce app

### 실행

개발
```
uv run uvicorn app.application:app --reload
```

운영
```
uv run main.py
```

또는

```
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```