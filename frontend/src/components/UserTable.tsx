import React, { useEffect, useState } from "react";
import "./UserTable.css";

interface User {
  id: number;
  name: string;
  username: string;
  email: string;
  phone: string;
  website: string;
  [key: string]: any; // For address and company fields
}

const flattenAddress = (address: any) =>
  address
    ? `${address.street}, ${address.suite}, ${address.city}, ${address.zipcode} (${address.geo?.lat}, ${address.geo?.lng})`
    : "";

const flattenCompany = (company: any) =>
  company ? `${company.name} (${company.catchPhrase}, ${company.bs})` : "";

const UserTable: React.FC = () => {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchUsers = async () => {
      setLoading(true);
      setError(null);
      try {
        const response = await fetch(
          process.env.REACT_APP_API_URL + "/api/users"
        );
        if (!response.ok) {
          throw new Error("Failed to fetch user data");
        }
        const data = await response.json();
        setUsers(data);
      } catch (err: any) {
        setError(err.message || "Unknown error");
      } finally {
        setLoading(false);
      }
    };
    fetchUsers();
  }, []);

  if (loading) return <div>Loading user data...</div>;
  if (error) return <div className="error">Error: {error}</div>;

  return (
    <div className="user-table-container">
      <h2>User Data Table</h2>
      <table className="user-table">
        <thead>
          <tr>
            <th>Id</th>
            <th>Name</th>
            <th>Username</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Website</th>
            <th>Address</th>
            <th>Company</th>
          </tr>
        </thead>
        <tbody>
          {users.map((u) => (
            <tr key={u.id}>
              <td>{u.id}</td>
              <td>{u.name}</td>
              <td>{u.username}</td>
              <td>{u.email}</td>
              <td>{u.phone}</td>
              <td>{u.website}</td>
              <td>{flattenAddress(u.address)}</td>
              <td>{flattenCompany(u.company)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default UserTable;