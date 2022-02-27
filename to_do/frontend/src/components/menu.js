import React from 'react';
import FooterPage from "./fotter";
import {HashRouter, Route, BrowserRouter, Link} from "react-router-dom";

const Menu = () => {
  return (
      <nav className="navbar navbar-light bg-light">
          <form className="form-inline">
              <button className="btn btn-outline-success" type="button"><Link to ='/'>Users</Link></button>
              <button className="btn btn-outline-success" type="button"><Link to ='/projects'>Projects list</Link></button>
              <button className="btn btn-outline-success" type="button"><Link to ='/ToDo'>What's need to do list</Link></button>
          </form>
      </nav>
  );
}

export default Menu;