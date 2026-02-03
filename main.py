import uvicorn


def main():
    print("Hello from fastapi-commerce!")
    uvicorn.run(
        "app.application:app",
        host="0.0.0.0",
        port=8000,
        workers=4,
    )


if __name__ == "__main__":
    main()
