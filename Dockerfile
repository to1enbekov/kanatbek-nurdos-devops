FROM python:3.12-slim
WORKDIR /opt/devops
COPY app/ ./app/
RUN python -m compileall -q app/ && useradd --create-home --uid 10001 appuser
USER appuser
EXPOSE 8000
CMD ["python", "-u", "app/main.py"]
