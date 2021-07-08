import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";

class App extends Component {
    constructor(props) {
        super(props);
        this.state = { apiResponse: "" };
    }

    /* Display User Data */
    // This is an example query, (Last name and first names were switched up in the database)
    getUser(id) {
        fetch(`http://localhost:9000/api/users/${id}`)
            .then(res => res.json())
            .then(res => this.setState({apiResponse : res.rows[0].LastName + " " + res.rows[0].FirstName}))
            .catch(err => err)
    }
    
    componentDidMount() {
        this.getUser(0);
    }

    render() {
        return (
            <div className="App">
                <header className="App-header">
                    <img src={logo} className="App-logo" alt="logo" />
                    <h1 className="App-title">Welcome to React</h1>
                </header>
                <p className="App-intro">{`Hello, ${this.state.apiResponse}`}</p>
            </div>
        );
    }
}

export default App;
