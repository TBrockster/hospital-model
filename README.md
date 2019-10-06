# hospital-model

## Approach

I spent the first few minutes planning out the model for my classes and my database. I decided on having a TeamMember class and a Teams class, since logic needs to be tested for individuals and teams as a whole. I then decided on a simple database layout with two tables, one for TeamMembers and one for Teams, demonstrated below.


| id | profilePicture | firstName | lastName | type | onLeave | specialities | biography |
|--|--|--|--|--|--|--|--|
| 1 | www.profilepicture.com/John | John | Doe | Surgeon | false | [Neuro, Cardiac] | Loves Cats |
| 2 | www.profilepicture.com/Jane | Jane | Doe | Nurse | true | [Paediatrics] | Hates Cats |

| TeamID | MemberID |
|--|--|
| 1 | 1 |
| 1 | 2 |
| 2 | 2 |
| 2 | 3 |

Since this is the first project I have worked on using Python, I was unfamiliar with the options for frameworks, and so I spent a few minutes researching them, and decided on Django for its Django REST Framework module. I followed some basic setup guide steps, and begun the work on the TeamMember and Team models. I decided to use Pytest for my unit testing, as it is the only Python testing library that I am familiar with.

## Still To Do

 - Rework tests with doubles
 - Create database, migrations and tables.
 - Create API.
