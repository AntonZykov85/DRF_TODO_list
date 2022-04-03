import React from "react";

class TODOForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {initial_project: '', note: '', creator: []}
    }

    handleCreatorChange(event) {
       if(!event.target.selectedOptions){
            this.setState({
                'creator':[]
            })
            return;
        }

        let  creators = []
        for (let i = 0; i < event.target.selectedOptions.length;i++){
            creators.push(event.target.selectedOptions.item(i).value)

        }
        this.setState({
            'creator': creators
        })
    }


    handleChange(event){
        this.setState(
            {
                [event.target.name]:event.target.value
            }
        )
         console.log(event.target.name, event.target.value)
         console.log(this.state.initial_project)
         console.log(this.state.note)
         console.log(this.state.creator)
    }


    handleSubmit(event){
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
                    <label for="login">Название проекта</label>
                    <input type="text" className="form-control" name="initial_project"
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label for="text">Текст задачи</label>
                    <input type="text" className="form-control" name="note"
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                {/*<div className="form-group">*/}
                {/*    <label for="creator">Создатель задачи</label>*/}
                {/*    <input type="number" className="form-control" name="creator"*/}
                {/*           onChange={(event) => this.handleChange(event)}/>*/}
                {/*</div>*/}

                <select name="creator" multiple onChange={(event) => this.handleCreatorChange(event)}>
                    {this.props.todos.map((item) => <option value={item.id}> {item.username} </option>)}

                </select>


                <input type="submit" className="btn btn-primary" value="Save"/>
            </form>
        );
    }
}

export default TODOForm