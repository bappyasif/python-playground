import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "src.app:server",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="debug"
    )

# if fails to run this from "run" button then try run it manually using this command ```uvicorn src.app:server --host 0.0.0.0 --port 8000 --reload --log-level debug```


# if __name__ == "__main__":
#     uvicorn.run(
#         "src.app:server",
#         host="0.0.0.0",
#         port=8000,
#         reload=True
#     )