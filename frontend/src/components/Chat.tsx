import { useEffect, useRef, useState } from "react";

import { Stack, TextInput, ActionIcon, ScrollArea } from "@mantine/core";

import { PaperPlaneTiltIcon } from "@phosphor-icons/react";

import { MessageBubble } from "./MessageBubble";
import { sendMessage } from "../api/chat";

type Message = {
  role: "user" | "assistant";
  content: string;
};

export function Chat() {
  const viewport = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  const [messages, setMessages] = useState<Message[]>([
    {
      role: "assistant",
      content: "Hi! I can help you understand your spending.",
    },
  ]);

  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  async function send() {
    if (!input.trim() || loading) {
      return;
    }

    const text = input;

    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: text,
      },
    ]);

    setInput("");
    setLoading(true);

    try {
      const answer = await sendMessage(text);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: answer,
        },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "Sorry, I couldn't process your request.",
        },
      ]);

      console.error(error);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    viewport.current?.scrollTo({
      top: viewport.current.scrollHeight,
      behavior: "smooth",
    });
  }, [messages, loading]);

  useEffect(() => {
    if (!loading) {
      inputRef.current?.focus();
    }
  }, [loading]);

  return (
    <Stack h="100%" gap={0}>
      <ScrollArea flex={1} viewportRef={viewport}>
        <Stack p="md" gap="sm">
          {messages.map((message, index) => (
            <MessageBubble key={index} {...message} />
          ))}

          {loading && (
            <MessageBubble role="assistant" content="Penny is thinking..." />
          )}
        </Stack>
      </ScrollArea>

      <TextInput
        ref={inputRef}
        mx="md"
        mb="md"
        placeholder="Ask about spending..."
        value={input}
        disabled={loading}
        onChange={(e) => setInput(e.currentTarget.value)}
        rightSection={
          <ActionIcon onClick={send} disabled={loading}>
            <PaperPlaneTiltIcon size={18} />
          </ActionIcon>
        }
        onKeyDown={(e) => {
          if (e.key === "Enter" && !loading) {
            send();
          }
        }}
      />
    </Stack>
  );
}
