import React from 'react'
import {Link} from "react-router-dom";

const ProjectItem = ({project, deleteProject}) => {
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

           <td>
               <button onClick={() => deleteProject(project.id)} type='button'>Delete</button>
           </td>

       </tr>
   )
}

const ProjectsList = ({projects, deleteProject}) => {
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

           {projects.map((project) => <ProjectItem project={project} deleteProject={deleteProject}/>)}
       </table>
   )
}


export default ProjectsList