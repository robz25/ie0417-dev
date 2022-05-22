import uvicorn


def main():
    uvicorn.run("sensor_commands.eieManager:app")


if __name__ == "__main__":
    main()
