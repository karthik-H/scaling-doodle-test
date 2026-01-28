import React, { useEffect, useState } from "react";
import "./UserTable.css";
import { fetchUsers, User } from "../services/userService";

/**
 * Flattens the address object or string for display.
 * @param address Address object or stringified JSON
 */
const flattenAddress = (address: any) => {
  let addr = address;
  if (typeof address === "string") {
    try {
      addr = JSON.parse(address);
    } catch {
      return address;
    }
  }
  return addr
    ? `${addr.street}, ${addr.suite}, ${addr.city}, ${addr.zipcode} (${addr.geo?.lat}, ${addr.geo?.lng})`
    : "";
};

/**
 * Flattens the company object or string for display.
 * @param company Company object or stringified JSON
 */
const flattenCompany = (company: any) => {
  let comp = company;
  if (typeof company === "string") {
    try {
      comp = JSON.parse(company);
    } catch {
      return company;
    }
  }
  return comp ? `${comp.name} (${comp.catchPhrase}, ${comp.bs})` : "";
};

/**
 * UserTable component - displays user data in a table view.
 */
const UserTable: React.FC = () => {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const loadUsers = async () => {
      setLoading(true);
      setError(null);
      try {
        const data = await fetchUsers();
        setUsers(data);
      } catch (err: any) {
        setError(err.message || "Unknown error");
      } finally {
        setLoading(false);
      }
    };
    loadUsers();
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