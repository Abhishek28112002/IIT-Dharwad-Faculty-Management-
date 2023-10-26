-- Create Instructor table
CREATE TABLE Instructor (
    instructor_id int not null,
    name varchar(255) not null,
    department varchar(255) not null,
    type varchar(255) default 'Permanent',
    salary int default 0,
    email varchar(255) not null, 
    phone_number varchar(12),
    performance_score int default 0,
    primary key (instructor_id)
);
-- Create Specialization table
CREATE TABLE Specialization (
    instructor_id int not null references Instructor(instructor_id),
    specialization varchar(255) not null
);
-- Create Courses table
CREATE TABLE Courses (
    course_id int not null,
    course_name varchar(255) not null,
    course_description varchar(255) not null,
    department varchar(255) not null,
    primary key (course_id)
);

-- Create Feedback table
CREATE TABLE Feedback (
    course_id int not null references Courses(course_id),
    avg_rating_teaching int default 0,
    avg_rating_behaviour int default 0,
    avg_rating_knowledge int default 0,
    batch_year int not null,
    semester int not null,
    primary key (course_id, batch_year, semester)
);

-- Create Teaches table
CREATE TABLE Teaches (
    course_id int not null references Courses(course_id),
    instructor_id int not null references Instructor(instructor_id),
    batch_year int not null,
    semester int not null,
    primary key (course_id, instructor_id)
);

-- Create Perv_Teaches table
CREATE TABLE Perv_Teaches (
    course_id int not null,
    instructor_id int not null references Instructor(instructor_id),
    collage_name varchar(100) not null,
    batch_year int not null,
    semester int not null,
    primary key (course_id, instructor_id)
);

-- Create Achievements table
CREATE TABLE Achievements (
    instructor_id int not null references Instructor(instructor_id),
    award_year int not null,
    award_name varchar(1000) not null,
    reason varchar(10000)
);

-- Create Research table
CREATE TABLE Research (
    research_area varchar(100) not null,
    status varchar(100) default 'active',
    budget varchar(100) default '',
    research_topic varchar(100) not null
);

-- Create Researcher table
CREATE TABLE Researcher (
    instructor_id int not null references Instructor(instructor_id),
    research_topic varchar(100) not null,
    research_area varchar(100)
);

-- Create MoreInfo table
CREATE TABLE MoreInfo (
    instructor_id int not null references Instructor(instructor_id),
    graduated_college varchar(100) not null,
    graduated_year int not null,
    born varchar(20),
    about TEXT -- Using TEXT for a longer text column
);

-- Create PositionsOfResponsibility table
CREATE TABLE PositionsOfResponsibility (
    por_id int not null,
    instructor_id int not null references Instructor(instructor_id),
    position_name varchar(255) not null,
    start_date date,
    end_date date,
    primary key (por_id)
);

-- Create Publications table
CREATE TABLE Publications (
    publication_id int not null,
    instructor_id int not null references Instructor(instructor_id),
    title varchar(255) not null,
    publication_date date,
    research_paper_id int not null,
    publication_type varchar(100),
    primary key (publication_id)
);
