import { Paper } from "@mantine/core";

export function PhoneFrame({ children }: { children: React.ReactNode }) {
  return (
    <Paper shadow="xl" radius="xl" w={390} h="90vh" mx="auto" mt="xl">
      {children}
    </Paper>
  );
}
