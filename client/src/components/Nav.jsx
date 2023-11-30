import { useState, useEffect } from "react";
// import { BrowserRouter, Routes, Route } from "react-router-dom";
// // import Home from "./Home";
// import Collection from "./Collection";
// import Favorites from "./Favorites";
// import Add_recipe from "./Add-recipe";
import { Link } from "react-router-dom";
import Bigbites from "../assets/Bigbites.png";
import Button from "./Button";

function Nav() {
  const logo = Bigbites;

  // sets to true or false depending on the size of the window
  let [open, setOpen] = useState(window.innerWidth > 768);

  // handles the toggle on the menu icon and close icon
  const handleToggle = () => {
    setOpen((open) => !open);
  };
  let Links = [
    { name: "HOME", link: "/home" },
    { name: "COLLECTION", link: "/collection" },
    { name: "PROFILE", link: "/profile" },
  ];

  // here we want to add an event listener for window size
  useEffect(() => {
    const handleWindowResize = () => {
      setOpen(window.innerWidth > 768);
    };

    window.addEventListener("resize", handleWindowResize);

    return () => {
      window.removeEventListener("resize", handleWindowResize);
    };
  }, []); // Adding an empty dependency array ensures this effect runs only once

  return (
    <div className=" shadow-md  bg-opacity-50 relative w-full top-0 left-0">
      <div className="md:flex items-center justify-between bg-gradient-to-r from-white to-orange-100 py-4 md:px-10 px-7">
        <div
          className="font-bold text-2xl cursor-pointer flex items-center font-[Poppins]
        text-gray-800"
        >
          <span className="text-3x1 text-orange-500 mr-1 pt-2 ">
            <img className="w-40" src={logo} />
          </span>
        </div>
        <div
          onClick={handleToggle}
          className="text-3x1 absolute right-8 top-6 cursor-pointer md:hidden"
        >
          <ion-icon name={open ? "close" : "menu"}></ion-icon>
        </div>
        <ul
          className={`md:flex rounded-md md:items-center md:pb-0 pb-12 absolute md:static bg-white md:z-auto z-{-1} left-0 w-full md:w-auto md:pl-0 pl-9 transition-all duration-500 ease-in ${
            open ? "top-20 opacity-100" : "opacity-0 pointer-events-none"
          }`}
          style={{ top: "calc(100% + 1rem)" }}
        >
          {Links.map((linkItem) => (
            <li key={linkItem.name} className="md:ml-8 text-xl md:my-0 my-7 ">
              <Link
                to={linkItem.link}
                className="text-orange-500 hover:text-orange-300 duration-500"
              >
                {linkItem.name}
              </Link>
            </li>
          ))}
          <Button>Log in</Button>
        </ul>
      </div>
    </div>
  );
}

export default Nav;
