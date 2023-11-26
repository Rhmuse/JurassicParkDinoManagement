import Navbar from 'react-bootstrap/NavBar';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import NavDropdown from 'react-bootstrap/NavDropdown';
import { Link, Route, Routes } from 'react-router-dom';
import DashBoard from './Components/Dashboard';
import ViewAllDinosaurs from './Components/ViewAllDinosaurs';
import PostDinosaur from './Components/PostDinosaur';

function App() {
  return (
    <div className='app-container'>
      <Navbar expand="lg" className="bg-body-tertiary" >
        <Container>
          <Navbar.Brand href="/">Jurassic Park</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link href="/">Home</Nav.Link>
              <Nav.Link href="#link"></Nav.Link>
              <NavDropdown title="Manage Dinosaurs" id="basic-nav-dropdown">
                <NavDropdown.Item as={Link} to="/dinosaurs">All Dinosaurs</NavDropdown.Item>
                <NavDropdown.Item as={Link} to="/dinosaurs/post">Add New Dinosaur</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
              </NavDropdown>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
      <Routes>
        <Route path='/'>
          <Route index
            element={<DashBoard />}
          />
        </Route>
        <Route path='/dinosaurs'>
          <Route index
            element={<ViewAllDinosaurs />}
          />
          <Route path='post'
            element={<PostDinosaur />}
          />
        </Route>


      </Routes>
    </div>
  );
}

export default App;
