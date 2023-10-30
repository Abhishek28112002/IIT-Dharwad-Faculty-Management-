import React from 'react';

function Course() {
  // Sample course data
  const courses = [
    {
      course_id: 1,
      course_name: 'Introduction to React',
      course_dep: 'Computer Science',
      teacher: 'John Doe',
      batch: '2023',
      semester: 'Spring',
    },
    // Add more course objects as needed
  ];

  return (
    <div style={{padding:'24px'}}>
      <h2>Courses</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Course ID</th>
            <th>Course Name</th>
            <th>Department</th>
            <th>Teacher</th>
            <th>Batch</th>
            <th>Semester</th>
          </tr>
        </thead>
        <tbody>
          {courses.map((course, index) => (
            <tr key={index}>
              <td>{course.course_id}</td>
              <td>{course.course_name}</td>
              <td>{course.course_dep}</td>
              <td>{course.teacher}</td>
              <td>{course.batch}</td>
              <td>{course.semester}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Course;
