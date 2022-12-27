import React from 'react'
import axios from 'axios';
import { useEffect } from 'react';





const App = ()=>{

  // defining the function to store the list of the post 
  const getAllPost = async ()=>{


	console.log("calling the getall post method inside the use effect ");
	// we have to use the axios to make a post request 
	const URL = "http://127.0.0.1:8000/api/";
	const response = await  axios.get(URL);
	console.log("The reponse from the backend is as follows \n");
	console.log(response.data);
  }
  // let us use a useffec 
  useEffect(() => {
    getAllPost()
    return () => {
      
    };
  }, []);
  return (
    <>
      <h1>this is this main content of the application </h1>
    </>
  )
}

// say everything went fine 
export default App;