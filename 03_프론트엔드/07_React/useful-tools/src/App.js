import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
    const [value, setValue] = useState('');
    useEffect(() => {
        console.log(value);
    }, [value]);

    return (
        <div>
            <p>와우!</p>
        </div>
    );
}

export default App;
