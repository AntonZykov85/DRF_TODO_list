import React from "react";

class ProjectForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {name: '', repo_link: '', users: []}
    }

    handleProjectChange(event) {
        if (!event.target.selectedOptions) {
            this.setState({
                'user': []
            })
            return;
        }
        let users_list = []
        for (let i = 0; i < event.target.selectedOptions.length; i++) {
            users_list.push(event.target.selectedOptions.item(i).value)
        }
        this.setState({
            'user': users_list
        })
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        )
        console.log(event.target.name, event.target.value)
    }

    handleSubmit(event) {
        this.props.createProject(this.state.name, this.state.repo_link, this.state.users)
        console.log(this.state.name)
        console.log(this.state.repo_link)
        console.log(this.state.users)
        event.preventDefault()
    }


    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label htmlFor="login">Название проекта</label>
                    <input type="text" className="form-control" name="name"
                           value={this.state.name} onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label htmlFor="link_to repo">Ссылка на репозиторий</label>
                    <input type="text" className="form-control" name="repo_link"
                           value={this.state.repo_link} onChange={(event) => this.handleChange(event)}/>
                </div>

                <div>
                    <div className="form-group">
                        <label htmlFor="user">Список пользователей</label>
                        <select className="select" name="user" multiple onChange={(event) => this.handleProjectChange(event)}>
                            {this.props.users.map((item) => <option value={item.id}> {item.username}</option>)}

                        </select>
                    </div>
                </div>

                <input type="submit" className="btn btn-primary btn-lg btn-block" value="Save"/>
            </form>
        );
    }
}

export default ProjectForm