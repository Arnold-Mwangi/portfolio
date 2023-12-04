import React, { useState, useEffect } from "react";
import "./RotatingIcons.css"; // Create a CSS file for styling

const RotatingIcon = ({ icon }) => {
  const [rotation, setRotation] = useState(0);

  useEffect(() => {
    const intervalId = setInterval(() => {
      setRotation((prevRotation) => prevRotation + 1);
    }, 16); // Adjust the interval as needed for the desired rotation speed

    return () => clearInterval(intervalId);
  }, []);

  return (
    <div className="rotating-icon" style={{ transform: `rotate(${rotation}deg)` }}>
      <img src={icon} alt="Icon" />
    </div>
  );
};

export default RotatingIcon;
