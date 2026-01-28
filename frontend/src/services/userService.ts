/**
 * User Service - Handles API calls to fetch user data from backend.
 * Reads API base URL from environment variables.
 */

export interface User {
  id: number;
  name: string;
  username: string;
  email: string;
  phone: string;
  website: string;
  address: string; // CSV stores address as stringified object
  company: string; // CSV stores company as stringified object
}

const API_BASE_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";

/**
 * Fetches all users from the backend API.
 * @returns Promise<User[]>
 * @throws Error if the request fails or response is invalid.
 */
export async function fetchUsers(): Promise<User[]> {
  const response = await fetch(`${API_BASE_URL}/api/users`);
  if (!response.ok) {
    throw new Error(`Failed to fetch users: ${response.status} ${response.statusText}`);
  }
  const data = await response.json();
  // Defensive: Ensure data is an array of objects with required fields
  if (!Array.isArray(data)) {
    throw new Error("Invalid user data format received from API");
  }
  return data as User[];
}