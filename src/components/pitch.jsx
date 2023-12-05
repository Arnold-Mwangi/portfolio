// PitchVideo.js
import React from 'react';
import { pitch } from '../assets';

const PitchVideo = () => {
  return (
    <div className="w-full h-full">
      <video
        className="w-full h-full object-cover"
        loop
        autoPlay
        
      >
        <source src={pitch} type="video/mp4" />
      </video>
    </div>
  );
};

export default PitchVideo;
