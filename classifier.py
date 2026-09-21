from pathlib import Path


def classify(message: str) -> tuple[str, str]:
    text = message.lower()

    if any(word in text for word in ("очередь", "холодн", "пропал", "не работает")):
        return (
            "жалоба",
            "Спасибо за сообщение. Мы передадим информацию ответственным сотрудникам для проверки.",
        )

    if any(word in text for word in ("как", "где", "получить", "парковк")):
        return (
            "справка",
            "Подскажите, пожалуйста, дополнительные детали — мы поможем найти нужную информацию.",
        )

    return (
        "другое",
        "Спасибо за обращение. Уточните, пожалуйста, детали, чтобы мы могли помочь.",
    )


def main() -> None:
    messages_path = Path(__file__).with_name("messages.txt")
    messages = [line.strip() for line in messages_path.read_text(encoding="utf-8").splitlines() if line.strip()]

    for number, message in enumerate(messages, start=1):
        category, reply = classify(message)
        print(f"{number}. {message}")
        print(f"   Категория: {category}")
        print(f"   Ответ: {reply}")


if __name__ == "__main__":
    main()
