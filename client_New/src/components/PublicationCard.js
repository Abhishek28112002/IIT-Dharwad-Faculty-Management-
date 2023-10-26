import React from 'react'

import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
function Publication({data}) {
  return (
    <Card>
    <Card.Body>
      <Card.Title>{data.title}</Card.Title>
      <Card.Text>
        By  {data.name.map((prof) => (
            <span key={prof}>
              {prof} {','}
            </span>
          ))}
      {''}  Departmant of {data.department}
      </Card.Text>
      <div style={{display:'flex',gap:'8px',alignItems:'center'}}>
      <Button variant="primary">Check it</Button>
      <Card.Text>
        {data.publication_dates}
        </Card.Text>
      </div>
    </Card.Body>
  </Card>
  )
}

export default Publication
