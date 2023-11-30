// import { useEffect, useState } from "react";
import Nav from "./Nav";
import Card from "./Card";

function Collection() {
  console.log("hellodds");
  return (
    <>
      <div>
        <Nav />
        <div className="grid grid-cols-4">
          <Card />
        </div>
      </div>
    </>
  );
}

export default Collection;
