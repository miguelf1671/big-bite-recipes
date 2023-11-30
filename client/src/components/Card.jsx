import { useState, useEffect } from "react";

function Card() {
  const [recipeList, setRecipeList] = useState([]);

  const [isFlipped, setIsFlipped] = useState(false);
  const [isBouncing, setIsBouncing] = useState(false);

  useEffect(() => {
    fetch("/api/recipes")
      .then((response) => response.json())
      .then((recipeData) => setRecipeList(recipeData))
      .catch((error) => console.error(error));
  }, []);

  const handleFlip = () => {
    setIsFlipped(!isFlipped);
    setIsBouncing(true);
    setTimeout(() => {
      setIsBouncing(false);
    }, 550); // Duration of the animation
  };
  return (
    <>
      {recipeList.map((recipe, index) => (
        <div
          key={index} // Add a unique key to each mapped element
          onClick={handleFlip}
          className={
            isBouncing
              ? "max-wsm rounded-lg flex flex-col justify-center transition-transform duration-100 object-scale-down border-8 border-orange-500 animate-[wiggle_0.55s_ease-in-out_both] overflow-hidden"
              : "max-wsm rounded-lg flex flex-col justify-center transition-transform duration-100 object-scale-down scale-100 border-8 border-orange-500 hover:border-orange-300 overflow-hidden"
          }
        >
          {isFlipped ? (
            <>
              <img
                src={recipe.image}
                className="mb-2 rounded-b-md border-b-8 border-orange-500 blur-lg brightness-75 duration-700"
              />
              <h1 className="absolute w-full text-center font-light">
                {recipe.ingredients}
              </h1>
              <h1 className="mb-2 text-2xl font-light tracking-light text-black pt-2 text-center duration-700">
                {recipe.directions}
              </h1>
            </>
          ) : (
            <>
              <img
                src={recipe.image}
                className="mb-2 rounded-b-md border-b-8 border-orange-500 duration-700 scale-100 hover:scale-110"
              />
              <h2 className="mb-2 text-2xl font-normal tracking-light text-black text-center mt-3">
                {recipe.name}
              </h2>
            </>
          )}
        </div>
      ))}
    </>
  );
}

export default Card;
