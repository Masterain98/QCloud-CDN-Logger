docker build -f Dockerfile -t qcloud-logger/latest .
docker run --name=Qcloud-Logger \
           --mount type=bind,source="$(pwd)"/data,target=/app/data \
           --mount type=bind,source="$(pwd)"/config.json,target=/app/config.json \
           --restart always qcloud-logger/latest
