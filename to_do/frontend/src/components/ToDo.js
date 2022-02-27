import React from 'react'


const ToDoItem = ({ToDo}) => {
   return (
       <tr>
           <td>
               {ToDo.initial_project}
           </td>
           <td>
               {ToDo.note}
           </td>
           <td>
               {ToDo.creation_date}
           </td>
           <td>
               {ToDo.update_date}
           </td>
           <td>
               {ToDo.creator}
           </td>

       </tr>
   )
}

const ToDoList = ({ToDos}) => {
   return (
       <table>
           <th>
               Initial project
           </th>
           <th>
               Note
           </th>
           <th>
               Creation date
           </th>

           <th>
               Update date
           </th>
           <th>
               Creator
           </th>


           {ToDos.map((ToDo) => <ToDoItem ToDo={ToDo} />)}
       </table>
   )
}


export default ToDoList