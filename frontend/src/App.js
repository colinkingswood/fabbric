import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const [items, setItems] = useState([]);
    const [selectedItem, setSelectedItem] = useState(null);
    const [selectedColor, setSelectedColor] = useState(null);
    const [imageSrc, setImageSrc] = useState(null);  // State to hold the image source

    useEffect(() => {
        axios.get('http://localhost:8000/api/items/')
        .then(response => {
            setItems(response.data);
        });
    }, []);

    const selectItem = item => {
        setSelectedColor(null)
        setSelectedItem(item);
    };

    const getCustomItem = (color, selectedItem) => {
        setSelectedColor(color)
        console.log(color, selectedItem);
        const url = 'http://localhost:8000/api/items/' + selectedItem.id + '/customize_color/';
        const data = {'color': color};
        axios.post(url, data)
            .then(response => {
                console.log('Response:', response);
                setImageSrc(`${response.data}`);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    };
    return (
    <div className="App">
        <h1>Clothing Items</h1>
        <div className="color-picker">
            {selectedItem && (
                <label>Choose a color to customize item
                    <input
                        type="color"
                        onChange={(e) => getCustomItem(e.target.value, selectedItem)}
                        style={{ marginLeft: 20 }}
                    />
                </label>
            )}
        </div>
        <div className="content">
            <div className="item-list">
                <ul>
                {items.map(item => (
                    <li key={item.id} onClick={() => selectItem(item)}>
                        <div>{item.name}</div>
                        <div>
                            <img src={item.thumbnail} alt={`${item.name}-tn`} />
                        </div>
                        <div>{item.description}</div>
                    </li>
                ))}
                </ul>
            </div>

            <div className="item-details">
            {selectedItem && selectedColor && (
                <div>
                    <h2>{selectedItem.name}</h2>
                    {imageSrc && <img src={imageSrc} alt={selectedItem.name} width="400" />}
                </div>
                )}
            </div>

            <div className="spacer"></div>  {/* Blank element to balance the layout */}
        </div>
    </div>
    );

}

export default App;

