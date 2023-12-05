import { BrowserRouter, Route, Routes } from "react-router-dom";
// import Nav from "./components/Nav";
import Home from "./components/Home";
import Collection from "./components/Collection";
import Profile from "./components/Profile";
import Sign_up from "./components/Sign_up";

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        {/* <Nav /> */}
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/collection" element={<Collection />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/signup" element={<Sign_up />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
