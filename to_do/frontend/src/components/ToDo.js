import React from 'react'
import {Link} from "react-router-dom";


const ToDoItem = ({ToDo, deleteTODO}) => {
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

           <td>
               <button onClick={() => deleteTODO(ToDo.id)} type='button'>Delete</button>
           </td>
       </tr>
   )
}

const ToDoList = ({ToDos, deleteTODO}) => {
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


               {ToDos.map((ToDo) => <ToDoItem ToDo={ToDo} deleteTODO={deleteTODO}/>)}
           </table>
   )
}


export default ToDoList