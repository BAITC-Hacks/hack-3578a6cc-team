import json
from pathlib import Path


def main() -> None:
    events_path = Path(__file__).with_name("events.json")
    events = json.loads(events_path.read_text(encoding="utf-8"))
    critical_events = [event for event in events if event["level"] == "critical"]

    for event in critical_events:
        print(f'{event["level"]}: {event["message"]}')

    print(f"критичных {len(critical_events)}")


if __name__ == "__main__":
    main()
