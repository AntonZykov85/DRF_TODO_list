import React from 'react';
import logo from './logo.svg';
import './App.css';
import ProjectsList from "./components/project";
import ToDoList from "./components/ToDo";
import UserList from "./components/users";
import FooterPage from "./components/fotter";
import Menu from "./components/menu";
import NotFound404 from "./components/NotFound404";
import axios from 'axios'
import {HashRouter, Route, BrowserRouter, Switch} from "react-router-dom";

class App extends React.Component {
   constructor(props) {
       super(props)
       this.state = {
           'users': [],
           'project': [],
           'to_do': [],
       }
   }
   componentDidMount() {
     axios.get('http://127.0.0.1:8000/api/users/')
       .then(response => {
           const users = response.data
               this.setState(
               {
                   'users': users
               }
           )
       }).catch(error => console.log(error)),


     axios.get('http://127.0.0.1:8000/api/project/')
       .then(response => {
           const project = response.data
               this.setState(
               {
                   'project': project
               }
           )
       }).catch(error => console.log(error)),


     axios.get('http://127.0.0.1:8000/api/to_do/')
       .then(response => {
           const to_do = response.data
               this.setState(
               {
                   'to_do': to_do
               }
           )
       }).catch(error => console.log(error))
}

   render () {
       return (
           <div>

             <div>
                   <HashRouter>
                       <div>
                           <Menu />
                       </div>

                       <Switch>
                           <Route exact path='/' component = {() => <UserList users={this.state.users} />} />
                           <Route exact path='/projects' component = {() =>  <ProjectsList projects={this.state.project} />} />
                           <Route exact path='/ToDo' component = {() =>  <ToDoList ToDos={this.state.to_do} />}/>
                           <Route component = {NotFound404}/>

                       </Switch>

                      </HashRouter>
               </div>

               <div>
                   <FooterPage />
               </div>

           </div>


       )
   }

}



export default App;
