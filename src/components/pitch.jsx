import React from 'react';
import { pitch } from '../assets';
import './PitchVideo.css'; // Import a separate CSS file for styling

const PitchVideo = ( {isMuted, toggleMute}) => {
  const videoRef = React.useRef(null)

  React.useEffect(() => {
    if (videoRef.current) {
      videoRef.current.muted = isMuted
    }

    if (!isMuted){
      videoRef.current.currentTime = 0
      videoRef.current.play()
    }
  }, [isMuted])

  return (
    <div className="video-container">
      <video
      ref = {videoRef}
        className="video rounded-md"
        loop
        autoPlay
        muted = {isMuted}
        playsInline
        
      >
        <source src={pitch} type="video/mp4" />
      </video>
    </div>
  );
};

export default PitchVideo;
