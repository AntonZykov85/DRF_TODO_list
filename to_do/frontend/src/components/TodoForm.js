import React from "react";

class TODOForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {initial_project: '', note: '', creator: ''}
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
        this.props.createTODO(this.state.initial_project, this.state.note, this.state.creator)
        console.log(this.state.initial_project)
        console.log(this.state.note)
        console.log(this.state.creator)
        event.preventDefault()
    }


    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="login">Наименование проекта</label>
                    <input type="text" className="form-control" name="initial_project"
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label for="text">Текст задания</label>
                    <input type="text" className="form-control" name="note"
                           onChange={(event) => this.handleChange(event)}/>
                </div>

                <div className="form-group">
                    <label for="creator">Создатель проекта</label>
                    <input type="number" className="form-control" name="creator"
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <input type="submit" className="btn btn-primary" value="Save"/>
            </form>
        );
    }
}

export default TODOForm