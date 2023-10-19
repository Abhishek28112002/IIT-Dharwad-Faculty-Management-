import React from 'react';

const dummyInstructor = {
  name: 'John Doe',
  email: 'john.doe@example.com',
  department: 'Computer Science',
  type: 'Permanent',
  salary: 80000,
  phone_number: '+1 123-456-7890',
  performance_score: 95,
  specializations: [
    { id: 1, name: 'Web Development' },
    { id: 2, name: 'Database Management' },
  ],
  courses: [
    { course_id: 1, course_name: 'Web Development 101', department: 'Computer Science' },
    { course_id: 2, course_name: 'Database Design', department: 'Computer Science' },
  ],
  research: [
    { id: 1, topic: 'Machine Learning', area: 'Artificial Intelligence' },
    { id: 2, topic: 'Database Optimization', area: 'Databases' },
  ],
  publications: [
    { id: 1, title: 'Machine Learning Techniques', date: '2022-05-15', type: 'Research Paper' },
    { id: 2, title: 'Database Performance Optimization', date: '2021-10-20', type: 'Research Paper' },
  ],
  awards: [
    { id: 1, year: 2020, name: 'Outstanding Teacher Award', reason: 'Exceptional teaching performance' },
    { id: 2, year: 2019, name: 'Best Research Paper Award', reason: 'Innovative research contribution' },
  ],
};

const InstructorProfile = () => {
  return (
    <div className="container" style={{gap:'24px',display:'flex',flexDirection:'column'}}>
      <h2 className="my-4">Instructor Profile: {dummyInstructor.name}</h2>
      
      <div className="row">
        {/* Personal Information Section */}
        <div className="col-md-6">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Personal Information</h5>
              <p><strong>Email:</strong> {dummyInstructor.email}</p>
              <p><strong>Department:</strong> {dummyInstructor.department}</p>
              <p><strong>Type:</strong> {dummyInstructor.type}</p>
              <p><strong>Salary:</strong> {dummyInstructor.salary}</p>
              <p><strong>Phone Number:</strong> {dummyInstructor.phone_number}</p>
              <p><strong>Performance Score:</strong> {dummyInstructor.performance_score}</p>
            </div>
          </div>
        </div>

        {/* Specializations Section */}
        <div className="col-md-6">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Specializations</h5>
              <ul className="list-group">
                {dummyInstructor.specializations.map((specialization) => (
                  <li key={specialization.id} className="list-group-item">{specialization.name}</li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </div>

      {/* Courses Section */}
      <div className="row">
        <div className="col-md-6">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Courses</h5>
              <ul className="list-group">
                {dummyInstructor.courses.map((course) => (
                  <li key={course.course_id} className="list-group-item">
                    <strong>Course Name:</strong> {course.course_name}
                    <br />
                    <strong>Department:</strong> {course.department}
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>

        {/* Research Topics Section */}
        <div className="col-md-6">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Research Topics</h5>
              <ul className="list-group">
                {dummyInstructor.research.map((topic) => (
                  <li key={topic.id} className="list-group-item">
                    <strong>Topic:</strong> {topic.topic}
                    <br />
                    <strong>Area:</strong> {topic.area}
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </div>

      {/* Publications Section */}
      <div className="row">
        <div className="col-md-6">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Publications</h5>
              <ul className="list-group">
                {dummyInstructor.publications.map((publication) => (
                  <li key={publication.id} className="list-group-item">
                    <strong>Title:</strong> {publication.title}
                    <br />
                    <strong>Date:</strong> {publication.date}
                    <br />
                    <strong>Type:</strong> {publication.type}
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>

        {/* Awards Section */}
        <div className="col-md-6">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Awards</h5>
              <ul className="list-group">
                {dummyInstructor.awards.map((award) => (
                  <li key={award.id} className="list-group-item">
                    <strong>Year:</strong> {award.year}
                    <br />
                    <strong>Name:</strong> {award.name}
                    <br />
                    <strong>Reason:</strong> {award.reason}
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default InstructorProfile;