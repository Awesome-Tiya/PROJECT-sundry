/// <reference types="vite/client" />

// Extend the existing Vite-provided ImportMetaEnv
interface ImportMetaEnv extends Readonly<Record<string, string>> {
  readonly VITE_API_BASE_URL?: string;
  // Add other custom VITE_ vars here
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
