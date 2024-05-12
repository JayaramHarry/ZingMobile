const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

// Define roles
const roles = {
  SuperAdmin: 0,
  Admin: 1,
  Teacher: 2,
  Student: 3
};

// Simulated database
let colleges = [];

// College class
class College {
  constructor(name, state, city, campus, section) {
    this.name = name;
    this.state = state;
    this.city = city;
    this.campus = campus;
    this.section = section;
    this.students = [];
  }
}

// Middleware for role-based access control
function authorize(role) {
  return (req, res, next) => {
    // Simulated logic to check if user has permission based on role
    // For simplicity, assuming all users have full access in this example
    next();
  };
}

// Routes
// Read data
app.get('/students', authorize('SuperAdmin'), (req, res) => {
  // Return all students data
  const allStudents = colleges.flatMap(college => college.students);
  res.json(allStudents);
});

// Write data
app.post('/college/:collegeId/students', authorize('Admin'), (req, res) => {
  const collegeId = parseInt(req.params.collegeId);
  const college = colleges[collegeId];
  if (!college) return res.status(404).send("College not found");

  const student = req.body;
  college.students.push(student);
  res.status(201).json(student);
});

// Update data
app.put('/college/:collegeId/student/:studentId', authorize('Teacher'), (req, res) => {
  const collegeId = parseInt(req.params.collegeId);
  const studentId = parseInt(req.params.studentId);

  const college = colleges[collegeId];
  if (!college) return res.status(404).send("College not found");

  const student = college.students.find(s => s.id === studentId);
  if (!student) return res.status(404).send("Student not found");

  // Update student data
  const updatedStudent = req.body;
  Object.assign(student, updatedStudent);

  res.json(student);
});

// Delete data
app.delete('/college/:collegeId/student/:studentId', authorize('Admin'), (req, res) => {
  const collegeId = parseInt(req.params.collegeId);
  const studentId = parseInt(req.params.studentId);

  const college = colleges[collegeId];
  if (!college) return res.status(404).send("College not found");

  const index = college.students.findIndex(s => s.id === studentId);
  if (index === -1) return res.status(404).send("Student not found");

  college.students.splice(index, 1);
  res.sendStatus(204);
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
