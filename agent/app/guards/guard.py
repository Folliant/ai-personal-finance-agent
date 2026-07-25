class Guard:
    BLOCKED_PATTERNS = [
        "ignore previous instructions",
        "system prompt",
        "reveal your instructions",
        "transfer money",
        "send money",
        "make a payment",
    ]

    def check_input(
        self,
        request: str,
    ) -> None:
        text = request.lower()

        for pattern in self.BLOCKED_PATTERNS:
            if pattern in text:
                raise ValueError("Sorry, I cannot process that request.")

    def check_output(
        self,
        response: str | None,
    ) -> None:
        if not response or not response.strip():
            raise ValueError("Empty response")
