import os
import multiprocessing


host = os.environ.get("HOST", "0.0.0.0")
port = os.environ.get("PORT", "8000")

workers_per_core = int(os.environ.get("WORKERS_PER_CORE", 1))

cores = multiprocessing.cpu_count()
default_concurrency = (workers_per_core * cores) + 1

## Gunicorn config
# Server socket
bind = [f"{host}:{port}"]
# Workers Processes
workers = default_concurrency
timeout = 120
graceful_timeout = 120
keepalive = 120
# Server mechanics
worker_tmp_dir = os.environ.get("TMP_DIR", "/dev/shm")
# Debugging
reload = os.environ.get("RELOAD", False)
# Logging
loglevel = os.environ.get("LOG_LEVEL", "info")
accesslog = os.environ.get("ACCESS_LOG", "-")
errorlog = os.environ.get("ERROR_LOG", "-")
