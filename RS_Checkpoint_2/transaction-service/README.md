# Transaction Service

Handles internal money transfers.

## Run
conda create -n transaction-service python=3.14
conda activate transaction-service
pip install -r requirements.txt
uvicorn server:app --port 8002