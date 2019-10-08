# hospital-model

## API URLs

 - http://127.0.0.1:8000/teams/
   - Lists all teams, including their attributes:
     - ID: An automatically incrementing IntegerField, used as the primary key field.
     - teamName: A unique name for the team, following the convention of colour + animal (Blue Tiger).
     - teamMembers: A list of all team members belonging to this team, including all their attributes, explained below.
   - Allows List and Create.

 - http://127.0.0.1:8000/teams/{id}
   - A specific view for an individual team depending on the ID in the URL.
   - Lists the same attributes as /teams.
   - Allows for Retrieve, Update and Destroy.

 - http://127.0.0.1:8000/teammembers/
   - Lists all teamMembers, and their attributes:
     - ID: An automatically incrementing IntegerField, used as the primary key field.
     - profilePicture: A URLField to a profile picture.
     - firstName: A CharField to store a team members first name.
     - lastName: A CharField to store a team members last name.
     - type: A CharField to store a team members 'type' (Surgeon, Nurse or Admin Assistant).
     - onLeave: A BooleanField to store if a team member is on leave.
     - specialities: A CharField to store any specialites of a team member (Renal, Orthopaedics, etc).
     - biography: A TextField to store a team members biography.
   - Allows for List and Create.

 - http://127.0.0.1:8000/teammembers/{id}
   - A specific view for an individual team member depending on the ID in the URL.
   - Lists the same attributes as /teammembers.
   - Allows for Retrieve, Update and Destroy.

## Approach

I spent the first few minutes planning out the model for my classes and my database. I decided on having a TeamMember class and a Teams class, since logic needs to be tested for individuals and teams as a whole. I then decided on a simple database layout with two tables, one for TeamMembers and one for Teams, demonstrated below.


| id | profilePicture | firstName | lastName | type | onLeave | specialities | biography |
|--|--|--|--|--|--|--|--|
| 1 | www.profilepicture.com/John | John | Doe | Surgeon | false | Neuro, Cardiac | Loves Cats |
| 2 | www.profilepicture.com/Jane | Jane | Doe | Nurse | true | Paediatrics | Hates Cats |

| TeamID | MemberID |
|--|--|
| 1 | 1 |
| 1 | 2 |
| 2 | 2 |
| 2 | 3 |

Since this is the first project I have worked on using Python, I was unfamiliar with the options for frameworks, and so I spent a few minutes researching them, and decided on Django for its Django REST Framework module. I followed some basic setup guide steps, and begun the work on the TeamMember and Team models. I decided to use Pytest for my unit testing, as it is the only Python testing library that I am familiar with.

## Still To Do

 - Link API and logic.
 - Setup permissions.