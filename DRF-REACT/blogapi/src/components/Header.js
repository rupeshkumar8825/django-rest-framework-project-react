import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import {Toolbar} from '@material-ui/core';
import {Typography} from '@material-ui/core';
import {CssBaseline} from '@material-ui/core';
import { makeStyles }  from '@material-ui/core';


// making some changes to the css properties apart from the material ui 
const useStyles = makeStyles((theme) => ({
    appBar: {
        borderBottom : `1px solid ${theme.palette.divider}`,
    }
}));


// now we have to make the react component 
const Header = () =>{
    const classes = useStyles();

    return (
        <React.Fragment>
            <CssBaseline></CssBaseline>
            <AppBar position = "static" color="white" elevation = {0} className = {classes.appBar}>
                <Toolbar>
                    <Typography variate = "h6" color = "inherit" noWrap>
                        BlogmeUp
                    </Typography>
                </Toolbar>
            </AppBar>

            {/* <h1>this is the header of the application</h1> */}
        </React.Fragment>
    )
}

// say everything went fine 
// we have to export this component 
export default Header;