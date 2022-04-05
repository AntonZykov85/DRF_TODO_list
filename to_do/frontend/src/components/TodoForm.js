import React from "react";

class TODOForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {initial_project: '', note: '', creator: ''}
    }

    //  handleTODOChange(event) {
    //     if (!event.target.selectedOptions) {
    //         this.setState({
    //             'initial_project': []
    //         })
    //         return;
    //     }
    //     let initial_project_list = []
    //     for (let i = 0; i < event.target.selectedOptions.length; i++) {
    //         initial_project_list.push(event.target.selectedOptions.item(i).value)
    //     }
    //     this.setState({
    //         'initial_project': initial_project_list
    //     })
    // }


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
                {/*<div>*/}
                {/*        <div className="form-group">*/}
                {/*            <label htmlFor="initial_project">Список проектов</label>*/}
                {/*                <select className="select" name="initial_project" multiple onChange={(event) => this.handleTODOChange(event)}>*/}
                {/*                    {this.props.to_do.map((item) => <option value={item.id}> {item.creator}</option>)}*/}

                {/*                </select>*/}
                {/*        </div>*/}
                {/*</div>*/}


                <div className="form-group">
                    <label htmlFor="login">Введите id проекта</label>
                    <input type="text" className="form-control" name="initial_project"
                           onChange={(event) => this.handleChange(event)}/>
                </div>


                <div className="form-group">
                    <label for="text">Содержание проекта</label>
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