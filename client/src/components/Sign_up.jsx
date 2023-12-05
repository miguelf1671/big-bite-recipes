import { useState, useEffect } from "react";
import { Form } from "semantic-ui-react";
import Nav from "./Nav";
// import { useHistory } from "react-router-dom";

function Sign_up() {
  const [isSignUp, setIsSignUp] = useState(false);
  const [formDataSignUp, setFormDataSignUp] = useState({
    username: "",
    email: "",
    password: "",
  });
  const [formDataLogin, setFormDataLogin] = useState({
    username: "",
    password: "",
  });
  const [allUsers, setAllUsers] = useState([]);

  useEffect(() => {
    fetch("/api/users")
      .then((res) => res.json())
      .then((userData) => setAllUsers(userData));
  }, []);

  const handleAddUser = (newUser) => {
    fetch("/api/signup", {
      method: "POST",
      credentials: "include",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newUser),
    })
      .then((res) => res.json())
      .then((newlyAddedUser) => {
        setAllUsers([...allUsers, newlyAddedUser]);
        // Additional logic after sign-up if needed
      });
  };

  // const history = useHistory();

  const handleLogin = () => {
    fetch("/api/login", {
      method: "POST",
      credentials: "include",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formDataLogin),
    })
      .then((res) => res.json())
      .then((loggedInUser) => {
        // Additional logic after login if needed
        // history.push("/api/profile");
        window.location.href = "/profile";
      })
      .catch((error) => {
        console.error("Error logging in:", error);
        // Handle login error (e.g., display an error message)
      });
  };

  const handleSignUpSubmit = (e) => {
    e.preventDefault();
    const newUser = {
      username: formDataSignUp.username,
      email: formDataSignUp.email,
      password: formDataSignUp.password,
    };
    handleAddUser(newUser);
  };

  const handleLoginSubmit = (e) => {
    e.preventDefault();
    handleLogin();
  };

  const handleSignUpChange = (e) => {
    const { name, value } = e.target;
    setFormDataSignUp((prevFormData) => ({
      ...prevFormData,
      [name]: value || "",
    }));
  };

  const handleLoginChange = (e) => {
    const { name, value } = e.target;
    setFormDataLogin((prevFormData) => ({
      ...prevFormData,
      [name]: value || "",
    }));
  };

  const handleToggle = () => {
    setIsSignUp(!isSignUp);
    setFormDataSignUp({ username: "", password: "" });
    setFormDataLogin({ username: "", password: "" });
  };

  return (
    <>
      <div>
        <Nav />
      </div>

      <div className="flex justify-center items-center">
        {isSignUp ? (
          <Form
            className="bg-orange-200 shadow-md rounded px-8 pt-6 pb-8 mb-4"
            onSubmit={handleSignUpSubmit}
          >
            <Form.Group widths="equal">
              <div className="mb-4">
                <label
                  className="block text-black text-sm font-bold mb-2"
                  htmlFor="username"
                >
                  Username
                </label>
                <Form.Input
                  className="block"
                  name="username"
                  placeholder="Enter Username"
                  onChange={handleSignUpChange}
                  value={formDataSignUp.username}
                />
              </div>
              <div className="mb-4"></div>
              <div className="mb-6">
                <label
                  className="block text-black text-sm font-bold mb-2"
                  htmlFor="password"
                >
                  Password
                </label>
                <Form.Input
                  className="block"
                  name="password"
                  type="password"
                  placeholder="Enter Password"
                  onChange={handleSignUpChange}
                  value={formDataSignUp.password}
                />
              </div>
            </Form.Group>
            <div className="flex items-center justify-center">
              <Form.Button
                type="submit"
                className="rounded py-2 px-4 transition duration-500 ease-in-out bg-orange-500 hover:bg-orange-700 hover:-translate-y-1 hover:scale-110..."
              >
                Sign Up
              </Form.Button>
            </div>
          </Form>
        ) : (
          <Form
            className="bg-orange-200 shadow-md rounded px-8 pt-6 pb-8 mb-4"
            onSubmit={handleLoginSubmit}
          >
            <Form.Group widths="equal">
              <div className="mb-4">
                <label
                  className="block text-black text-sm font-bold mb-2"
                  htmlFor="username"
                >
                  Username
                </label>
                <Form.Input
                  className="block"
                  name="username"
                  placeholder="Enter Username"
                  onChange={handleLoginChange}
                  value={formDataLogin.username}
                />
              </div>
              <div className="mb-6">
                <label
                  className="block text-black text-sm font-bold mb-2"
                  htmlFor="password"
                >
                  Password
                </label>
                <Form.Input
                  className="block"
                  name="password"
                  type="password"
                  placeholder="Enter Password"
                  onChange={handleLoginChange}
                  value={formDataLogin.password}
                />
              </div>
            </Form.Group>
            <div className="flex items-center justify-center">
              <Form.Button
                type="submit"
                className="rounded py-2 px-4 transition duration-500 ease-in-out bg-orange-500 hover:bg-orange-700 hover:-translate-y-1 hover:scale-110..."
              >
                Login
              </Form.Button>
            </div>
          </Form>
        )}
        <button onClick={handleToggle}>
          {isSignUp ? "Switch to Login" : "Switch to Sign Up"}
        </button>
      </div>
    </>
  );
}

export default Sign_up;
