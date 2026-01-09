# Auth Service

Issues JWT tokens used by other services.

## Run
conda create -n auth-service python=3.14
conda activate auth-service
pip install -r requirements.txt
uvicorn server:app --port 8000