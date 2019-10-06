# hospital-model

## Approach

I spent the first few minutes planning out the model for my classes and my database. I decided on having a TeamMember class and a Teams class, since logic needs to be tested for individuals and teams as a whole. I then decided on a simple database layout with two tables, one for TeamMembers and one for Teams, demonstrated below.


| id | profilePicture | firstName | lastName | type | onLeave | specialities | biography |
| 1 | www.profilepicture.com/John | John | Doe | Surgeon | false | [Neuro, Cardiac] | Loves Cats |
| 2 | www.profilepicture.com/Jane | Jane | Doe | Nurse | true | [Paediatrics] | Hates Cats |

| TeamID | MemberID |
| 1 | 1 |
| 1 | 2 |
| 2 | 2 |
| 2 | 3 |