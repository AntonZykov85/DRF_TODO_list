import React from "react";
// import UserList from "./User";
import {Link} from "react-router-dom";


const Menu = () => {
  return (
      <nav className="navbar navbar-expand-md navbar-dark fixed-top bg-warning">
          <a className="navbar-brand" href="#">GeekBrains</a>
             <ul className="navbar-nav mr-auto">
                 <button className="btn btn-outline-success" type="button"><Link to ='/'>Users</Link></button>
                 <button className="btn btn-outline-success" type="button"><Link to ='/project'>Projects list</Link></button>
                 <button className="btn btn-outline-success" type="button"><Link to ='/ToDo'>What's need to do list</Link></button>
                 <button className="btn btn-outline-success" type="button"> {this.is_authenticated() ? <button onClick={() => this.logout()}>Logout</button> :
                         <Link to='/login'>Login </Link>}
                 </button>
             </ul>
      </nav>
  );
}

export default Menu;