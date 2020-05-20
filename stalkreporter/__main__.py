import asyncio
import dotenv
from stalkreporter.server import serve

if __name__ == "__main__":
    dotenv.load_dotenv()
    asyncio.run(serve())
