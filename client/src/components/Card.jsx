import PropTypes from "prop-types";
import { useState } from "react";

function Card({ recipe }) {
  const [isFlipped, setIsFlipped] = useState(false);
  const [liked, setLikes] = useState(false);

  const handleLike = () => {
    setLikes(!liked);
  };

  const handleFlip = () => {
    setIsFlipped(!isFlipped);
  };

  //   Put a button on every card that when clicked triggers an event. That event should call a fetch
  //   to the API endpoint for DELETEing the clicked recipe. This should be authorized so it shouldn't work
  //   if the user isn't logged in.

  return (
    <>
      <div
        onClick={handleFlip}
        className="max-wsm rounded-lg flex flex-col justify-center transform overflow-hidden border"
      >
        {isFlipped ? (
          <>
            <img
              src={recipe.image}
              className="mb-2  border-b-8 border-orange-500 blur-lg brightness-75 duration-700 cursor-pointer transform rotate-0 sm:rotate-45 md:rotate-90 lg:rotate-180 xl:-rotate-90..."
              alt="Flipped Recipe"
            />
            <h1 className="absolute w-full text-orange-50 text-center font-light">
              {recipe.ingredients}
            </h1>
            <button
              onClick={handleLike}
              className={liked ? "text-orange-500" : "text-black"}
            >
              <ion-icon name="heart-circle-outline"></ion-icon>
            </button>
            <h1 className="mb-2 text-2xl font-light tracking-light text-black pt-2 text-center duration-700">
              {recipe.directions}
            </h1>
          </>
        ) : (
          <>
            <img
              src={recipe.image}
              className="mb-2 border-b-8 border-orange-500 duration-700 scale-100 cursor-pointer "
              alt="Recipe"
            />
            <h2 className="mb-2 text-2xl font-normal tracking-light text-black text-center mt-3">
              {recipe.name}
            </h2>
          </>
        )}
      </div>
    </>
  );
}

Card.propTypes = {
  recipe: PropTypes.shape({
    image: PropTypes.string.isRequired,
    ingredients: PropTypes.string.isRequired,
    directions: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
    // Add more PropTypes for other properties if needed
  }).isRequired,
};

export default Card;
