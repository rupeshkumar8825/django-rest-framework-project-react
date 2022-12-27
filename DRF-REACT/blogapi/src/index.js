// this is the main component of the react application 
import React from 'react'
import ReactDOM from 'react-dom'
import './index.css'


// then we will be needing the route for this purpose 
import {Route, BrowserRouter as Router, Routes} from 'react-router-dom';
import App from './App';
// i also need to import some other components for this purpose 
// we will be importing the header and the footer for the application that will remain the same
// for all the pages for this purpose 
// import Header from './components/Header';
// import Footer from './components/Footer';
import Header from './components/Header';
import Footer from './components/Footer';


// now we have to create the routing for the application 
const routing = (
    <Router>
        <React.StrictMode>
            {/* here is the herarchy for the home page  */}
            {/* we will have the header and footer the same across all the pages */}
            <Header></Header>
            {/* this is the routing for the app components and other components  */}
            <Routes>
                <Route exact path='/' element={<App></App>}/>
            </Routes>
            <Footer></Footer>
        </React.StrictMode>
    </Router>
)

// now we have to render this component inside the root 
ReactDOM.render(routing, document.getElementById('root'));




 