python -m pip install -r requirements.txt
docker build -t api_gateway .
docker run --network my-network -p 5000:5000 api_gateway