import React from 'react';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
function ResearchCard({ data }) {
 
  return (
    <Card border="primary" style={{ width: '18rem' }}>
      <Card.Header>{data.research_area}</Card.Header>
      <Card.Body>
        <div style={{display:'flex',gap:'8px',alignItems:'center'}}>
        <Card.Title>Research Topic is {data.research_topic} </Card.Title>
        <div className={data.status}>{data.status}</div>
        </div>
        <Card.Text>
          This research have active participation from {' '}
          {data.researchers?.map((prof) => (
            <span key={prof.researcher_id}>
              {prof.name} from {prof.department} department.
            </span>
          ))}
        </Card.Text>
      </Card.Body>
    </Card>
  );
}

export default ResearchCard;
