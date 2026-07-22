import logging
from pathlib import Path
from logging.handlers import RotatingFileHandler

def setup_logging(name: str = "todoapp", level: int = logging.INFO, logs_dir: Path | None = None) -> logging.Logger:
    # Place logs at project root: .../15_todoapp_monitor/logs/app.log
    root_dir = Path(__file__).resolve().parent.parent
    logs_dir = logs_dir or (root_dir / "logs")
    logs_dir.mkdir(exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s")

    file_handler = RotatingFileHandler(
        logs_dir / "app.log", maxBytes=1_000_000, backupCount=5, encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # Reset handlers to avoid duplicates on reload
    logger.handlers.clear()
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    # Reduce noise from uvicorn access logs
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    return logger