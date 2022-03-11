import React from 'react'
import {Link} from "react-router-dom";

const ProjectItem = ({project}) => {
   return (
       <tr>
           <td>
              <Link to={`/project/${project.id}`}>{project.name}</Link>
           </td>

           <td>
               {project.repo_link}
           </td>

           <td>
               {project.users}
           </td>

       </tr>
   )
}

const ProjectsList = ({projects}) => {
   return (
       <table>
           <th>
               Project name
           </th>

           <th>
               Repositorium link
           </th>

           <th>
               Users
           </th>
           {projects.map((project) => <ProjectItem project={project} />)}
       </table>
   )
}


export default ProjectsList