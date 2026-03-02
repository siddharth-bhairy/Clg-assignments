// import React, { useState } from "react";
// import ProgressBar from "./progressbar";

// function App() {
//   const [progress, setProgress] = useState(40);

//   return (
//     <div style={{ padding: "40px" }}>
//       <h2>Custom Progress Bar</h2>

//       <ProgressBar progress={progress} />

//       <br />

//       <button onClick={() => setProgress(prev => Math.min(prev + 10, 100))}>
//         Increase
//       </button>

//       <button onClick={() => setProgress(prev => Math.max(prev - 10, 0))}>
//         Decrease
//       </button>
//     </div>
//   );
// }

// export default App;

import React from "react";
import UserCard from "./UserCard";

function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h2>User List</h2>
      <UserCard
        name="Alice"
        age={25}
        isAdmin={true}
        hobbies={["Reading", "Gaming"]}
      />

      <UserCard
        name="Bob"
        age={30}
        // isAdmin not provided → default false
        // hobbies not provided → default empty array
      />
    </div>
  );
}

export default App;