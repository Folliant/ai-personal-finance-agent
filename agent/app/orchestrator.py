from app.agent.agent import Agent
from app.guards.guard import Guard


class Orchestrator:
    def __init__(
        self,
        agent: Agent,
        guard: Guard,
    ):
        self.agent = agent
        self.guard = guard

    def run(
        self,
        session_id: str,
        request: str,
    ):
        self.guard.check_input(request)

        result = self.agent.run(
            session_id=session_id,
            query=request,
        )

        self.guard.check_output(result)

        return result
