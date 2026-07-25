import { z } from "zod";

const configSchema = z.object({
  apiUrl: z.url(),
});

export const config = configSchema.parse({
  apiUrl: import.meta.env.VITE_API_URL,
});
