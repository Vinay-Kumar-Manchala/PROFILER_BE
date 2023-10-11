import uvicorn
from dotenv import load_dotenv

load_dotenv()

from scripts.constants import app_configuration

if __name__ == '__main__':
    uvicorn.run("main:app", host=app_configuration.HOST, port=int(app_configuration.PORT))
