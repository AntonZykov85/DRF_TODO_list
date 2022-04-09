import React from 'react';
// import logo from './logo.svg';
import {Route, Link, Switch, Redirect, BrowserRouter as Router} from "react-router-dom";

import './bootstrap/css/bootstrap.min.css'
import './bootstrap/css/sticky-footer-navbar.css'

import UserList from "./components/users.js";
import ProjectsList from "./components/project.js";
import ToDoList from "./components/ToDo";
import Menu from "./components/menu.js";
import FooterPage from "./components/fotter.js";
import NotFound404 from "./components/NotFound404.js";
import LoginForm from "./components/Auth.js";
import axios from "axios";
import Cookies from 'universal-cookie';
import ProjectForm from "./components/ProjectForm";
import TODOForm from "./components/TodoForm";


class App extends React.Component {
   constructor(props) {
       super(props)
       this.state = {
           'users': [],
           'project': [],
           'to_do': [],
           'token': '',
       }
   }


    deleteProject(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/project/${id}`, {headers}).then(

            response => {
                this.load_data()
            }
        ).catch(error => {
            console.log(error)
            this.setState({project: []})
        })
    }


    deleteTODO(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/to_do/${id}`, {headers}).then(
            response => {
                this.load_data()
            }
        ).catch(error => {
            console.log(error)
            this.setState({to_do: []})
        })
    }


    deleteUser(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/users/${id}`, {headers}).then(
            response => {
                this.load_data()
            }
        ).catch(error => {
            console.log(error)
            this.setState({users: []})
        })
    }


    createProject(name, repo_link, user) {
        const headers = this.get_headers()
        const data = {name: name, repo_link: repo_link, users_list: user}
        axios.post('http://127.0.0.1:8000/api/project/', data, {headers}).then(

            response => {

            //     let new_project = response.data
            //     const user = this.state.users.filter((item) => item.id === new_project.user) [0]
            //     new_project.user = user
            //     this.setState({project: [...this.state.project, new_project]})
            // }).catch(error => {
            //  console.log(error)})}

                this.load_data()
            }
        ).catch(error => {
            console.log(error)
            this.setState({project: []})

        })

    }

    createTODO(initial_project, note, creator) {
        const headers = this.get_headers()
        const data = {initial_project: initial_project, note: note, creator: creator}
        axios.post('http://127.0.0.1:8000/api/to_do/', data, {headers}).then(
            response => {
                this.load_data()
            }
        ).catch(error => {
            console.log(error)
            this.setState({to_do: []})

        })

    }

   logout() {
        this.set_token('')
    }


    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
        // this.setState({'token': token})
        // console.log(this.set_token)
    }

    is_authenticated() {
        return this.state.token !== ''
    }


    get_token_from_cookies() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        console.log(token)
        this.setState({'token': token}, () => this.load_data())
        // this.setState({'token': token})
    }


    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
            .then(response => {
                this.set_token(response.data['token'])
                console.log(response.data)
            }).catch(error => alert('Неверный логин или пароль!'))
    }

    get_headers() {
        // console.log('test')
        let headers = {
            'Content-Type': 'application/json'
        }
        // console.log(headers)
        // console.log(this.is_authenticated())
        if (this.is_authenticated()) {
            // console.log(`Token ${this.state.token}`)
            headers['Authorization'] = `Token ${this.state.token}`
        }
        return headers
    }

    load_data() {
        const headers = this.get_headers()
        console.log(this.get_headers())

        axios.get('http://127.0.0.1:8000/api/users/', {headers})
            .then(response => {
                this.setState({'users': response.data})
            }).catch(error => {
            console.log(error)
            this.setState({'users': []})
        })

        axios.get('http://127.0.0.1:8000/api/project/', {headers})
            .then(response => {
                this.setState({'project': response.data})
            }).catch(error => {
            console.log(error)
            this.setState({'project': []})
        })

        axios.get('http://127.0.0.1:8000/api/to_do/')
            .then(response => {
                this.setState({'to_do': response.data})
            }).catch(error => {
            console.log(error)
            this.setState({'to_do': []})
        })
    }


    componentDidMount() {
        this.get_token_from_cookies()
        // this.load_data()
    }

    render() {
        return (
            <div>
                <Router>
                    <header>
                        <nav className="navbar navbar-expand-md navbar-dark fixed-top bg-warning">
                            <a className="navbar-brand" href="#">GeekBrains</a>
                            <ul className="navbar-nav mr-auto">
                                <button className="btn btn-outline-success" type="button"><Link to ='/'>Users</Link></button>
                                <button className="btn btn-outline-success" type="button"><Link to ='/project'>Projects list</Link></button>
                                <button className="btn btn-outline-success" type="button"><Link to ='/ToDo'>What's need to do list</Link></button>
                                <button className="btn btn-outline-success" type="button"><Link to ='/projects/create'>Create project</Link></button>
                                <button className="btn btn-outline-success" type="button"><Link to ='/todos/create'>Create task</Link></button>
                                <button className="btn btn-outline-success" type="button"> {this.is_authenticated() ? <button onClick={() => this.logout()}>Logout</button> :
                                    <Link to='/login'>Login </Link>}
                                </button>
                            </ul>
                        </nav>
                    </header>
                    <main role="main" class="flex-shrink-0">
                        <div className="container">
                            <Switch>
                                <Route exact path='/' component={() => <UserList users={this.state.users} auth={this.is_authenticated()}
                                                                              deleteUser={(id)=> this.deleteUser(id)}/>}/>


                                <Route exact path='/project' component={() => <ProjectsList projects={this.state.project} auth={this.is_authenticated()}
                                                                              deleteProject={(id)=> this.deleteProject(id)}/>}/>

                                <Route exact path='/ToDo' component = {() =>  <ToDoList ToDos={this.state.to_do} auth={this.is_authenticated()}
                                                                                               deleteTODO={(id) => this.deleteTODO(id)}/>}/>


                                <Route exact path='/projects/create'> <ProjectForm users_list={this.state.users}
                                                                                   createProject={(name, repo_link, user) => this.createProject(name, repo_link, user)}/></Route>


                                <Route exact path='/todos/create'> <TODOForm to_do={this.state.to_do}
                                                                             createTODO={(initial_project, note, creator) => this.createTODO(initial_project, note, creator)}/></Route>


                                <Route exact path='/login'> <LoginForm get_token={(username, password) => this.get_token(username, password)}/> </Route>

                                <Route component={NotFound404}/>
                            </Switch>
                        </div>
                    </main>
                    <FooterPage/>
                </Router>
            </div>
        )
    }
}


export default App;
