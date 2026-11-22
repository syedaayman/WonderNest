import { defineConfig, loadEnv } from "vite";
import react from "@vitejs/plugin-react";

// In development the SPA runs on :5173 and proxies /api to the FastAPI server.
// In production FastAPI serves the built files, so relative /api calls just work.
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, ".", "");
  return {
    plugins: [react()],
    server: {
      port: 5173,
      proxy: {
        "/api": {
          target: env.VITE_DEV_API_TARGET || "http://127.0.0.1:8000",
          changeOrigin: true,
        },
      },
    },
    build: {
      outDir: "dist",
      sourcemap: false,
    },
  };
});
