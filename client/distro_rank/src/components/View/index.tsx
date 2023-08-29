import React, { useState, useEffect } from 'react';
import axios from 'axios';

interface Distro {
  id: number;
  name: string;
  description: string;
  version: string;
}

const DistroList: React.FC = () => {
  const [distros, setDistros] = useState<Distro[]>([]);

  useEffect(() => {
    axios.get<Distro[]>('http://127.0.0.1:8000/api/distributions/')  // Replace with your API endpoint
      .then(response => {
        setDistros(response.data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      <h1>Linux Distribution Ranking</h1>
      <ul>
        {distros.map(distro => (
          <li key={distro.id}>
            <h2>{distro.name}</h2>
            <p>{distro.description}</p>
            <p>Version: {distro.version}</p>
            {/* Add more fields as needed */}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default DistroList;

