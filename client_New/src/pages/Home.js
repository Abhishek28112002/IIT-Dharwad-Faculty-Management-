import React from 'react'
import ProfileCard from '../components/ProfileCard'
export default function Home() {
  return (
   <div >
<div style={{display: 'flex',  justifyContent:'flex-start', alignItems:'center',flexWrap:'wrap',gap:'24px'}}>
<ProfileCard/>
<ProfileCard/>
<ProfileCard/>
<ProfileCard/>
<ProfileCard/>
<ProfileCard/>
  </div>


   </div>
  )
}
