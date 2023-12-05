import { useEffect, useState } from "react";
import Nav from "./Nav";
import Card from "./Card";

function Profile() {
  const [favoriteRecipes, setFavoriteRecipes] = useState([]);
  const [submittedRecipes, setSubmittedRecipes] = useState([]);

  useEffect(() => {
    fetch("/api/favorited-recipes")
      .then((res) => res.json())
      .then((data) => setFavoriteRecipes(data));
  }, []);

  useEffect(() => {
    fetch("/api/submitted-recipes")
      .then((res) => res.json())
      .then((data2) => setSubmittedRecipes(data2));
  }, []);
  return (
    <>
      <div>
        <Nav />
      </div>
      <div>
        <h1 className="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white">
          Favorites
        </h1>
      </div>
      <div className="grid grid-cols-3">
        {favoriteRecipes.map((recipe, index) => (
          <Card key={index} recipe={recipe} />
        ))}
      </div>
      <div>
        <h1 className="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white">
          Submitted
        </h1>
      </div>
      <div className="grid grid-cols-3">
        {submittedRecipes.map((recipe, index) => (
          <Card key={index} recipe={recipe} />
        ))}
      </div>
    </>
  );
}

export default Profile;
