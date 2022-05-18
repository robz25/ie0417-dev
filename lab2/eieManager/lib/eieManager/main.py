import uvicorn


def main():
    """
    Device Manager application main function.
    """
    uvicorn.run("eieManager.ServerAPI.main:app")


if __name__ == "__main__":
    main()
