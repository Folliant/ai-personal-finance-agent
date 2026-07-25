import { config } from "../config";

export async function sendMessage(message: string) {
  const response = await fetch(`${config.apiUrl}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      session_id: "demo-session",
      message,
    }),
  });

  if (!response.ok) {
    throw new Error("Failed to send message");
  }

  const data = await response.json();

  return data.answer;
}
