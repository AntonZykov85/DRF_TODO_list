import React from 'react'


const UserItem = ({user, deleteUser}) => {
   return (
       <tr>
           <td>{user.id}</td>
           <td>{user.username}</td>
           <td>{user.first_name}</td>
           <td>{user.last_name}</td>
           <td>{user.email}</td>
           <td>
               <button onClick={() => deleteUser(user.id)} type='button'>Delete</button>
           </td>
       </tr>
   )
}

const UserList = ({users, deleteUser}) => {
   return (
       <table>
           <th>
               id
           </th>
           <th>
               Username
           </th>
           <th>
               First name
           </th>
           <th>
               Last Name
           </th>
           <th>
               E-mail
           </th>

           {users.map((user) => <UserItem user={user} deleteUser={deleteUser}/>)}
       </table>
   )
}


export default UserList