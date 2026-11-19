from fastapi import APIRouter

router = APIRouter(prefix="/events", tags=["Events"])

events = [
    {"name": "Welcome Day", "day": "Monday"},
    {"name": "SQL Workshop", "day": "Wednesday"},
    {"name": "API Demo", "day": "Friday"},
    {"name": "Quiz", "day": "Monday"}
]

@router.get("")
def get_events():
    return events

@router.get("/{day}")
def get_events_by_day(day: str):
    return [
        event for event in events
        if event["day"].lower() == day.lower()
    ]