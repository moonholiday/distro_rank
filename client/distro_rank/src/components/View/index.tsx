import React, { useState, useEffect } from 'react';
import axios from 'axios';

interface Distro {
    id: number;
    name: string;
    description: string;
    version: string;
    release_date: string;
    website: string;
    documentation: string;
    popularity_score: string;
    logo: string;
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
                        <img src={distro.logo} />
                        <p>{distro.description}</p>
                        <p>{distro.release_date}</p>
                        <p>{distro.documentation}</p>
                        <p>{distro.popularity_score}</p>
                        <p>{distro.website}</p>
                        <p>Version: {distro.version}</p>
                        {/* Add more fields as needed */}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default DistroList;

