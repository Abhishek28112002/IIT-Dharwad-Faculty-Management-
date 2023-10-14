import React,{useState} from 'react'
import ProfileCard from '../components/ProfileCard'
import  Search from '../assets/Search.svg' 
import plus from '../assets/plus.svg'
import AddFaculty from '../components/AddFaculty'
export default function Home() {
  const [show, setShow] = useState(false);
  
  const handleClose = () => setShow(false);
  const handleShow = () => {console.log(show);setShow(true);}
  return (
    <div className='container mt-3'>
      {show && <AddFaculty handleClose={handleClose}/>}
   <div  style={{display:'flex',flexDirection:'column',gap:'24px'}}>
    <div style={{
  display: 'flex',
  alignItems: 'flex-start',
  gap: '24px',
  justifyContent:'space-between',
  alignSelf: 'stretch'
}}>
  
      
      <div style={{
        display: 'flex',
        width: '320px',
        padding: '10px 14px',
        alignItems: 'center',
        gap: '8px',
        alignSelf: 'stretch',
        justifyContent: 'center',
        borderRadius: 'var(--radius-medium, 8px)',
        background:'#fff'
      }} className="container_Style">
        <img src={Search} alt="Search Icon" style={{width:'24px'}} />
        <input
          type="text"
          style={{
            border: 'none',
            width: '100%',
          }}
          placeholder="Search by Name, Email"
        />
  </div>
<div style={{color:'black',display:'flex',alignItems:'center',gap:'12px'}}>
<div className='Box'>
  Sort by Departmant
</div>

</div>
<div style={{color:'black',display:'flex',alignItems:'center',gap:'12px',background:'#167bff',color:'white'}}className='Box' onClick={handleShow}>
<img src={plus} style={{width:'24px'}}/>Add 
</div>
</div>

<div style={{display: 'flex',  justifyContent:'flex-start', alignItems:'center',flexWrap:'wrap',gap:'24px'}}>
<ProfileCard/>
<ProfileCard/>
<ProfileCard/>
<ProfileCard/>
<ProfileCard/>
<ProfileCard/>
  </div>


   </div>
   </div>
  )
}
