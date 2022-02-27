import React from 'react';
import { MDBContainer, MDBFooter } from "mdbreact";
import UserList from "./users";

const FooterPage = () => {
  return (
      <fotter class="fotter">
        <MDBContainer fluid>
          &copy; {new Date().getFullYear()} Copyright: <a href="https://gb.ru"> GeekBrains </a>
        </MDBContainer>
      </fotter>
  );
}

export default FooterPage;