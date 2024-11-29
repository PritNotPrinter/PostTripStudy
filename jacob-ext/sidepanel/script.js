// Hardcoded course data with notes and assignments for each course
const courseData = {
  ICS3UO: {
    notes:
      "Note: Study Chapter 5 on Python Functions. Remember to revise syntax for loops.",
    assignments: "Assignment: Complete Python Quiz (due in 2 weeks)",
    tests: "Test: Midterm Exam covering Chapters 1-4 (Date: Nov 15)",
  },
  SCH3UR: {
    notes:
      "Note: Review Chapter 7 on Chemical Reactions and balancing equations.",
    assignments: "Assignment: Lab Report on Chemical Reactions (due in 3 days)",
    tests: "Test: Final Exam on Chapters 1-10 (Date: Dec 5)",
  },
  JacobTest: {
    notes:
      "Note: Prepare for the mock test. Review past quizzes and practice problems.",
    assignments:
      "Assignment: Submit a reflection on the mock test (due in 5 days)",
    tests: "Test: Mock Test (Date: Nov 10)",
  },
  CLU3MO: {
    notes:
      "Note: Read Chapter 3 on the Canadian Charter of Rights and Freedoms.",
    assignments: "Assignment: Case study on freedom of speech (due in 1 week)",
    tests: "Test: Final Exam on Constitutional Law (Date: Dec 12)",
  },
};

const courseSelect = document.getElementById("course");
const contentSelect = document.getElementById("content-type");
const displayTitle = document.getElementById("display-title");
const displayContent = document.getElementById("display-content");

courseSelect.addEventListener("change", updateContentDisplay);
contentSelect.addEventListener("change", updateContentDisplay);

function updateContentDisplay() {
  const selectedCourse = courseSelect.value;
  const selectedContentType = contentSelect.value;

  displayTitle.innerText = `Your ${capitalizeFirstLetter(
    selectedContentType
  )} for ${selectedCourse}:`;

  const content = courseData[selectedCourse][selectedContentType];

  displayContent.innerText =
    content || "No content available for this selection.";
}

function capitalizeFirstLetter(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

updateContentDisplay();
