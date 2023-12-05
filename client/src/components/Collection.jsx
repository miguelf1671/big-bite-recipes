import { useEffect, useState } from "react";
import Nav from "./Nav";
import Card from "./Card";

function Collection() {
  const [recipeList, setRecipeList] = useState([]);

  useEffect(() => {
    fetch("/api/recipes")
      .then((response) => response.json())
      .then((recipeData) => setRecipeList(recipeData))
      .catch((error) => console.error(error));
  }, []);

  console.log("hellodds");
  return (
    <>
      <div>
        <Nav />
      </div>
      <div className="grid grid-cols-3">
        {recipeList.map((recipe, index) => (
          <Card key={index} recipe={recipe} />
        ))}
      </div>
    </>
  );
}

export default Collection;
