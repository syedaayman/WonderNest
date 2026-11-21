"""Command-line entry point: ``python -m app.curriculum.cli`` from the backend folder."""

from app.core.config import get_settings
from app.core.database import SessionLocal
from app.curriculum.seed import seed_curriculum


def main() -> None:
    db = SessionLocal()
    try:
        counts = seed_curriculum(db, get_settings().DEMO_PASSWORD)
    finally:
        db.close()
    print(counts)
    print("Seed complete.")


if __name__ == "__main__":
    main()
