Hands on 1

Task 1: Testing Types
Unit Testing

Test Case: Verify the create_course() function creates a course object correctly.
Type: Functional Testing

Integration Testing

Test Case: Verify the POST /api/courses/ endpoint successfully stores course details in the database.
Type: Functional Testing

System Testing

Test Case: Create a course using the API and verify it is stored in the database and can be retrieved successfully.
Type: Functional Testing

User Acceptance Testing (UAT)

Test Case: Verify that a college administrator can successfully create a new course through the application.
Type: Functional Testing

Non-Functional Testing Example

Performance Testing: Verify that GET /api/courses/ responds within 2 seconds even when the database contains 1000+ courses.

Black-Box vs White-Box Testing

Black-Box Testing

Tests application functionality without knowing the source code.
Focuses on inputs and outputs.
Usually performed by QA Testers.

White-Box Testing

Tests internal code, logic, and program structure.
Requires programming knowledge.
Usually performed by Developers.
Test Cases for POST /api/courses/
Test Case ID	Description	Preconditions	Test Steps	Expected Result	Actual Result	Pass/Fail
TC001	Create a new course with valid data	API is running	Send POST request with valid course details	Course created successfully (201 Created)		
TC002	Create course with duplicate course code	Course already exists	Send POST request with existing course code	Error message returned (409 Conflict)		
TC003	Create course with missing required fields	API is running	Send POST request without course name	Validation error returned (400 Bad Request)		
Task 2: Defect Lifecycle
Defect Lifecycle
New
 ↓
Assigned
 ↓
Open
 ↓
Fixed
 ↓
Retest
 ↓
Verified
 ↓
Closed

Rejected → Bug is invalid or cannot be reproduced.

Deferred → Bug fix is postponed to a future release.
Severity and Priority Classification
a) POST /api/courses/ returns 500 Internal Server Error
Severity: Critical
Priority: P1
Reason: Core functionality is completely broken.
b) Course names longer than 150 characters are silently truncated
Severity: Medium
Priority: P3
Reason: Data loss occurs but application still works.
c) Typo in Swagger Documentation
Severity: Low
Priority: P4
Reason: Cosmetic issue with no functional impact.
d) Login occasionally returns 401 for valid credentials
Severity: High
Priority: P1
Reason: Users cannot reliably access the system.
Defect Report

Defect ID: BUG-001

Title: POST /api/courses/ returns 500 Internal Server Error

Environment: Local Development

Build Version: v1.0

Severity: Critical

Priority: P1

Steps to Reproduce:

Open Postman.
Send a POST request to /api/courses/.
Provide valid course details.
Click Send.

Expected Result:
Course should be created successfully with HTTP 201.

Actual Result:
API returns HTTP 500 Internal Server Error.

Attachment:
Screenshot of 500 error.

Severity vs Priority

Severity indicates how serious the defect is.

Priority indicates how quickly the defect should be fixed.

Example:
A company logo missing on the homepage has Low Severity but High Priority if the application is about to be demonstrated to clients.




Hands on 2



HANDS-ON 2 – SDLC vs TDLC (V-Model & Agile QA Integration)
Task 1: V-Model Mapping
Requirements
      │
      ▼
System Design
      │
      ▼
Architecture Design
      │
      ▼
Module Design
      │
      ▼
Coding
      ▲
      │
Unit Testing
      ▲
      │
Integration Testing
      ▲
      │
System Testing
      ▲
      │
Acceptance Testing
SDLC ↔ TDLC Mapping
SDLC Phase	Corresponding Testing Phase	Test Artifact
Requirements	Acceptance Testing	Acceptance Test Plan
System Design	System Testing	System Test Cases
Architecture Design	Integration Testing	Integration Test Plan
Module Design	Unit Testing	Unit Test Cases
Entry and Exit Criteria
Unit Testing

Entry Criteria:

Module development completed.
Source code available.

Exit Criteria:

All unit test cases passed.
No critical defects.
Integration Testing

Entry Criteria:

Individual modules tested successfully.

Exit Criteria:

Module interactions verified.
No major integration defects.
System Testing

Entry Criteria:

Complete application deployed.

Exit Criteria:

Functional and non-functional testing completed.
No critical defects remain.
Acceptance Testing

Entry Criteria:

System testing completed successfully.

Exit Criteria:

Customer approves the application.
Early QA Involvement
Requirement Review
Design Review
Task 2: Agile QA & Shift-Left Testing
Problems with Waterfall Testing
Defects are identified very late.
Bug fixing becomes expensive.
Project delivery is delayed.
QA Role in Agile
Sprint Planning
Review user stories.
Define acceptance criteria.
Estimate testing effort.
Daily Stand-up
Report testing progress.
Discuss blockers.
Coordinate with developers.
Sprint Review
Verify completed features.
Validate acceptance criteria.
Demonstrate tested functionality.
Retrospective
Discuss issues faced during testing.
Suggest process improvements.
Improve testing practices.
Shift-Left Practices
Review requirements before development.
Write test cases before coding (TDD/BDD).
Perform static code analysis.
Conduct API contract testing before integration.
Acceptance Criteria (Gherkin)
Scenario 1: Happy Path
Given the college admin is logged into the system
When valid course details are entered
Then the course should be created successfully
Scenario 2: Duplicate Course Code
Given a course with the same course code already exists
When the admin submits the course details
Then the system should display a duplicate course code error
Scenario 3: Missing Required Fields
Given the admin leaves required fields empty
When the admin submits the form
Then validation errors should be displayed and the course should not be created