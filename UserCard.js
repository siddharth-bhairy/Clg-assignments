import React from "react";
import PropTypes from "prop-types";

const UserCard = ({ name, age, isAdmin, hobbies }) => {
  return (
    <div style={{ border: "1px solid gray", padding: "10px", width: "250px", margin: "10px" }}>
      <h3>{name}</h3>
      <p>Age: {age}</p>
      <p>Role: {isAdmin ? "Admin" : "User"}</p>
      <p>Hobbies: {hobbies.join(", ")}</p>
    </div>
  );
};

// --------------------
// Prop Types Validation
// --------------------
UserCard.propTypes = {
  name: PropTypes.string.isRequired,     // Must be a string and required
  age: PropTypes.number.isRequired,      // Must be a number and required
  isAdmin: PropTypes.bool,                // Optional boolean
  hobbies: PropTypes.arrayOf(PropTypes.string) // Array of strings
};

// Default props if not provided
UserCard.defaultProps = {
  isAdmin: false,
  hobbies: []
};

export default UserCard;