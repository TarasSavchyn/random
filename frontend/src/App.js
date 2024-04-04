import React from 'react';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Navbar from './navbar/Navbar';
import AddressManager from './adresses/AddressManager';
import BankManager from "./banks/BankManager";

function App() {
    return (
        <Router>
            <div>
                <Navbar/>
                <Routes>
                    <Route path="/banks" element={<BankManager/>}/>
                    <Route path="/addresses" element={<AddressManager/>}/>
                </Routes>
            </div>
        </Router>
    );
}

export default App;