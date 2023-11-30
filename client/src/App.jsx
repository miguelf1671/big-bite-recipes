import { BrowserRouter, Route, Routes } from "react-router-dom";
// import Nav from "./components/Nav";
import Home from "./components/Home";
import Collection from "./components/Collection";
import Profile from "./components/Profile";

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        {/* <Nav /> */}
        <Routes>
          <Route path="/home" element={<Home />} />
          <Route path="/collection" element={<Collection />} />
          <Route path="/profile" element={<Profile />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
