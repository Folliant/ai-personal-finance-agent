import { Paper, Text, Group, Avatar } from "@mantine/core";
import { RobotIcon, UserIcon } from "@phosphor-icons/react";

type Props = {
  role: "user" | "assistant";
  content: string;
};

export function MessageBubble({ role, content }: Props) {
  const isUser = role === "user";

  return (
    <Group justify={isUser ? "flex-end" : "flex-start"} mb="sm">
      {!isUser && (
        <Avatar>
          <RobotIcon size={20} />
        </Avatar>
      )}

      <Paper p="sm" radius="lg" maw={260} bg={isUser ? "blue.1" : "gray.1"}>
        <Text size="sm">{content}</Text>
      </Paper>

      {isUser && (
        <Avatar>
          <UserIcon size={20} />
        </Avatar>
      )}
    </Group>
  );
}
