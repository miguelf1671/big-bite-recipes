function Button(props) {
  return (
    <>
      <button className="bg-orange-500 text-white font-[Poppins] py-2 px-6 rounded md:ml-8 hover:bg-orange-300 duration-500 ">
        {props.children}
      </button>
    </>
  );
}

export default Button;
