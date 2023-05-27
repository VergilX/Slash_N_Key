import {BrowserRouter as Router,Switch,Route} from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './components/pages/Home';

function App() {

  return (
    <>
    <Router>
    <Navbar/>
     <Switch>
     <Route exact path = "/" element = {<Home />} />
     </Switch>
     </Router>
    </>
  );
}

export default App;