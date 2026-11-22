import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// In development the SPA runs on :5173 and proxies /api to the FastAPI server.
// In production FastAPI serves the built files, so relative /api calls just work.
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      "/api": {
        target: process.env.VITE_DEV_API_TARGET ?? "http://127.0.0.1:8000",
        changeOrigin: true,
      },
    },
  },
  build: {
    outDir: "dist",
    sourcemap: false,
  },
});
