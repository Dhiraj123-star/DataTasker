from celery import Celery

celery_app = Celery(
    "datatasker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/1"
)

celery_app.autodiscover_tasks(["app.tasks"])

# Explicit import to ensure registration
import app.tasks.csv_processor
