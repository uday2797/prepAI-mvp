import axios from "axios";

export const API = axios.create({
  baseURL: "/api", // Vercel serverless will route /api automatically
});
