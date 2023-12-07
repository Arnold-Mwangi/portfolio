import React from 'react'
import { motion } from 'framer-motion'
import { styles } from '../styles'
import { sound } from '../assets'
import { audio } from '../assets'
import PitchVideo from './pitch';

const Hero = () => {
  const [isMuted, setMuted] = React.useState(true);

  const toggleMute = () => {
    setMuted((prevMute) => !prevMute);
  };


  return (

    <section className='relative w-full h-[500px] sm: hover:h-screen max-auto overflow-hidden'>
      <div className={`${styles.paddingX} absolute inset-0 top-[120px] max-w-7xl mx-auto flex flex-row items-start gap-5`}>
        <div className='flex flex-col justify-center items-center mt-5'>
          <div className='w-5 h-5 rounded-full bg-[#EA501A;]' />
          <div className='w-1 sm:h-80 h-40 violet-gradient' />
        </div>
        <div>
          <div className='absolute inset-0 z-[-50]'>
            <PitchVideo isMuted={isMuted} toggleMute={toggleMute} />
          </div>
          <div className='absolute inset-0 z-[-1] bg-[#EA501A]' style={{ background: 'linear-gradient(to right, #050816, transparent)' }}>

          </div>


          <h1 className={`${styles.heroHeadText} text-white`}>
            Hi, I'm
            <span className="text-[#EA501A]">
              &nbsp; Arnold
            </span>
          </h1>
          <p className={`${styles.heroSubText} mt-2 text-white-100`}>
            I develop Interactive, Dynamic, 3D Web Visuals<br className='lg:block hidden' />
            and Android applications using different Technologies.
          </p>

          <button
            className='bg-blend-lighten'
            onClick={toggleMute}
          >
            <span className='fill-slate-50'>
              {isMuted ?
                <img src={audio} alt='unMute' />
                :
                <img src={sound} alt='mute' />}
            </span>

          </button>
        </div>

      </div>


    </section >

  )


}

export default Hero